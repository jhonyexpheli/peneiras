"""Normaliza os dados crus (data/raw) numa base única para o site (data/base.json).

Não aplica o método: só junta as fontes por ticker, padroniza nomes e unidades,
marca situação na CVM e OPA. O método (4 passos) roda no navegador, em
site/motor.js, para a página poder ajustar os parâmetros ao vivo; o mesmo
arquivo pode rodar em Node num backend futuro.

Uso: python collector/montar_base.py
"""
from __future__ import annotations

import json
import re
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"
CFG = RAIZ / "config"

SITUACAO_CVM = {
    "EM RECUPERAÇÃO JUDICIAL OU EQUIVALENTE": "RJ",
    "EM RECUPERAÇÃO EXTRAJUDICIAL": "REJ",
    "FALIDA": "FAL",
    "LIQUIDAÇÃO EXTRAJUDICIAL": "LE",
    "EM LIQUIDAÇÃO JUDICIAL": "LJ",
}

# Indicadores do histórico do Status Invest que vão para o site.
HIST_KEYS = ["dy", "p_l", "p_vp", "ev_ebit", "ev_ebitda", "lpa", "roe", "roic",
             "dividaliquida_patrimonioliquido", "dividaliquida_ebitda", "dividaliquida_ebit",
             "margembruta", "margemebit", "margemliquida", "receitas_cagr5", "liquidezcorrente"]

STOP = {"SA", "S", "A", "CIA", "COMPANHIA", "DE", "DO", "DA", "DOS", "DAS", "E", "PARTICIPACOES",
        "PART", "HOLDING", "EM", "RECUPERACAO", "JUDICIAL", "EXTRAJUDICIAL", "OU", "EQUIVALENTE",
        "BRASIL", "BRASILEIRA", "GRUPO"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().upper()
    s = re.sub(r" - EM .*$", "", s)
    s = re.sub(r"[^A-Z0-9 ]", " ", s)
    return " ".join(w for w in s.split() if w not in STOP)


def resumo_cotacoes(serie):
    """serie: [[dia_desde_1970, fechamento_ajustado], ...] em ordem.

    Volatilidade = desvio-padrão anualizado dos retornos diários (log). Saltos acima de
    25% num dia são tratados como erro de ajuste/evento societário e ficam fora da conta
    (a quantidade é informada)."""
    import math
    from datetime import date, timedelta

    serie = [s for s in serie if s[1] and s[1] > 0]
    if len(serie) < 30:
        return {}
    d0 = date(1970, 1, 1)
    rets = [math.log(serie[i][1] / serie[i - 1][1]) for i in range(1, len(serie))]

    def vol(rs):
        rs2 = [r for r in rs if abs(r) <= 0.25]
        if len(rs2) < 100:
            return None, 0
        m = sum(rs2) / len(rs2)
        return math.sqrt(sum((r - m) ** 2 for r in rs2) / (len(rs2) - 1)) * math.sqrt(252) * 100, len(rs) - len(rs2)

    v1, s1 = vol(rets[-252:])
    v2, _ = vol(rets[-504:])
    pico, mdd = -1.0, 0.0
    for _, v in serie[-252:]:
        pico = max(pico, v)
        mdd = min(mdd, v / pico - 1)
    mensal = {}
    for dia, v in serie:
        d = d0 + timedelta(days=int(dia))
        mensal[f"{d.year}-{d.month:02d}"] = v
    ks = sorted(mensal)[-121:]
    return {"vol_1a": v1, "vol_2a": v2, "saltos_1a": s1, "max_drawdown_1a": mdd * 100,
            "primeiro_pregao": (d0 + timedelta(days=int(serie[0][0]))).isoformat(),
            "fechamento_mensal": [[k, mensal[k]] for k in ks]}


def ler(nome):
    p = RAW / nome
    return json.loads(p.read_text("utf-8")) if p.exists() else None


def main() -> None:
    # Status Invest pode vir do coletor (servidor) ou do coletor de navegador
    # (site/coletar_navegador.js), que grava tudo num arquivo só.
    nav = ler("statusinvest_navegador.json") or {}
    uni = (ler("si_universo.json") or {}).get("lista") or nav.get("universo", [])
    hist = (ler("si_historico.json") or {}).get("dados") or nav.get("historico", {})
    fund = (ler("fund_detalhes.json") or {}).get("dados", {})
    precos = (ler("precos.json") or {}).get("dados") or nav.get("precos", {})
    # Cotações ajustadas do Fundamentus (preferidas): recalcula volatilidade aqui.
    cot = (ler("cotacoes_fundamentus.json") or {}).get("dados")
    if cot:
        precos = {t: resumo_cotacoes(s) for t, s in cot.items() if s}
    cvm = (ler("cvm_cadastro.json") or {}).get("linhas", [])
    opa = json.loads((CFG / "opa.json").read_text("utf-8"))
    mapa_manual = json.loads((CFG / "cvm_tickers.json").read_text("utf-8")) if (CFG / "cvm_tickers.json").exists() else {}

    # Situação especial na CVM, casada pelo nome da companhia.
    especiais = []
    for row in cvm:
        cod = SITUACAO_CVM.get(row.get("SIT_EMISSOR", ""))
        if cod:
            especiais.append({"cod": cod, "desde": row.get("DT_INI_SIT_EMISSOR"), "nome": row["DENOM_SOCIAL"],
                              "cnpj": row["CNPJ_CIA"], "chave": norm(row["DENOM_SOCIAL"])})

    def situacao(ticker: str, nome_si: str):
        if ticker in mapa_manual:
            alvo = mapa_manual[ticker]
            for e in especiais:
                if e["cnpj"] == alvo:
                    return e
            return None
        # Casa por palavras inteiras: uma lista de palavras precisa ser prefixo da outra
        # (evita "LITEL" casar com "LITELA").
        k = norm(nome_si).split()
        for e in especiais:
            a = e["chave"].split()
            n = min(len(a), len(k))
            if n and a[:n] == k[:n]:
                return e
        return None

    opa_por_ticker = {}
    for it in opa["itens"]:
        if it.get("status") == "pendente":
            for t in it["tickers"]:
                opa_por_ticker[t] = {k: it.get(k) for k in ("empresa", "tipo", "obs", "fonte")}

    registros = []
    for x in uni:
        t = x["ticker"]
        f = fund.get(t) or {}
        bal, dre, info = f.get("balanco", {}), f.get("dre", {}), f.get("info", {})
        num = lambda s: None if s in (None, "", "-") else float(str(s).replace(".", "").replace(",", "."))
        h = hist.get(t) or {}
        hcomp = {}
        for k in HIST_KEYS:
            serie = h.get(k) or []
            hcomp[k] = [[int(a), int(tp), v] for a, tp, v in serie if v is not None]
        p = precos.get(t) or {}
        sit = situacao(t, x.get("companyname", ""))
        lucro = dre.get("Lucro Líquido") or [None, None]
        ebit = dre.get("EBIT") or [None, None]
        receita = dre.get("Receita Líquida") or [None, None]
        reg = {
            "ticker": t,
            "empresa": x.get("companyname"),
            "empresa_id": x.get("companyid"),
            "setor": x.get("sectorname"),
            "subsetor": x.get("subsectorname"),
            "segmento": x.get("segmentname"),
            "preco": x.get("price"),
            "liquidez": x.get("liquidezmediadiaria"),
            "valor_mercado": num(info.get("Valor de mercado")) or x.get("valormercado"),
            "valor_firma": num(info.get("Valor da firma")),
            "caixa": bal.get("Disponibilidades"),
            "divida_bruta": bal.get("Dív. Bruta"),
            "divida_liquida": bal.get("Dív. Líquida"),
            "patrimonio": bal.get("Patrim. Líq"),
            "ativo": bal.get("Ativo"),
            "receita_12m": receita[0], "receita_3m": receita[1],
            "ebit_12m": ebit[0], "ebit_3m": ebit[1],
            "lucro_12m": lucro[0], "lucro_3m": lucro[1],
            "ultimo_balanco": info.get("Últ balanço processado"),
            "data_cotacao": info.get("Data últ cot"),
            "ind": {k: x.get(k) for k in ("dy", "p_l", "p_vp", "ev_ebit", "roe", "roic", "margemebit",
                                            "margemliquida", "margembruta", "dividaliquidaebit",
                                            "dividaliquidapatrimonioliquido", "liquidezcorrente",
                                            "receitas_cagr5", "lpa", "vpa")},
            "vol_1a": p.get("vol_1a"), "vol_2a": p.get("vol_2a"), "saltos_1a": p.get("saltos_1a"),
            "drawdown_1a": p.get("max_drawdown_1a", p.get("drawdown_1a")),
            "primeiro_pregao": p.get("primeiro_pregao", p.get("primeiro")),
            "mensal": p.get("fechamento_mensal", p.get("mensal")),
            "oscilacoes": f.get("oscilacoes"),
            "cvm": sit and {k: sit[k] for k in ("cod", "desde", "nome", "cnpj")},
            "opa": opa_por_ticker.get(t),
            "hist": hcomp if h else None,
            "tem_ficha": bool(f), "tem_hist": bool(h),
        }
        registros.append(reg)

    meta = {
        "gerado_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fontes": {
            "universo": (ler("si_universo.json") or {}).get("coletado_em") or nav.get("coletado_em"),
            "historico": (ler("si_historico.json") or {}).get("coletado_em") or nav.get("coletado_em"),
            "fichas": (ler("fund_detalhes.json") or {}).get("coletado_em"),
            "precos": (ler("cotacoes_fundamentus.json") or {}).get("coletado_em") or (ler("precos.json") or {}).get("coletado_em") or nav.get("coletado_em"),
            "precos_fonte": "Fundamentus, fechamento ajustado" if cot else "Status Invest, sem ajuste de proventos",
            "cvm": (ler("cvm_cadastro.json") or {}).get("coletado_em"),
            "opa": opa.get("atualizado_em"),
        },
        "cvm_especiais": [{k: e[k] for k in ("cod", "desde", "nome", "cnpj")} for e in especiais],
        "opa": opa["itens"],
    }
    out = {"meta": meta,
           "criterios": json.loads((CFG / "criterios.json").read_text("utf-8")),
           "setores": json.loads((CFG / "setores.json").read_text("utf-8")),
           "acoes": registros}
    (RAIZ / "data" / "base.json").write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), "utf-8")
    com = sum(1 for r in registros if r["tem_ficha"])
    print(f"base.json: {len(registros)} ações, {com} com ficha, {sum(1 for r in registros if r['cvm'])} com situação especial na CVM")


if __name__ == "__main__":
    main()
