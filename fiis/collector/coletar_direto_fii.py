"""Coleta pelo servidor: informes da CVM e Fundamentus.

Uso:  python collector/coletar_direto_fii.py [--liq-min 50000] [--sem-cvm]

Grava em data/raw/:
  cvm/inf_mensal_fii_AAAA.zip        (2016 até o ano corrente)
  cvm/inf_trimestral_fii_AAAA.zip    (últimos 3 anos)
  fundamentus_fii_resultado.json     (tabela geral)
  fundamentus_fii_detalhes.json      (ficha de cada fundo com liquidez >= liq-min)
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
import time

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import fontes_fii as F  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--liq-min", type=float, default=50_000)
    ap.add_argument("--sem-cvm", action="store_true")
    a = ap.parse_args()
    (RAW / "cvm").mkdir(parents=True, exist_ok=True)
    ano = dt.date.today().year

    if not a.sem_cvm:
        for y in range(2016, ano + 1):
            (RAW / "cvm" / f"inf_mensal_fii_{y}.zip").write_bytes(F.cvm_zip("mensal", y))
            print("mensal", y)
        for y in range(ano - 2, ano + 1):
            (RAW / "cvm" / f"inf_trimestral_fii_{y}.zip").write_bytes(F.cvm_zip("trimestral", y))
            print("trimestral", y)

    tabela = F.fund_fii_resultado()
    (RAW / "fundamentus_fii_resultado.json").write_text(json.dumps(tabela, ensure_ascii=False), "utf-8")
    print("fundamentus tabela:", len(tabela))

    alvo = [x["ticker"] for x in tabela if (x["liquidez"] or 0) >= a.liq_min]
    caminho = RAW / "fundamentus_fii_detalhes.json"
    det = json.loads(caminho.read_text("utf-8")) if caminho.exists() else {}
    for i, t in enumerate(alvo):
        if det.get(t, {}).get("_coletado") == str(dt.date.today()):
            continue
        try:
            d = F.fund_detalhes(t)
            d["_coletado"] = str(dt.date.today())
            det[t] = d
        except Exception as e:  # fonte instável: segue e registra
            det[t] = {"erro": str(e)[:200]}
        if i % 20 == 0:
            caminho.write_text(json.dumps(det, ensure_ascii=False), "utf-8")
            print(f"detalhes {i}/{len(alvo)}")
        time.sleep(0.8)
    caminho.write_text(json.dumps(det, ensure_ascii=False), "utf-8")
    print("detalhes:", len(det))


if __name__ == "__main__":
    main()
