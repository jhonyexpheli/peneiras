"""Indicadores de referência: Banco Central (SGS) e Tesouro Direto (taxa da NTN-B).

Uso: python ferramentas/macro.py --saida dados_oficiais/macro.json

Banco Central, SGS (api.bcb.gov.br, sem chave), conferido em 10/11/2026:
    432    meta da Selic (% a.a.); a série já traz a meta vigente até a próxima reunião do Copom
    4389   CDI anualizado base 252 (% a.a.)
    13522  IPCA acumulado em 12 meses (%)
Tesouro Transparente: preços e taxas diárias do Tesouro Direto (CSV público). Daqui sai a taxa
real da NTN-B (Tesouro IPCA+), a régua para o prêmio do DY dos FIIs.
Cada fonte que falhar fica registrada como erro; as demais seguem.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import pathlib

import requests

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
SGS = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{id}/dados?formato=json&dataInicial={ini}&dataFinal={fim}"
SERIES = {"selic_meta": 432, "cdi": 4389, "ipca_12m": 13522}
TESOURO = ("https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/"
           "resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/precotaxatesourodireto.csv")


def sgs(id_, hoje):
    # Janela de datas e não "últimos N": a meta da Selic vem preenchida até a próxima reunião do
    # Copom, e os últimos pontos da série são datas futuras. O IPCA sai com uns 40 dias de atraso.
    ini = (hoje - dt.timedelta(days=120)).strftime("%d/%m/%Y")
    r = requests.get(SGS.format(id=id_, ini=ini, fim=hoje.strftime("%d/%m/%Y")), headers={"User-Agent": UA}, timeout=60)
    r.raise_for_status()
    pts = []
    for x in r.json():
        d = dt.datetime.strptime(x["data"], "%d/%m/%Y").date()
        if d <= hoje:  # a meta da Selic vem preenchida para datas futuras
            pts.append((d, float(x["valor"])))
    d, v = max(pts)
    return {"valor": v, "data": d.isoformat(), "fonte": f"Banco Central, SGS série {id_}"}


def num(s):
    return float(s.replace(".", "").replace(",", ".")) if s and s.strip() else None


def ntnb():
    """Taxa real de compra do Tesouro IPCA+ no dia mais recente do arquivo.

    Usa a média dos títulos com mais de 5 anos para o vencimento (a NTN-B que um FII de renda
    disputa) e guarda cada título usado.
    """
    r = requests.get(TESOURO, headers={"User-Agent": UA}, timeout=300)
    r.raise_for_status()
    txt = r.content.decode("latin1")
    linhas = list(csv.DictReader(io.StringIO(txt), delimiter=";"))
    col = {k.lower(): k for k in linhas[0]}
    tipo, venc, base = col["tipo titulo"], col["data vencimento"], col["data base"]
    taxa = next(v for k, v in col.items() if k.startswith("taxa compra"))
    data = lambda s: dt.datetime.strptime(s, "%d/%m/%Y").date()
    ipca = [x for x in linhas if x[tipo].strip() in ("Tesouro IPCA+", "Tesouro IPCA+ com Juros Semestrais")]
    ultimo = max(data(x[base]) for x in ipca)
    titulos = []
    for x in ipca:
        if data(x[base]) != ultimo or num(x[taxa]) is None:
            continue
        anos = (data(x[venc]) - ultimo).days / 365.25
        titulos.append({"titulo": x[tipo].strip(), "vencimento": data(x[venc]).isoformat(), "anos": round(anos, 1), "taxa": num(x[taxa])})
    longos = [t for t in titulos if t["anos"] >= 5] or titulos
    return {
        "valor": round(sum(t["taxa"] for t in longos) / len(longos), 2),
        "data": ultimo.isoformat(),
        "regra": "média da taxa real de compra dos Tesouro IPCA+ com mais de 5 anos até o vencimento",
        "titulos": sorted(titulos, key=lambda t: t["vencimento"]),
        "fonte": "Tesouro Transparente, preços e taxas do Tesouro Direto",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--saida", default="dados_oficiais/macro.json")
    a = ap.parse_args()
    hoje = dt.date.today()
    out, erros = {"coletado_em": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}, {}
    for k, id_ in SERIES.items():
        try:
            out[k] = sgs(id_, hoje)
        except Exception as e:  # segue com as demais
            erros[k] = str(e)[:200]
    try:
        out["ntnb"] = ntnb()
    except Exception as e:
        erros["ntnb"] = str(e)[:200]
    if erros:
        out["erros"] = erros
    p = pathlib.Path(a.saida)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2), "utf-8")
    print(json.dumps({k: (v.get("valor") if isinstance(v, dict) else v) for k, v in out.items()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
