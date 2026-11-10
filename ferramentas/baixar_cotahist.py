"""Baixa as séries históricas oficiais da B3 (COTAHIST) e grava o mercado à vista num CSV compacto.

Uso:
    python ferramentas/baixar_cotahist.py --desde 2016 --cache cache/cotahist \
        --saida dados_oficiais/cotahist_vista.csv.gz

Arquivos da B3 (gratuitos, sem chave):
    COTAHIST_A{ano}.ZIP       ano inteiro; o do ano corrente é atualizado ao longo do ano
    COTAHIST_D{ddmmaaaa}.ZIP  um pregão; usado para completar os dias que o anual ainda não trouxe

Layout (posições de 1 a 245, documento "SeriesHistoricas_Layout" da B3), conferido em 10/11/2026
numa linha real de PETR4 de 05/11/2026:
    03-10 data  11-12 CODBDI  13-24 ticker  25-27 tipo de mercado (010 = à vista)
    40-49 especificação  57-69 abertura  70-82 máxima  83-95 mínima  109-121 fechamento
    148-152 negócios  153-170 quantidade  171-188 volume  211-217 fator de cotação  231-242 ISIN
    Preços e volume com 2 casas decimais implícitas. Preço por unidade = preço / fator de cotação.

Anos já fechados ficam no cache e não são baixados de novo.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import io
import pathlib
import time
import zipfile

import requests

URL = "https://bvmf.bmfbovespa.com.br/InstDados/SerHist/{nome}"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
# CODBDI mantidos: 02 lote padrão, 05/06 sancionadas e concordatárias, 07 recuperação extrajudicial,
# 08 recuperação judicial, 12 e 13 fundos imobiliários, 14 certificados e fundos (ETF, Fiagro).
# Ficam de fora BDRs (34-36), direitos e recibos (10) e bônus (22), que nenhuma das peneiras usa.
CODBDI = {"02", "05", "06", "07", "08", "12", "13", "14"}
COLUNAS = ["data", "codbdi", "ticker", "especi", "abertura", "maxima", "minima", "fechamento",
           "negocios", "quantidade", "volume", "isin"]


def baixar(nome: str, destino: pathlib.Path, tentativas: int = 4) -> bool:
    """Grava o zip em destino. Devolve False quando a B3 não tem o arquivo (404: fim de semana, feriado)."""
    ultimo = None
    for i in range(tentativas):
        try:
            r = requests.get(URL.format(nome=nome), headers={"User-Agent": UA}, timeout=300)
            if r.status_code == 404:
                return False
            if r.status_code == 200 and r.content[:2] == b"PK":
                destino.parent.mkdir(parents=True, exist_ok=True)
                destino.write_bytes(r.content)
                return True
            ultimo = f"HTTP {r.status_code}, {len(r.content)} bytes"
        except requests.RequestException as e:
            ultimo = str(e)
        time.sleep(3 * (2 ** i))
    raise RuntimeError(f"falha ao baixar {nome}: {ultimo}")


def registros(zip_path: pathlib.Path):
    """Linhas do mercado à vista (tipo de mercado 010) de um zip COTAHIST."""
    with zipfile.ZipFile(zip_path) as z:
        with z.open(z.namelist()[0]) as fh:
            for bruta in io.TextIOWrapper(fh, encoding="latin1"):
                if not bruta.startswith("01") or bruta[24:27] != "010" or bruta[10:12] not in CODBDI:
                    continue
                fator = int(bruta[210:217] or 1) or 1
                preco = lambda a, b: int(bruta[a - 1:b]) / 100 / fator
                d = bruta[2:10]
                yield {
                    "data": f"{d[:4]}-{d[4:6]}-{d[6:]}",
                    "codbdi": bruta[10:12],
                    "ticker": bruta[12:24].strip(),
                    "especi": bruta[39:49].strip(),
                    "abertura": preco(57, 69),
                    "maxima": preco(70, 82),
                    "minima": preco(83, 95),
                    "fechamento": preco(109, 121),
                    "negocios": int(bruta[147:152]),
                    "quantidade": int(bruta[152:170]),
                    "volume": int(bruta[170:188]) / 100,
                    "isin": bruta[230:242],
                }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", type=int, default=2016)
    ap.add_argument("--cache", default="cache/cotahist")
    ap.add_argument("--saida", default="dados_oficiais/cotahist_vista.csv.gz")
    a = ap.parse_args()
    cache = pathlib.Path(a.cache)
    hoje = dt.date.today()

    saida = pathlib.Path(a.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    datas, n, tickers = set(), 0, set()
    # Grava linha a linha (onze anos de pregões não cabem confortavelmente em memória).
    with gzip.open(saida, "wt", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=COLUNAS)
        w.writeheader()

        def gravar(z):
            nonlocal n
            k = 0
            for r in registros(z):
                w.writerow(r)
                datas.add(r["data"])
                tickers.add(r["ticker"])
                k += 1
            n += k
            return k

        for ano in range(a.desde, hoje.year + 1):
            z = cache / f"COTAHIST_A{ano}.ZIP"
            if ano < hoje.year and z.exists():
                origem = "cache"
            elif baixar(z.name, z):
                origem = "baixado"
            else:
                print(f"{z.name}: a B3 ainda não publicou")
                continue
            print(f"{z.name} ({origem}, {z.stat().st_size / 1e6:.0f} MB): {gravar(z)} linhas à vista")

        # Pregões que o arquivo anual ainda não trouxe: completa com os arquivos diários.
        ultima = max(datas) if datas else f"{a.desde}-01-01"
        d = dt.date.fromisoformat(ultima) + dt.timedelta(days=1)
        while d <= hoje:
            if d.weekday() < 5:
                z = cache / "diarios" / f"COTAHIST_D{d:%d%m%Y}.ZIP"
                if z.exists() or baixar(z.name, z):
                    print(f"{z.name}: {gravar(z)} linhas à vista")
            d += dt.timedelta(days=1)

    print(f"{saida}: {n} linhas, {len(tickers)} tickers, {len(datas)} pregões, de {min(datas)} a {max(datas)}")

if __name__ == "__main__":
    main()
