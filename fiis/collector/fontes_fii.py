"""Clientes das fontes de dados da Peneira FIIs.

Projeto separado da Peneira de Valor (screener/): nada aqui importa de lá.
Cada função devolve dados crus, sem aplicar o método.

Fontes:
  - CVM dados abertos (oficial): informes mensal e trimestral estruturados de FII.
    Mensal: PL, VP da cota, cotas, cotistas, composição do ativo e passivo (desde 2016).
    Trimestral: imóveis (área, vacância, inadimplência), resultado e rendimentos declarados.
  - Fundamentus (não oficial): tabela geral de FIIs e ficha de cada fundo
    (FFO, receita, venda de ativos e rendimento distribuído em 12m e 3m).
  - Status Invest (não oficial, só pelo navegador): universo, setor, cotistas e
    histórico de rendimentos por cota (data com e data de pagamento).
  - Yahoo Finance chart API (não oficial, só pelo navegador): cotações sem ajuste
    por proventos (mensais 10 anos e diárias 2 anos).

Acesso testado em 03/11/2026: CVM e Fundamentus respondem ao servidor;
Status Invest responde 403 ao servidor e o Yahoo é lido numa aba do navegador
(ver coletar_navegador_fii.js). Tesouro Transparente bloqueado neste ambiente.
"""
from __future__ import annotations

import csv
import io
import time
import zipfile

import requests
from bs4 import BeautifulSoup

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)

ENDPOINTS = {
    "cvm_mensal": "https://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/inf_mensal_fii_{ano}.zip",
    "cvm_trimestral": "https://dados.cvm.gov.br/dados/FII/DOC/INF_TRIMESTRAL/DADOS/inf_trimestral_fii_{ano}.zip",
    "fund_fii_resultado": "https://www.fundamentus.com.br/fii_resultado.php",
    "fund_detalhes": "https://www.fundamentus.com.br/detalhes.php",
    # pelo navegador:
    "si_busca": "https://statusinvest.com.br/category/advancedsearchresultpaginated?CategoryType=2",
    "si_proventos": "https://statusinvest.com.br/fii/companytickerprovents?ticker={ticker}&chartProventsType=2",
    "yahoo_chart": "https://query1.finance.yahoo.com/v8/finance/chart/{ticker}.SA",
}

_s = requests.Session()
_s.headers.update({"User-Agent": UA, "Accept-Language": "pt-BR,pt;q=0.9"})


def _get(url, *, params=None, tries=4, pausa=1.5):
    ultimo = None
    for i in range(tries):
        try:
            r = _s.get(url, params=params, timeout=60)
            if r.status_code == 200 and r.content:
                return r
            ultimo = f"HTTP {r.status_code}, {len(r.content)} bytes"
        except requests.RequestException as e:
            ultimo = str(e)
        time.sleep(pausa * (2 ** i))
    raise RuntimeError(f"falha em {url}: {ultimo}")


def num(s):
    """Número no formato brasileiro ("1.234,56", "9,5%") ou None."""
    if s is None:
        return None
    s = str(s).strip().replace("%", "")
    if s in ("", "-"):
        return None
    try:
        return float(s.replace(".", "").replace(",", "."))
    except ValueError:
        return None


# ---------------------------------------------------------------- CVM

def cvm_zip(tipo: str, ano: int) -> bytes:
    """Zip do informe ('mensal' ou 'trimestral') de um ano."""
    return _get(ENDPOINTS[f"cvm_{tipo}"].format(ano=ano)).content


def cvm_tabelas(conteudo_zip: bytes, prefixo: str) -> list[dict]:
    """Lê do zip o CSV cujo nome começa com o prefixo (ex.: 'inf_mensal_fii_complemento').

    As colunas mudaram com a Resolução CVM 175: CNPJ_Fundo virou CNPJ_Fundo_Classe.
    Aqui as duas viram 'cnpj'.
    """
    import re
    z = zipfile.ZipFile(io.BytesIO(conteudo_zip))
    # nome exato (prefixo_AAAA.csv): 'imovel' não pode pegar 'imovel_renda_acabado_inquilino'
    nomes = [n for n in z.namelist() if re.fullmatch(re.escape(prefixo) + r"_\d{4}\.csv", n)]
    out = []
    for n in nomes:
        txt = z.read(n).decode("latin1")
        for row in csv.DictReader(io.StringIO(txt), delimiter=";"):
            row["cnpj"] = row.get("CNPJ_Fundo_Classe") or row.get("CNPJ_Fundo")
            out.append(row)
    return out


# ---------------------------------------------------------------- Fundamentus

def fund_fii_resultado() -> list[dict]:
    """Tabela geral de FIIs do Fundamentus, uma linha por ticker."""
    r = _get(ENDPOINTS["fund_fii_resultado"])
    soup = BeautifulSoup(r.content.decode("iso-8859-1"), "lxml")
    t = soup.select_one("table")
    hdr = [th.get_text(strip=True) for th in t.select("thead th")]
    out = []
    for tr in t.select("tbody tr"):
        c = [td.get_text(strip=True) for td in tr.select("td")]
        d = dict(zip(hdr, c))
        out.append({
            "ticker": d.get("Papel"),
            "segmento_fund": d.get("Segmento"),
            "cotacao": num(d.get("Cotação")),
            "ffo_yield": num(d.get("FFO Yield")),
            "dy": num(d.get("Dividend Yield")),
            "p_vp": num(d.get("P/VP")),
            "valor_mercado": num(d.get("Valor de Mercado")),
            "liquidez": num(d.get("Liquidez")),
            "qtd_imoveis": num(d.get("Qtd de imóveis")),
            "preco_m2": num(d.get("Preço do m2")),
            "aluguel_m2": num(d.get("Aluguel por m2")),
            "cap_rate": num(d.get("Cap Rate")),
            "vacancia_media": num(d.get("Vacância Média")),
        })
    return out


def fund_detalhes(ticker: str) -> dict:
    """Ficha do fundo no Fundamentus: resultado 12m e 3m, balanço, imóveis."""
    r = _get(ENDPOINTS["fund_detalhes"], params={"papel": ticker})
    soup = BeautifulSoup(r.content.decode("iso-8859-1"), "lxml")
    c = [td.get_text(" ", strip=True).lstrip("?").strip() for td in soup.select("table.w728 td")]
    if "Nome" not in c:
        return {}

    def depois(rotulo, n=1):
        idx = [i for i, x in enumerate(c) if x == rotulo]
        return c[idx[n - 1] + 1] if len(idx) >= n else None

    return {
        "nome": depois("Nome"),
        "data_ult_cot": depois("Data últ cot"),
        "mandato": depois("Mandato"),
        "segmento": depois("Segmento"),
        "gestao": depois("Gestão"),
        "liquidez_2m": num(depois("Vol $ méd (2m)")),
        "valor_mercado": num(depois("Valor de mercado")),
        "cotas": num(depois("Nro. Cotas")),
        "relatorio": depois("Relatório"),
        "ult_trimestral": depois("Últ Info Trimestral"),
        "ffo_cota": num(depois("FFO/Cota")),
        "dividendo_cota": num(depois("Dividendo/cota")),
        "vp_cota": num(depois("VP/Cota")),
        "receita_12m": num(depois("Receita", 1)),
        "receita_3m": num(depois("Receita", 2)),
        "venda_ativos_12m": num(depois("Venda de ativos", 1)),
        "venda_ativos_3m": num(depois("Venda de ativos", 2)),
        "ffo_12m": num(depois("FFO", 1)),
        "ffo_3m": num(depois("FFO", 2)),
        "rend_distribuido_12m": num(depois("Rend. Distribuído", 1)),
        "rend_distribuido_3m": num(depois("Rend. Distribuído", 2)),
        "ativos": num(depois("Ativos")),
        "patrimonio": num(depois("Patrim Líquido")),
        "qtd_imoveis": num(depois("Qtd imóveis")),
        "area_m2": num(depois("Área (m2)")),
        "cap_rate": num(depois("Cap Rate")),
        "vacancia_media": num(depois("Vacância Média")),
        "imoveis_pl": num(depois("Imóveis/PL do FII")),
    }
