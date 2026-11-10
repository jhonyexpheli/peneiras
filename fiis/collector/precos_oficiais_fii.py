"""Cotações dos FIIs pela B3 (COTAHIST), no lugar do Yahoo Finance lido pelo navegador.

Uso: python collector/precos_oficiais_fii.py [--cotahist ../dados_oficiais/cotahist_vista.csv.gz]

Grava data/raw/b3_fii.json com, por ticker, os mesmos campos que montar_base_fii.py lia do Yahoo
(prim, ult, vol, mdd, saltos, n, ye, mens) e mais a liquidez média de 2 meses e o ISIN.
Entram os códigos terminados em 11 com ISIN de fundo (BR....CTF...) ou classificados pela B3 como
fundo imobiliário (CODBDI 12 e 13).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ.parent / "ferramentas"))
import b3  # noqa: E402


def e_fii(ticker, codbdi, isin):
    return bool(re.fullmatch(r"[A-Z]{4}1[12]", ticker)) and (codbdi in ("12", "13") or "CTF" in isin)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cotahist", default=str(RAIZ.parent / "dados_oficiais" / "cotahist_vista.csv.gz"))
    a = ap.parse_args()
    series, pregoes = b3.ler_vista(a.cotahist, e_fii)
    out = {}
    for t, s in series.items():
        r = b3.resumo(s, pregoes, meses_mensal=24)
        if not r:
            continue
        out[t] = {
            "prim": r["primeiro"],
            "ult": [r["data_preco"], r["preco"]],
            "vol": round(r["vol_1a"], 2) if r["vol_1a"] is not None else None,
            "mdd": round(r["mdd_1a"], 2),
            "saltos": r["saltos_1a"],
            "n": r["pregoes_1a"],
            "ye": r["dezembro"],
            "mens": dict(r["mensal"]),
            "liquidez": r["liquidez"],
            "isin": r["isin"],
            "codbdi": r["codbdi"],
            "eventos": r["eventos"],
        }
    destino = RAIZ / "data" / "raw" / "b3_fii.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps({"fonte": "B3, COTAHIST", "ate": pregoes[-1], "pregoes": len(pregoes),
                                   "coletado": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                                   "cotacoes": out}, ensure_ascii=False), "utf-8")
    print(f"b3_fii.json: {len(out)} fundos, pregões até {pregoes[-1]}")


if __name__ == "__main__":
    main()
