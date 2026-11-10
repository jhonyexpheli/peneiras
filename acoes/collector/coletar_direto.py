"""Coleta o que o servidor alcança direto: CVM (cadastro) e Fundamentus (tabela geral + fichas).
Status Invest (universo, histórico e cotações) exige navegador: ver coletar_navegador.js."""
import json, sys, time
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import fontes
from coletar import salvar, carregar, agora, por_acao

liq_min = float(sys.argv[1]) if len(sys.argv) > 1 else 300_000
salvar("cvm_cadastro.json", {"fonte": fontes.ENDPOINTS["cvm_cadastro"], "coletado_em": agora(), "linhas": fontes.cvm_cadastro()})
res = fontes.fund_resultado()
salvar("fund_resultado.json", {"fonte": fontes.ENDPOINTS["fund_resultado"], "coletado_em": agora(), **res})
i = res["header"].index("Liq.2meses")
tick = sorted(r[0] for r in res["rows"] if (fontes._num(r[i]) or 0) >= liq_min)
print("fundamentus tickers:", len(tick), flush=True)
por_acao("fund_detalhes.json", tick, fontes.fund_detalhes, False, 0.3, "fichas Fundamentus")
