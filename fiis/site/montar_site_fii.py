"""Gera a página da Peneira FIIs a partir de site/app.html.

Uso:  python site/montar_site_fii.py

Embute motor_fii.js, carteira_fii.js e uma versão enxuta de data/base_fii.json
(só os campos que a página usa) e grava:
  dist_fii/index.html     site estático (carteira no localStorage)
  dist_fii/base_fii.json  base enxuta, para o site real servir por API
O mesmo index.html é publicado como Artifact (carteira no banco do artifact).
Projeto separado: não lê nem escreve nada em screener/.
"""
from __future__ import annotations

import json
import pathlib

RAIZ = pathlib.Path(__file__).resolve().parents[1]
SITE = RAIZ / "site"
DIST = RAIZ / "dist_fii"

CAMPOS = [
    "ticker", "nome", "cnpj", "segmento_cvm", "segmento_fund", "segmento_si", "gestao", "administrador",
    "preco", "data_preco", "liquidez", "cotistas", "cotas", "vp_cota", "patrimonio", "valor_mercado",
    "ref_mensal", "passivo_pl", "taxa_adm_mes_pct", "dy_12m", "fonte_dy", "resultado",
    "vol_1a", "mdd_1a", "saltos_1a", "pregoes_1a", "hist", "eventos", "hist_descartes", "diversificacao",
]


def enxugar(f: dict) -> dict:
    out = {k: f.get(k) for k in CAMPOS}
    c = f.get("composicao")
    if c:
        out["composicao"] = {k: c.get(k) for k in ("imoveis", "papel", "fii", "outros", "caixa", "investido",
                                                    "pct", "pct_desenvolvimento", "passivo_total")}
    else:
        out["composicao"] = None
    im = f.get("imoveis")
    if im:
        out["imoveis"] = {**im, "imoveis": (im.get("imoveis") or [])[:8]}
    else:
        out["imoveis"] = None
    fu = f.get("fund") or {}
    out["fund"] = {k: fu.get(k) for k in ("ffo_12m", "qtd_imoveis")}
    # fundos sem liquidez nenhuma levam só o necessário para a lista de eliminados
    if not (f.get("liquidez") or 0) > 0:
        out["hist"] = {}
        out["imoveis"] = None
        out["diversificacao"] = None
    return out


def arred(o, nd=6):
    if isinstance(o, float):
        return round(o, nd)
    if isinstance(o, list):
        return [arred(x, nd) for x in o]
    if isinstance(o, dict):
        return {k: arred(v, nd) for k, v in o.items()}
    return o


def main():
    base = json.loads((RAIZ / "data" / "base_fii.json").read_text("utf-8"))
    leve = {
        "gerado_em": base["gerado_em"],
        "fontes": base["fontes"],
        "criterios": base["criterios"],
        "grupos": base["grupos"],
        "eventos_fii": base["eventos_fii"],
        "mapeados_por_nome": base.get("mapeados_por_nome", []),
        "macro": base.get("macro"),
        "fundos": [arred(enxugar(f)) for f in base["fundos"]],
    }
    txt = json.dumps(leve, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    html = (SITE / "app.html").read_text("utf-8")
    html = html.replace("__BASE__", txt, 1)
    html = html.replace("/*__MOTOR__*/", (SITE / "motor_fii.js").read_text("utf-8"), 1)
    html = html.replace("/*__CARTEIRA__*/", (SITE / "carteira_fii.js").read_text("utf-8"), 1)
    DIST.mkdir(exist_ok=True)
    (DIST / "index.html").write_text(html, "utf-8")
    (DIST / "base_fii.json").write_text(txt.replace("<\\/", "</"), "utf-8")
    print(f"dist_fii/index.html: {len(html) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
