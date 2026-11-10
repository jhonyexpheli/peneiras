"""Quadro de diferenças entre a base atual e a base montada com as fontes oficiais.

Uso:
    python ferramentas/comparar.py \
        --acoes antes/base.json acoes/data/base.json \
        --fiis antes/base_fii.json fiis/data/base_fii.json \
        --saida relatorios/diferencas.md

Para cada peneira: quanto mudou em cada campo que veio da fonte nova (ativo a ativo), e o que
isso fez com o resultado do método (quem entrou e quem saiu do ranking, o top 20).
O método é rodado pelo próprio motor de cada peneira (ferramentas/rodar_motor.js, em Node).
"""
from __future__ import annotations

import argparse
import json
import pathlib
import statistics
import subprocess

RAIZ = pathlib.Path(__file__).resolve().parents[1]

PROJETOS = {
    "acoes": {
        "nome": "Peneira de Valor (ações)",
        "motor": RAIZ / "acoes" / "site" / "motor.js",
        "lista": "acoes",
        "campos": [("preco", "Preço (R$)", 2), ("liquidez", "Liquidez diária (R$)", 0), ("vol_1a", "Volatilidade 1 ano (%)", 1),
                   ("drawdown_1a", "Maior queda 1 ano (%)", 1), ("valor_mercado", "Valor de mercado (R$)", 0)],
    },
    "fiis": {
        "nome": "Peneira FIIs",
        "motor": RAIZ / "fiis" / "site" / "motor_fii.js",
        "lista": "fundos",
        "campos": [("preco", "Preço (R$)", 2), ("liquidez", "Liquidez diária (R$)", 0), ("vol_1a", "Volatilidade 1 ano (%)", 1),
                   ("mdd_1a", "Maior queda 1 ano (%)", 1), ("dy_12m", "DY 12 meses (%)", 2), ("pvp", "P/VP", 2)],
    },
}


def ok(v):
    return isinstance(v, (int, float)) and v == v


def valor(x, k):
    if k == "pvp":
        return x["preco"] / x["vp_cota"] if ok(x.get("preco")) and ok(x.get("vp_cota")) and x["vp_cota"] else None
    return x.get(k)


def fmt(v, d):
    if not ok(v):
        return "–"
    if abs(v) >= 1e9:
        return f"{v / 1e9:,.2f} bi".replace(",", "X").replace(".", ",").replace("X", ".")
    if abs(v) >= 1e6:
        return f"{v / 1e6:,.1f} mi".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def motor(proj, caminho):
    r = subprocess.run(["node", str(RAIZ / "ferramentas" / "rodar_motor.js"), str(proj["motor"]), str(caminho)],
                       capture_output=True, text=True, check=True)
    return json.loads(r.stdout)


def comparar(chave, antes_p, depois_p):
    proj = PROJETOS[chave]
    antes = {x["ticker"]: x for x in json.loads(pathlib.Path(antes_p).read_text("utf-8"))[proj["lista"]]}
    depois = {x["ticker"]: x for x in json.loads(pathlib.Path(depois_p).read_text("utf-8"))[proj["lista"]]}
    comuns = sorted(set(antes) & set(depois))
    md = [f"## {proj['nome']}", ""]
    md.append(f"Universo: {len(antes)} antes, {len(depois)} depois ({len(comuns)} em comum"
              + (f"; só na base nova: {', '.join(sorted(set(depois) - set(antes))[:15])}" if set(depois) - set(antes) else "")
              + (f"; só na base antiga: {', '.join(sorted(set(antes) - set(depois))[:15])}" if set(antes) - set(depois) else "") + ").")
    md += ["", "### Campos que vieram da fonte nova", "",
           "Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.", "",
           "| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |", "|---|---|---|---|---|"]
    maiores = {}
    for k, rot, d in proj["campos"]:
        difs = []
        for t in comuns:
            a, b = valor(antes[t], k), valor(depois[t], k)
            if ok(a) and ok(b) and a != 0:
                difs.append((abs(b / a - 1) * 100, t, a, b))
        if not difs:
            md.append(f"| {rot} | 0 | – | – | – |")
            continue
        md.append(f"| {rot} | {len(difs)} | {fmt(statistics.median(x[0] for x in difs), 1)}% | "
                  f"{sum(1 for x in difs if x[0] > 5)} | {sum(1 for x in difs if x[0] > 20)} |")
        maiores[rot] = (sorted(difs, reverse=True)[:8], d)

    # Qual janela de liquidez da B3 fica mais perto da fonte antiga (Status Invest ou Fundamentus).
    var = {}
    for t in comuns:
        a = antes[t].get("liquidez")
        for k, v in (depois[t].get("liquidez_variantes") or {}).items():
            if ok(a) and a >= 1e5 and ok(v):
                var.setdefault(k, []).append(v / a - 1)
    if var:
        corte = 1e6 if chave == "acoes" else 5e5
        md += ["", "### Qual medida de liquidez da B3 bate com a fonte antiga", "",
               f"Ativos com liquidez antiga acima de R$ 100 mil. A peneira usa a primeira linha (2 meses, pregões sem negócio contam zero).", "",
               "| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |", "|---|---|---|---|---|"]
        for k, l in var.items():
            md.append(f"| {k.replace('_', ' ')} | {len(l)} | {fmt(statistics.median(l) * 100, 1)}% | "
                      f"{fmt(statistics.median(abs(x) for x in l) * 100, 1)}% | {sum(1 for x in l if abs(x) > 0.1)} |")

    ma, md_ = motor(proj, antes_p), motor(proj, depois_p)
    ia, idp = {x["t"]: x for x in ma["itens"]}, {x["t"]: x for x in md_["itens"]}
    ranq = lambda m: {x["t"] for x in m["itens"] if x["etapa"] == 4}
    ra, rd = ranq(ma), ranq(md_)
    md += ["", "### O que muda no resultado do método", "",
           f"Ranqueados: {ma['ranqueados']} antes, {md_['ranqueados']} depois. "
           f"Entraram {len(rd - ra)}, saíram {len(ra - rd)}, continuaram {len(ra & rd)}.", ""]
    if rd - ra:
        md += ["**Entraram no ranking**", "", "| Ativo | Antes saía por | Posição agora |", "|---|---|---|"]
        for t in sorted(rd - ra, key=lambda t: idp[t]["pos"] or 999):
            mot = "; ".join(ia[t]["motivos"]) if t in ia else "não estava na base"
            md.append(f"| {t} | {mot[:160]} | {idp[t]['pos']}º {('(' + idp[t]['grupo'] + ')') if chave == 'fiis' else ''} |")
        md.append("")
    if ra - rd:
        md += ["**Saíram do ranking**", "", "| Ativo | Posição antes | Motivo agora |", "|---|---|---|"]
        for t in sorted(ra - rd, key=lambda t: ia[t]["pos"] or 999):
            mot = "; ".join(idp[t]["motivos"]) if t in idp else "não está na base nova"
            md.append(f"| {t} | {ia[t]['pos']}º {('(' + ia[t]['grupo'] + ')') if chave == 'fiis' else ''} | {mot[:160]} |")
        md.append("")
    grupos = sorted({x["grupo"] for x in ma["itens"] if x["etapa"] == 4 and x["grupo"]}) if chave == "fiis" else [None]
    for g in grupos:
        top = lambda m: [x["t"] for x in sorted((x for x in m["itens"] if x["etapa"] == 4 and (g is None or x["grupo"] == g)),
                                                  key=lambda x: x["pos"])][:20]
        ta, td = top(ma), top(md_)
        md += [f"**Top {len(ta)}{(' ' + g) if g else ''}**: {len(set(ta) & set(td))} de {len(ta)} continuam.", "",
               "| # | Antes | Depois |", "|---|---|---|"]
        for i in range(max(len(ta), len(td))):
            a = ta[i] if i < len(ta) else ""
            b = td[i] if i < len(td) else ""
            md.append(f"| {i + 1} | {a} | {b}{'' if not b or b in ta else ' (novo)'} |")
        md.append("")
    if maiores:
        md += ["### Maiores diferenças por campo", "", "Para conferir na fonte: o valor antigo, o novo e a variação.", ""]
        for rot, (lst, d) in maiores.items():
            md.append(f"**{rot}**: " + "; ".join(f"{t} {fmt(a, d)} → {fmt(b, d)} ({fmt(b / a * 100 - 100, 0)}%)" for p, t, a, b in lst))
            md.append("")
    return md


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--acoes", nargs=2)
    ap.add_argument("--fiis", nargs=2)
    ap.add_argument("--macro")
    ap.add_argument("--saida", default="relatorios/diferencas.md")
    a = ap.parse_args()
    md = ["# Quadro de diferenças: fontes oficiais × base atual", "",
          "Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.", ""]
    if a.macro and pathlib.Path(a.macro).exists():
        m = json.loads(pathlib.Path(a.macro).read_text("utf-8"))
        md += ["## Indicadores de referência", "", "| Indicador | Valor | Data | Fonte |", "|---|---|---|---|"]
        for k, rot in (("selic_meta", "Selic meta (% a.a.)"), ("cdi", "CDI (% a.a.)"), ("ipca_12m", "IPCA 12 meses (%)"), ("ntnb", "NTN-B, juro real (% a.a.)")):
            v = m.get(k)
            md.append(f"| {rot} | {fmt(v['valor'], 2) if v else '–'} | {v['data'] if v else '–'} | {v['fonte'] if v else m.get('erros', {}).get(k, 'sem dado')} |")
        md.append("")
    for chave in ("acoes", "fiis"):
        par = getattr(a, chave)
        if par:
            try:
                md += comparar(chave, *par)
            except Exception as e:  # um projeto com problema não esconde o outro
                md += [f"## {PROJETOS[chave]['nome']}", "", f"Comparação não concluída: {e}", ""]
    p = pathlib.Path(a.saida)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(md) + "\n", "utf-8")
    print("\n".join(md))


if __name__ == "__main__":
    main()
