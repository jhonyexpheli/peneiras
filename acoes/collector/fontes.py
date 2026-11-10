"""Clientes das fontes de dados do screener.

Cada função devolve dados crus (dict/list) já decodificados, sem cálculo.
Todos os endpoints ficam centralizados aqui para o site poder trocar de
fonte (ex.: brapi com token) sem mexer no restante do código.

Fontes:
  - Status Invest (não oficial, público): universo de ações, liquidez, setor,
    indicadores atuais e histórico anual de ~30 indicadores (10 pontos).
  - Fundamentus (não oficial, público): balanço e DRE resumidos por ação
    (caixa, dívida, PL, EBIT e lucro 12m e do último trimestre) e cotações diárias.
  - CVM dados abertos (oficial): cadastro de companhias abertas com a
    situação do emissor (recuperação judicial, falência, liquidação...).
  - brapi.dev (opcional, com token): cotações históricas, alternativa para produção.

Acesso testado em 31/10/2026: Status Invest responde 403 a chamadas de servidor
(Cloudflare) e o cot_hist do Fundamentus devolve corpo vazio fora de uma sessão de
navegador. Para esses dois casos, ver coletar_navegador.js. Fundamentus detalhes,
CVM e brapi funcionam direto do servidor.
"""
from __future__ import annotations

import csv
import io
import json
import math
import os
import time
from typing import Any

import requests
from bs4 import BeautifulSoup

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/130.0 Safari/537.36"
)

ENDPOINTS = {
    "si_busca": "https://statusinvest.com.br/category/advancedsearchresultpaginated",
    "si_historico": "https://statusinvest.com.br/acao/indicatorhistoricallist",
    "fund_detalhes": "https://www.fundamentus.com.br/detalhes.php",
    "fund_cotacoes": "https://www.fundamentus.com.br/amline/cot_hist.php",
    "fund_resultado": "https://www.fundamentus.com.br/resultado.php",
    "cvm_cadastro": "https://dados.cvm.gov.br/dados/CIA_ABERTA/CAD/DADOS/cad_cia_aberta.csv",
    "brapi_quote": "https://brapi.dev/api/quote/{ticker}",
}

_session = requests.Session()
_session.headers.update({"User-Agent": UA, "Accept-Language": "pt-BR,pt;q=0.9"})


def _get(url: str, *, params=None, data=None, method="GET", tries=4, pausa=1.5, **kw) -> requests.Response:
    ultimo = None
    for i in range(tries):
        try:
            r = _session.request(method, url, params=params, data=data, timeout=40, **kw)
            # Fundamentus devolve 200 com corpo vazio quando limita a taxa.
            if r.status_code == 200 and r.content:
                return r
            ultimo = f"HTTP {r.status_code}, {len(r.content)} bytes"
        except requests.RequestException as e:  # rede instável
            ultimo = str(e)
        time.sleep(pausa * (2 ** i))
    raise RuntimeError(f"falha em {url}: {ultimo}")


# ---------------------------------------------------------------- Status Invest

def si_universo() -> list[dict]:
    """Todas as ações listadas com indicadores atuais, setor e liquidez média diária."""
    r = _get(
        ENDPOINTS["si_busca"],
        params={"search": "{}", "orderColumn": "", "isAsc": "", "page": 0, "take": 3000, "CategoryType": 1},
        headers={"X-Requested-With": "XMLHttpRequest"},
    )
    return r.json()["list"]


def si_historico(ticker: str) -> dict[str, list[list]]:
    """Histórico anual de indicadores: {indicador: [[ano, tipo, valor], ...]}.

    tipo 1 = ano corrente (últimos 12 meses), tipo 0 = exercício fechado.
    time=7 é a janela máxima do endpoint (ano corrente + 9 exercícios).
    O endpoint aceita vários codes[], mas só responde o primeiro: chamar um a um.
    """
    r = _get(
        ENDPOINTS["si_historico"],
        method="POST",
        data={"codes[]": ticker, "time": 7, "byQuarter": "false", "futureData": "false"},
        headers={"X-Requested-With": "XMLHttpRequest"},
    )
    arr = next(iter((r.json().get("data") or {}).values()), []) or []
    return {ind["key"]: [[x["rank"], x["timeType"], x.get("value")] for x in ind.get("ranks", [])] for ind in arr}


# ---------------------------------------------------------------- Fundamentus

def _num(s: str | None) -> float | None:
    if s is None:
        return None
    s = s.strip().replace("%", "")
    if s in ("", "-"):
        return None
    try:
        return float(s.replace(".", "").replace(",", "."))
    except ValueError:
        return None


def fund_detalhes(ticker: str) -> dict:
    """Ficha do Fundamentus: info, balanço, DRE (12m e 3m) e oscilações anuais."""
    r = _get(ENDPOINTS["fund_detalhes"], params={"papel": ticker})
    html = r.content.decode("iso-8859-1")
    soup = BeautifulSoup(html, "lxml")
    c = [td.get_text(" ", strip=True).lstrip("?").strip() for td in soup.select("table.w728 td")]

    def get(lab):
        try:
            return c[c.index(lab) + 1]
        except ValueError:
            return None

    info_keys = ["Cotação", "Data últ cot", "Empresa", "Setor", "Subsetor", "Tipo", "Vol $ méd (2m)",
                 "Valor de mercado", "Valor da firma", "Últ balanço processado", "Nro. Ações",
                 "Min 52 sem", "Max 52 sem"]
    info = {k: get(k) for k in info_keys}
    bal, dre = {}, {}
    if "Dados Balanço Patrimonial" in c:
        ib = c.index("Dados Balanço Patrimonial")
        ir = c.index("Dados demonstrativos de resultados")
        for i in range(ib + 1, ir - 1, 2):
            if c[i]:
                bal[c[i]] = _num(c[i + 1])
        r_ = c[ir + 3:]
        for i in range(0, len(r_) - 3, 4):
            if r_[i]:
                dre[r_[i]] = [_num(r_[i + 1]), _num(r_[i + 3])]
    osc = {k: _num(get(k)) for k in ["Dia", "Mês", "30 dias", "12 meses"]}
    for y in range(2010, 2031):
        v = get(str(y))
        if v is not None:
            osc[str(y)] = _num(v)
    return {"info": info, "balanco": bal, "dre": dre, "oscilacoes": osc}


def fund_cotacoes(ticker: str) -> list[list]:
    """Série diária de fechamento ajustado [[timestamp_ms, preco], ...] desde a listagem."""
    r = _get(ENDPOINTS["fund_cotacoes"], params={"papel": ticker}, pausa=3)
    return json.loads(r.text)


def fund_resultado() -> dict:
    """Tabela geral do Fundamentus (todas as ações, indicadores atuais)."""
    r = _get(ENDPOINTS["fund_resultado"])
    soup = BeautifulSoup(r.content.decode("iso-8859-1"), "lxml")
    t = soup.select_one("table#resultado")
    hdr = [th.get_text(strip=True) for th in t.select("thead th")]
    rows = [[td.get_text(strip=True) for td in tr.select("td")] for tr in t.select("tbody tr")]
    return {"header": hdr, "rows": rows}


# ---------------------------------------------------------------- CVM

SITUACAO_CVM = {
    "EM RECUPERAÇÃO JUDICIAL OU EQUIVALENTE": "RJ",
    "EM RECUPERAÇÃO EXTRAJUDICIAL": "REJ",
    "FALIDA": "FAL",
    "LIQUIDAÇÃO EXTRAJUDICIAL": "LE",
    "EM LIQUIDAÇÃO JUDICIAL": "LJ",
}


def cvm_cadastro() -> list[dict]:
    """Companhias com registro ATIVO na CVM e a situação do emissor."""
    r = _get(ENDPOINTS["cvm_cadastro"])
    txt = r.content.decode("iso-8859-1")
    keep = ["CNPJ_CIA", "DENOM_SOCIAL", "DENOM_COMERC", "CD_CVM", "SIT", "SIT_EMISSOR",
            "DT_INI_SIT_EMISSOR", "SETOR_ATIV", "CATEG_REG", "TP_MERC"]
    out = []
    for row in csv.DictReader(io.StringIO(txt), delimiter=";"):
        if row.get("SIT") == "ATIVO":
            out.append({k: row.get(k, "") for k in keep})
    return out


# ---------------------------------------------------------------- brapi (opcional)

def brapi_cotacoes(ticker: str, token: str | None = None, rng: str = "2y") -> list[list]:
    """Cotações diárias pela brapi.dev (precisa de token para histórico longo)."""
    token = token or os.environ.get("BRAPI_TOKEN")
    params = {"range": rng, "interval": "1d"}
    if token:
        params["token"] = token
    r = _get(ENDPOINTS["brapi_quote"].format(ticker=ticker), params=params)
    res = r.json()["results"][0].get("historicalDataPrice", [])
    return [[x["date"] * 1000, x["adjustedClose"] or x["close"]] for x in res if x.get("close")]


# ---------------------------------------------------------------- utilidades

def resumo_precos(serie: list[list]) -> dict:
    """Volatilidade anualizada (1 e 2 anos), drawdown de 1 ano e fechamentos mensais (11 anos)."""
    from datetime import datetime, timezone

    if not serie:
        return {}
    ult = serie[-504:]
    rets = [math.log(ult[i][1] / ult[i - 1][1]) for i in range(1, len(ult)) if ult[i - 1][1] > 0 and ult[i][1] > 0]

    def sd(a):
        if len(a) < 2:
            return None
        m = sum(a) / len(a)
        return math.sqrt(sum((x - m) ** 2 for x in a) / (len(a) - 1))

    r1 = rets[-252:]
    pico, mdd = -1.0, 0.0
    for _, v in serie[-252:]:
        pico = max(pico, v)
        mdd = min(mdd, v / pico - 1)
    mensal: dict[str, float] = {}
    for ts, v in serie:
        d = datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
        mensal[f"{d.year}-{d.month:02d}"] = v
    ks = sorted(mensal)[-132:]
    fmt = lambda ts: datetime.fromtimestamp(ts / 1000, tz=timezone.utc).date().isoformat()
    return {
        "primeiro_pregao": fmt(serie[0][0]),
        "ultimo_pregao": fmt(serie[-1][0]),
        "n_pregoes": len(serie),
        "vol_1a": sd(r1) * math.sqrt(252) * 100 if len(r1) > 100 and sd(r1) else None,
        "vol_2a": sd(rets) * math.sqrt(252) * 100 if len(rets) > 200 and sd(rets) else None,
        "max_drawdown_1a": mdd * 100,
        "fechamento_mensal": [[k, mensal[k]] for k in ks],
    }
