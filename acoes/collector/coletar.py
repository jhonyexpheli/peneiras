"""Coleta os dados crus das fontes e grava em data/raw/.

Uso:
    python collector/coletar.py                 # coleta tudo (retoma de onde parou)
    python collector/coletar.py --refazer       # ignora o cache e baixa de novo
    python collector/coletar.py --liquidez 500000

Só as ações com liquidez média diária acima do corte entram nas chamadas
por ação (histórico, ficha e cotações), para poupar as fontes.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import fontes  # noqa: E402

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"


def agora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def carregar(nome: str) -> dict:
    p = RAW / nome
    return json.loads(p.read_text("utf-8")) if p.exists() else {}


def salvar(nome: str, obj) -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    tmp = RAW / (nome + ".tmp")
    tmp.write_text(json.dumps(obj, ensure_ascii=False), "utf-8")
    tmp.replace(RAW / nome)


def por_acao(nome: str, tickers: list[str], fn, refazer: bool, pausa: float, rotulo: str) -> None:
    dados = {} if refazer else carregar(nome)
    base = dados.setdefault("dados", {})
    erros = dados.setdefault("erros", {})
    faltam = [t for t in tickers if t not in base]
    print(f"[{rotulo}] {len(faltam)} de {len(tickers)} a coletar")
    for i, t in enumerate(faltam, 1):
        try:
            base[t] = fn(t)
            erros.pop(t, None)
        except Exception as e:  # segue para o próximo e registra
            erros[t] = str(e)
        if i % 20 == 0:
            dados["coletado_em"] = agora()
            salvar(nome, dados)
            print(f"  {i}/{len(faltam)}")
        time.sleep(pausa)
    dados["coletado_em"] = agora()
    salvar(nome, dados)
    print(f"[{rotulo}] ok: {len(base)}  erros: {len(erros)}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--liquidez", type=float, default=1_000_000)
    ap.add_argument("--refazer", action="store_true")
    ap.add_argument("--sem-precos", action="store_true")
    ap.add_argument("--fonte-precos", choices=["fundamentus", "brapi"], default="fundamentus")
    a = ap.parse_args()

    uni = fontes.si_universo()
    salvar("si_universo.json", {"fonte": fontes.ENDPOINTS["si_busca"], "coletado_em": agora(), "lista": uni})
    tickers = sorted(x["ticker"] for x in uni if (x.get("liquidezmediadiaria") or 0) >= a.liquidez)
    print(f"universo {len(uni)}, com liquidez >= {a.liquidez:,.0f}: {len(tickers)}")

    salvar("cvm_cadastro.json", {"fonte": fontes.ENDPOINTS["cvm_cadastro"], "coletado_em": agora(), "linhas": fontes.cvm_cadastro()})
    salvar("fund_resultado.json", {"fonte": fontes.ENDPOINTS["fund_resultado"], "coletado_em": agora(), **fontes.fund_resultado()})

    por_acao("si_historico.json", tickers, fontes.si_historico, a.refazer, 0.3, "historico Status Invest")
    por_acao("fund_detalhes.json", tickers, fontes.fund_detalhes, a.refazer, 0.4, "fichas Fundamentus")
    if not a.sem_precos:
        if a.fonte_precos == "brapi":
            fn = lambda t: fontes.resumo_precos(fontes.brapi_cotacoes(t))
        else:
            fn = lambda t: fontes.resumo_precos(fontes.fund_cotacoes(t))
        por_acao("precos.json", tickers, fn, a.refazer, 1.5, f"cotações ({a.fonte_precos})")


if __name__ == "__main__":
    main()
