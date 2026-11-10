"""Atualiza data/base.json com as fontes oficiais: preços e liquidez da B3 (COTAHIST) e indicadores
de referência (Banco Central e Tesouro).

Uso:
    python collector/atualizar_oficial.py --cotahist ../dados_oficiais/cotahist_vista.csv.gz \
        --macro ../dados_oficiais/macro.json

Etapa 1 da troca de fontes. Substitui o que vinha das cotações do Fundamentus e do Status Invest
lidos pelo navegador:
    preco, data_cotacao, liquidez, vol_1a, vol_2a, saltos_1a, drawdown_1a, mensal
Os balanços e o histórico anual de indicadores continuam da última coleta (Status Invest e
Fundamentus) até a etapa 2 (demonstrativos da CVM).

Para os múltiplos não ficarem defasados do preço novo, o valor de mercado, o valor da firma e os
indicadores de preço da ficha (P/L, P/VP, DY, EV/EBIT, inclusive o ponto "atual" do histórico) são
recalculados a partir da ficha original guardada em "ancora_ficha": valor de mercado cresce na
mesma proporção do preço; valor da firma = valor de mercado + dívida líquida da ficha.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ.parent / "ferramentas"))
import b3  # noqa: E402

PRECO_IND = ["p_l", "p_vp"]        # sobem com o preço
PRECO_INV = ["dy"]                 # caem quando o preço sobe


def ok(v):
    return isinstance(v, (int, float)) and v == v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cotahist", default=str(RAIZ.parent / "dados_oficiais" / "cotahist_vista.csv.gz"))
    ap.add_argument("--macro", default=str(RAIZ.parent / "dados_oficiais" / "macro.json"))
    a = ap.parse_args()

    caminho = RAIZ / "data" / "base.json"
    base = json.loads(caminho.read_text("utf-8"))
    tickers = {x["ticker"] for x in base["acoes"]}
    series, pregoes = b3.ler_vista(a.cotahist, lambda t, cod, isin: t in tickers)
    print(f"COTAHIST: {len(series)} de {len(tickers)} ações com negócios, pregões até {pregoes[-1]}")

    sem, eventos = [], 0
    for x in base["acoes"]:
        r = b3.resumo(series.get(x["ticker"]), pregoes)
        if not r:
            sem.append(x["ticker"])
            x["liquidez"] = 0.0
            x["fonte_preco"] = f"sem negócios na B3 desde {pregoes[0][:4]}"
            continue
        anc = x.get("ancora_ficha")
        if not anc:
            anc = x["ancora_ficha"] = {
                "preco": x.get("preco"), "valor_mercado": x.get("valor_mercado"), "valor_firma": x.get("valor_firma"),
                "data_cotacao": x.get("data_cotacao"), "ind": {k: (x.get("ind") or {}).get(k) for k in PRECO_IND + PRECO_INV + ["ev_ebit"]},
                "hist_atual": {k: next((v for ano, tp, v in (x.get("hist") or {}).get(k, []) if tp == 1), None)
                               for k in PRECO_IND + PRECO_INV + ["ev_ebit"]},
            }
        f = r["preco"] / anc["preco"] if ok(anc.get("preco")) and anc["preco"] > 0 else None
        if f:
            if ok(anc.get("valor_mercado")):
                x["valor_mercado"] = anc["valor_mercado"] * f
                if ok(anc.get("valor_firma")):
                    x["valor_firma"] = anc["valor_firma"] + (x["valor_mercado"] - anc["valor_mercado"])
            ev_f = (x["valor_firma"] / anc["valor_firma"]) if ok(anc.get("valor_firma")) and anc["valor_firma"] and ok(x.get("valor_firma")) else None
            fat = {**{k: f for k in PRECO_IND}, **{k: 1 / f for k in PRECO_INV}, "ev_ebit": ev_f}
            for k, m in fat.items():
                if m is None:
                    continue
                if ok(anc["ind"].get(k)) and x.get("ind") is not None:
                    x["ind"][k] = anc["ind"][k] * m
                h = (x.get("hist") or {}).get(k)
                if h and ok(anc["hist_atual"].get(k)):
                    for p in h:
                        if p[1] == 1:
                            p[2] = anc["hist_atual"][k] * m
        x.update({
            "preco": r["preco"],
            "data_cotacao": dt.date.fromisoformat(r["data_preco"]).strftime("%d/%m/%Y"),
            "liquidez": r["liquidez"],
            "vol_1a": r["vol_1a"], "vol_2a": r["vol_2a"], "saltos_1a": r["saltos_1a"],
            "drawdown_1a": r["mdd_1a"],
            "mensal": r["mensal"],
            "eventos_preco": r["eventos"],
            "fonte_preco": "B3, COTAHIST",
        })
        eventos += len(r["eventos"])

    f = base["meta"]["fontes"]
    f["precos"] = pregoes[-1]
    f["precos_fonte"] = "B3, COTAHIST (fechamento oficial; desdobramentos e grupamentos corrigidos)"
    f["liquidez_fonte"] = "B3, COTAHIST: volume financeiro médio por pregão nos últimos 2 meses"
    try:
        base["macro"] = json.loads(pathlib.Path(a.macro).read_text("utf-8"))
    except FileNotFoundError:
        pass
    base["meta"]["atualizado_oficial_em"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    caminho.write_text(json.dumps(base, ensure_ascii=False, separators=(",", ":")), "utf-8")
    print(f"base.json: {len(base['acoes']) - len(sem)} ações com preço da B3, {len(sem)} sem negócios, "
          f"{eventos} desdobramentos/grupamentos corrigidos")


if __name__ == "__main__":
    main()
