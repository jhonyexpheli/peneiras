"""Junta as fontes por ticker e grava data/base_fii.json (sem aplicar o método).

Entradas em data/raw/:
  cvm/inf_mensal_fii_AAAA.zip, cvm/inf_trimestral_fii_AAAA.zip   (coletar_direto_fii.py)
  fundamentus_fii_resultado.json, fundamentus_fii_detalhes.json  (coletar_direto_fii.py)
  statusinvest_fii.json, yahoo_fii.json                          (coletar_navegador_fii.js)
Configuração: config/criterios_fii.json, config/grupos_fii.json, config/eventos_fii.json.

Cada fundo leva a data de referência e a fonte de cada bloco, para conferência.
"""
from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import fontes_fii as F  # noqa: E402

RAIZ = pathlib.Path(__file__).resolve().parents[1]
RAW = RAIZ / "data" / "raw"
CFG = RAIZ / "config"


def f(x):
    try:
        v = float(x)
        return v if v == v else None
    except (TypeError, ValueError):
        return None


def ler_json(nome, padrao=None):
    p = RAW / nome
    return json.loads(p.read_text("utf-8")) if p.exists() else padrao


# ---------------------------------------------------------------- CVM mensal

def cvm_mensal():
    """Por CNPJ: registros mensais (geral + complemento + ativo/passivo), última versão de cada mês."""
    por = defaultdict(dict)  # cnpj -> {data: registro}
    for z in sorted((RAW / "cvm").glob("inf_mensal_fii_*.zip")):
        b = z.read_bytes()
        for pref, chave in (("inf_mensal_fii_geral", "g"), ("inf_mensal_fii_complemento", "c"), ("inf_mensal_fii_ativo_passivo", "a")):
            for r in F.cvm_tabelas(b, pref):
                d = r["Data_Referencia"]
                reg = por[r["cnpj"]].setdefault(d, {})
                v = int(r.get("Versao") or 1)
                if reg.get("_v_" + chave, 0) <= v:
                    reg["_v_" + chave] = v
                    reg[chave] = r
    return por


GRUPOS_ATIVO = {
    "imoveis": ["Direitos_Bens_Imoveis", "Terrenos", "Imoveis_Renda_Acabados", "Imoveis_Renda_Construcao",
                "Imoveis_Venda_Acabados", "Imoveis_Venda_Construcao", "Outros_Direitos_Reais",
                "Acoes_Sociedades_Atividades_FII", "Cotas_Sociedades_Atividades_FII"],
    "papel": ["CRI", "CRI_CRA", "LCI", "LCI_LCA", "LIG", "Letras_Hipotecarias"],
    "fii": ["FII"],
    "outros": ["Acoes", "Debentures", "Bonus_Subscricao", "Certificados_Deposito_Valores_Mobiliarios",
               "Cedulas_Debentures", "Fundo_Acoes", "FIP", "FDIC", "Outras_Cotas_FI", "Notas_Promissorias",
               "CEPAC", "Outros_Valores_Mobliarios"],
    "caixa": ["Disponibilidades", "Titulos_Publicos", "Titulos_Privados", "Fundos_Renda_Fixa"],
}
DESENVOLVIMENTO = ["Imoveis_Renda_Construcao", "Imoveis_Venda_Construcao", "Imoveis_Venda_Acabados", "Terrenos"]


def composicao(a):
    if not a:
        return None
    soma = {k: sum(f(a.get(c)) or 0 for c in cols) for k, cols in GRUPOS_ATIVO.items()}
    investido = soma["imoveis"] + soma["papel"] + soma["fii"] + soma["outros"]
    dev = sum(f(a.get(c)) or 0 for c in DESENVOLVIMENTO)
    return {
        **{k: round(v, 2) for k, v in soma.items()},
        "investido": round(investido, 2),
        "desenvolvimento": round(dev, 2),
        "pct": {k: (soma[k] / investido if investido > 0 else None) for k in ("imoveis", "papel", "fii", "outros")},
        "pct_desenvolvimento": dev / investido if investido > 0 else None,
        "passivo_total": f(a.get("Total_Passivo")),
        "obrig_aquisicao": f(a.get("Obrigacoes_Aquisicao_Imoveis")),
        "obrig_securitizacao": f(a.get("Obrigacoes_Securitizacao_Recebiveis")),
    }


# ---------------------------------------------------------------- CVM trimestral

def ultima_versao(linhas, destino):
    """Guarda em destino[cnpj][data] as linhas da última versão de cada informe."""
    versoes = defaultdict(int)
    for r in linhas:
        k = (r["cnpj"], r["Data_Referencia"])
        versoes[k] = max(versoes[k], int(r.get("Versao") or 1))
    novos = set()
    for r in linhas:
        k = (r["cnpj"], r["Data_Referencia"])
        if int(r.get("Versao") or 1) == versoes[k]:
            if k not in novos:
                destino[k[0]][k[1]] = []
                novos.add(k)
            destino[k[0]][k[1]].append(r)


def cvm_trimestral():
    res = defaultdict(dict)   # cnpj -> {data: registro de resultado}
    imov = defaultdict(lambda: defaultdict(list))  # cnpj -> data -> [imóveis]
    ativos = defaultdict(dict)   # cnpj -> data -> [ativos financeiros: CRI, FII, ações de SPE...]
    inquil = defaultdict(dict)   # cnpj -> data -> [inquilinos por setor]
    for z in sorted((RAW / "cvm").glob("inf_trimestral_fii_*.zip")):
        b = z.read_bytes()
        ultima_versao(F.cvm_tabelas(b, "inf_trimestral_fii_ativo"), ativos)
        ultima_versao(F.cvm_tabelas(b, "inf_trimestral_fii_imovel_renda_acabado_inquilino"), inquil)
        for r in F.cvm_tabelas(b, "inf_trimestral_fii_resultado_contabil_financeiro"):
            d = r["Data_Referencia"]
            v = int(r.get("Versao") or 1)
            if res[r["cnpj"]].get(d, {}).get("_v", 0) <= v:
                r["_v"] = v
                res[r["cnpj"]][d] = r
        versoes = defaultdict(int)
        linhas = F.cvm_tabelas(b, "inf_trimestral_fii_imovel")
        for r in linhas:
            k = (r["cnpj"], r["Data_Referencia"])
            versoes[k] = max(versoes[k], int(r.get("Versao") or 1))
        for r in linhas:
            k = (r["cnpj"], r["Data_Referencia"])
            if int(r.get("Versao") or 1) == versoes[k]:
                imov[r["cnpj"]][r["Data_Referencia"]].append(r)
    return res, imov, ativos, inquil


def trimestre(d):
    """'2026-06-30' -> (2026, 2). Datas fora do fim de trimestre (ex.: 2026-03-30) vão para o trimestre do mês."""
    a, m = int(d[:4]), int(d[5:7])
    return a, (m - 1) // 3 + 1


def resultado_12m(regs: dict):
    """Resultado caixa, aluguel e rendimentos declarados nos 12 meses (dois semestres fechados).

    O informe trimestral traz o resultado de cada trimestre (Resultado_Trimestral_Liquido_Financeiro),
    o acumulado do semestre e os rendimentos declarados acumulados no semestre
    (no 2º e no 4º trimestres somam o trimestre anterior).
    """
    if not regs:
        return None
    q = {}
    for d, r in regs.items():
        q[trimestre(d)] = (d, r)
    chaves = sorted(q)
    semestrais = [k for k in chaves if k[1] in (2, 4)]
    if len(semestrais) < 2:
        return {"ref": q[chaves[-1]][0], "incompleto": True, "trimestres": len(chaves)}
    s2 = semestrais[-1]
    s1 = semestrais[-2]
    # os 4 trimestres cobertos
    alvo = []
    a, t = s2
    for _ in range(4):
        alvo.append((a, t))
        t -= 1
        if t == 0:
            a, t = a - 1, 4
    tem = [k for k in alvo if k in q]
    resultado = sum(f(q[s][1].get("Resultado_Financeiro_Liquido_Acumulado")) or 0 for s in (s1, s2))
    declarado = sum(f(q[s][1].get("Rendimentos_Declarados")) or 0 for s in (s1, s2))
    aluguel = sum(f(q[k][1].get("Receita_Aluguel_Investimento_Financeiro")) or 0 for k in tem)
    venda = sum((f(q[k][1].get("Receita_Venda_Investimento_Financeiro")) or 0) + (f(q[k][1].get("Custo_Investimento_Financeiro")) or 0) for k in tem)
    if len(tem) < 4 and tem:
        aluguel *= 4 / len(tem)
    ultimo = q[chaves[-1]]
    return {
        "ref": q[s2][0],
        "periodo": f"{alvo[-1][1]}T{alvo[-1][0]} a {s2[1]}T{s2[0]}",
        "resultado_12m": resultado,
        "declarado_12m": declarado,
        "payout": (declarado / resultado) if resultado > 0 else None,
        "aluguel_12m": aluguel,
        "ganho_venda_imoveis_12m": venda,
        "trimestres_aluguel": len(tem),
        "resultado_ult_tri": f(ultimo[1].get("Resultado_Trimestral_Liquido_Financeiro")),
        "ref_ult_tri": ultimo[0],
    }


def imoveis_resumo(por_data: dict):
    if not por_data:
        return None
    d = max(por_data)
    lst = [r for r in por_data[d] if "renda acabados" in (r.get("Classe") or "").lower()]
    if not lst:
        return {"ref": d, "n_renda": 0}
    area = [(f(r.get("Area")) or 0, f(r.get("Percentual_Vacancia")) or 0) for r in lst]
    a_tot = sum(x for x, _ in area)
    vac = (sum(x * v for x, v in area) / a_tot) if a_tot > 0 else sum(v for _, v in area) / len(area)
    rec = [(f(r.get("Percentual_Receitas_FII")) or 0, f(r.get("Percentual_Inadimplencia")) or 0) for r in lst]
    r_tot = sum(x for x, _ in rec)
    inad = (sum(x * v for x, v in rec) / r_tot) if r_tot > 0 else None
    maior = max((x for x, _ in rec), default=None)
    return {
        "ref": d,
        "n_renda": len(lst),
        "area_total": a_tot,
        "vacancia_fisica": vac * 100,
        "inadimplencia": inad * 100 if inad is not None else None,
        "maior_receita_pct": (maior / r_tot * 100) if (maior and r_tot) else None,
        "imoveis": sorted(
            [{"nome": (r.get("Nome_Imovel") or "")[:60], "area": f(r.get("Area")), "vac": (f(r.get("Percentual_Vacancia")) or 0) * 100,
              "receita": (f(r.get("Percentual_Receitas_FII")) or 0) * 100} for r in lst],
            key=lambda x: -(x["receita"] or 0))[:12],
    }


# ---------------------------------------------------------------- diversificação

UFS = "AC AL AP AM BA CE DF ES GO MA MT MS MG PA PB PR PE PI RJ RN RS RO RR SC SP SE TO".split()
_RE_UF = re.compile(r"(?<![A-Za-z])(" + "|".join(UFS) + r")(?![A-Za-z])")
CIDADES_UF = {
    "SAO PAULO": "SP", "BARUERI": "SP", "CAJAMAR": "SP", "GUARULHOS": "SP", "JUNDIAI": "SP", "CAMPINAS": "SP",
    "SANTANA DE PARNAIBA": "SP", "OSASCO": "SP", "EMBU": "SP", "ITUPEVA": "SP", "LOUVEIRA": "SP", "HORTOLANDIA": "SP",
    "SOROCABA": "SP", "RIBEIRAO PRETO": "SP", "SAO JOSE DOS CAMPOS": "SP", "SANTO ANDRE": "SP", "SAO BERNARDO": "SP",
    "ALPHAVILLE": "SP", "TAMBORE": "SP", "PAULINIA": "SP", "VALINHOS": "SP", "VINHEDO": "SP", "INDAIATUBA": "SP",
    "RIO DE JANEIRO": "RJ", "DUQUE DE CAXIAS": "RJ", "NITEROI": "RJ", "BARRA DA TIJUCA": "RJ",
    "BELO HORIZONTE": "MG", "BETIM": "MG", "CONTAGEM": "MG", "EXTREMA": "MG", "UBERLANDIA": "MG",
    "CURITIBA": "PR", "LONDRINA": "PR", "MARINGA": "PR", "PORTO ALEGRE": "RS", "CANOAS": "RS", "CAXIAS DO SUL": "RS",
    "FLORIANOPOLIS": "SC", "JOINVILLE": "SC", "BLUMENAU": "SC", "ITAJAI": "SC", "SALVADOR": "BA", "CAMACARI": "BA",
    "RECIFE": "PE", "JABOATAO": "PE", "CABO DE SANTO AGOSTINHO": "PE", "FORTALEZA": "CE", "BRASILIA": "DF",
    "GOIANIA": "GO", "MANAUS": "AM", "BELEM": "PA", "MACEIO": "AL", "NATAL": "RN", "JOAO PESSOA": "PB",
    "TERESINA": "PI", "SAO LUIS": "MA", "CUIABA": "MT", "CAMPO GRANDE": "MS", "VITORIA": "ES", "SERRA": "ES",
    "ARACAJU": "SE", "PALMAS": "TO",
}


def uf_de(endereco: str):
    import unicodedata
    e = endereco or ""
    achados = _RE_UF.findall(e)
    if achados:
        return achados[-1]
    n = unicodedata.normalize("NFKD", e).encode("ascii", "ignore").decode().upper()
    for cid, uf in CIDADES_UF.items():
        if cid in n:
            return uf
    return None


def fatias(pares, n_max=8):
    """[(nome, valor)] -> fatias em % do total, as n_max maiores e o resto em 'Outros'."""
    tot = sum(v for _, v in pares if v and v > 0)
    if tot <= 0:
        return [], 0
    ordem = sorted([(n, v) for n, v in pares if v and v > 0], key=lambda x: -x[1])
    sai = [{"nome": n, "pct": round(v / tot * 100, 3)} for n, v in ordem[:n_max]]
    resto = ordem[n_max:]
    if resto:
        sai.append({"nome": f"Outros ({len(resto)})", "pct": round(sum(v for _, v in resto) / tot * 100, 3), "outros": True})
    return sai, tot


def concentracao(valores):
    tot = sum(v for v in valores if v > 0)
    if tot <= 0:
        return None
    w = sorted((v / tot for v in valores if v > 0), reverse=True)
    hhi = sum(x * x for x in w)
    return {"n": len(w), "efetivo": round(1 / hhi, 2), "maior_pct": round(w[0] * 100, 2), "top3_pct": round(sum(w[:3]) * 100, 2), "hhi": round(hhi, 4)}


def rotulo_ativo(r):
    emis = (r.get("Emissor") or r.get("Nome_Ativo") or "").strip()
    tipo = r.get("Tipo") or ""
    m = re.match(r"^([A-Z]{4}1[1-3])\s*-", emis)
    if m:  # cota de FII: 'PNDL11 - PANORAMA ...'
        return m.group(1)
    m = re.search(r"\bCR[IA]\s*-\s*([0-9A-Z]{8,12})", emis)
    if m:  # CRI: 'TRUE SECURITIZADORA S.A. - CRI - 19E0322333'
        sec = emis.split(" ")[0].title()
        return f"CRI {m.group(1)} ({sec})" + (" compromissada" if "COMPROMISS" in emis.upper() else "")
    nome = (r.get("Nome_Ativo") or emis or tipo)[:48]
    return nome


def diversificacao(imov_por_data: dict, ativos_por_data: dict, inquil_por_data: dict):
    """Fatias para a pizza e medidas de concentração (informe trimestral mais recente)."""
    out = {}
    if imov_por_data:
        d = max(imov_por_data)
        lst = [r for r in imov_por_data[d] if "renda acabados" in (r.get("Classe") or "").lower()]
        if lst:
            rec = [((r.get("Nome_Imovel") or "?").strip()[:48], f(r.get("Percentual_Receitas_FII")) or 0) for r in lst]
            area = [((r.get("Nome_Imovel") or "?").strip()[:48], f(r.get("Area")) or 0) for r in lst]
            vagas = [((r.get("Nome_Imovel") or "?").strip()[:48], (f(r.get("Area")) or 0) * (f(r.get("Percentual_Vacancia")) or 0)) for r in lst]
            fr, _ = fatias(rec)
            fa, a_tot = fatias(area)
            fv, vaga_tot = fatias(vagas, 8)
            com_vaga = sum(1 for _, v in vagas if v > 0)
            leitura = None
            if a_tot > 0:
                pv = vaga_tot / a_tot * 100
                if pv < 1:
                    leitura = "sem vacância relevante"
                elif fv and fv[0]["pct"] >= 60:
                    leitura = f"concentrada: {fv[0]['nome']} responde por {fv[0]['pct']:.0f}% da área vaga"
                elif fv and fv[0]["pct"] >= 35:
                    leitura = f"parcialmente concentrada: {fv[0]['nome']} responde por {fv[0]['pct']:.0f}% da área vaga, o resto em {com_vaga - 1} {'imóvel' if com_vaga == 2 else 'imóveis'}"
                else:
                    leitura = f"pulverizada: área vaga espalhada por {com_vaga} imóveis"
            ufs = defaultdict(float)
            for r in lst:
                ufs[uf_de(r.get("Endereco")) or "Não identificado"] += f(r.get("Percentual_Receitas_FII")) or 0
            fu, u_tot = fatias(list(ufs.items()), 8)
            ident = sum(v for k, v in ufs.items() if k != "Não identificado")
            out["imoveis"] = {
                "ref": d, "receita": fr, "area": fa, "area_vaga": fv,
                "conc_receita": concentracao([v for _, v in rec]), "conc_area": concentracao([v for _, v in area]),
                "vaga_m2": round(vaga_tot, 1), "area_m2": round(a_tot, 1), "imoveis_com_vaga": com_vaga, "leitura_vacancia": leitura,
                "uf": fu if u_tot > 0 and ident / u_tot >= 0.7 else None,
            }
    if inquil_por_data:
        d = max(inquil_por_data)
        import unicodedata
        setores, nomes = defaultdict(float), {}
        for r in inquil_por_data[d]:
            s = " ".join((r.get("Setor_Atuacao") or "").split()).capitalize() or "Não informado"
            k = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()
            nomes.setdefault(k, s)
            setores[k] += f(r.get("Percentual_Receitas_FII")) or 0
        setores = defaultdict(float, {nomes[k]: v for k, v in setores.items()})
        fs, tot = fatias(list(setores.items()), 8)
        if tot > 0:
            out["setores"] = {"ref": d, "fatias": fs, "conc": concentracao(list(setores.values()))}
    if ativos_por_data:
        d = max(ativos_por_data)
        lst = [r for r in ativos_por_data[d] if (f(r.get("Valor")) or 0) > 0]
        papel = [(rotulo_ativo(r), f(r.get("Valor"))) for r in lst if "CRI" in (r.get("Tipo") or "").upper() or "LCI" in (r.get("Tipo") or "").upper() or "LIG" in (r.get("Tipo") or "").upper()]
        fii = [(rotulo_ativo(r), f(r.get("Valor"))) for r in lst if (r.get("Tipo") or "").strip().upper() == "FII"]
        for chave, pares in (("cri", papel), ("fii", fii)):
            if pares:
                # mesmo ativo em várias linhas (séries, compromissadas): soma pelo rótulo
                ag = defaultdict(float)
                for n, v in pares:
                    ag[n] += v
                fz, tot = fatias(list(ag.items()))
                out[chave] = {"ref": d, "fatias": fz, "total": round(tot, 2), "conc": concentracao(list(ag.values()))}
    return out or None


# ---------------------------------------------------------------- desdobramentos

def eventos_cotas(meses: list):
    """Desdobramento/grupamento: cotas multiplicam por ~k e o VP divide por ~k no mesmo mês."""
    ev = []
    for (d0, c0, v0), (d1, c1, v1) in zip(meses, meses[1:]):
        if not (c0 and c1 and v0 and v1):
            continue
        rc, rv = c1 / c0, v1 / v0
        for k in (rc, 1 / rc):
            if k >= 1.9 and abs(rc * rv - 1) < 0.12:
                ev.append({"data": d1, "fator": round(rc, 4)})
                break
    return ev


def fator_ate(data, eventos):
    """Fator para trazer um valor por cota de antes dos eventos para a base de cotas atual."""
    fat = 1.0
    for e in eventos:
        if data < e["data"]:
            fat /= e["fator"]
    return fat


# ---------------------------------------------------------------- cotações (Yahoo, pelo navegador)

def ler_yahoo():
    """data/raw/yahoo_fii.txt (formato compacto) -> {ticker: {...}}."""
    p = RAW / "yahoo_fii.txt"
    out = {}
    if not p.exists():
        return out
    for linha in p.read_text("utf-8").splitlines():
        if not linha or linha.startswith("#"):
            continue
        c = linha.split(";")
        anos = c[8].split("|")
        out[c[0]] = {
            "prim": c[1] or None,
            "ult": [c[2], f(c[3])] if c[2] else None,
            "vol": f(c[4]),
            "mdd": f(c[5]),
            "saltos": int(c[6] or 0),
            "n": int(c[7] or 0),
            "ye": {2016 + i: f(v) for i, v in enumerate(anos)},
        }
    return out


# ---------------------------------------------------------------- montagem

def isin_para_ticker(isin: str):
    m = re.match(r"^BR([A-Z]{4})CTF", isin or "")
    return m.group(1) + "11" if m else None


def norm_nome(s):
    """Nome do fundo sem acento, pontuação e termos padrão, para casar Fundamentus x CVM."""
    import unicodedata
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().upper()
    s = " ".join(re.sub(r"[^A-Z0-9 ]", " ", s).split())
    for termo in ("FUNDO DE INVESTIMENTO IMOBILIARIO", "FUNDO DE INVESTIMENTO", "RESPONSABILIDADE LIMITADA",
                  "FII", " RL", " FI ", "IMOBILIARIO", "CLASSE UNICA", "DE COTAS"):
        s = s.replace(termo, " ")
    return " ".join(s.split())


def dbr(s):
    """'30/10/2026' -> '2026-10-30'."""
    try:
        return dt.datetime.strptime(s, "%d/%m/%Y").date().isoformat()
    except (TypeError, ValueError):
        return None


def main():
    criterios = json.loads((CFG / "criterios_fii.json").read_text("utf-8"))
    grupos = json.loads((CFG / "grupos_fii.json").read_text("utf-8"))
    eventos = json.loads((CFG / "eventos_fii.json").read_text("utf-8"))

    fund_tab = {x["ticker"]: x for x in ler_json("fundamentus_fii_resultado.json", [])}
    fund_det = ler_json("fundamentus_fii_detalhes.json", {})
    si = ler_json("statusinvest_fii.json", {"universo": [], "proventos": {}})
    si_u = {x["ticker"]: x for x in si.get("universo", [])}
    yh = ler_yahoo()

    print("lendo CVM mensal...")
    mensal = cvm_mensal()
    print("lendo CVM trimestral...")
    res_tri, imov_tri, ativos_tri, inquil_tri = cvm_trimestral()

    # ticker -> cnpj pelo ISIN do informe mensal mais recente de cada CNPJ
    mapa = {}
    for cnpj, regs in mensal.items():
        ult = max(regs)
        g = regs[ult].get("g") or {}
        t = isin_para_ticker(g.get("Codigo_ISIN"))
        if t and (t not in mapa or ult > mapa[t][1]):
            mapa[t] = (cnpj, ult)

    # ISIN no formato novo (ex.: BR0EBICTF008) não traz o ticker: casa pelo nome do fundo
    import difflib
    nomes_cvm = {}
    for cnpj, regs in mensal.items():
        ult = max(regs)
        if ult < "2026-01-01":
            continue
        g = regs[ult].get("g") or {}
        nomes_cvm[norm_nome(g.get("Nome_Fundo_Classe"))] = cnpj
    lista_nomes = list(nomes_cvm)
    por_nome = []
    for t, d in fund_det.items():
        if t in mapa or not isinstance(d, dict) or not d.get("nome"):
            continue
        n = norm_nome(d["nome"])
        if n in nomes_cvm:
            mapa[t] = (nomes_cvm[n], "nome")
            por_nome.append(t)
            continue
        m = difflib.get_close_matches(n, lista_nomes, n=1, cutoff=0.92)
        if m:
            mapa[t] = (nomes_cvm[m[0]], "nome aproximado")
            por_nome.append(t)

    # Ticker renomeado (o ISIN guarda o código antigo, ex.: CVBI -> PCIP) e nome abreviado na CVM:
    # casa pelo número de cotas e pelo PL informados ao Fundamentus.
    cotas_cvm = []
    for cnpj, regs in mensal.items():
        com_c = [d for d in regs if regs[d].get("c")]
        if not com_c or max(com_c) < "2026-06-01":
            continue
        cc = regs[max(com_c)]["c"]
        cotas_cvm.append((cnpj, f(cc.get("Cotas_Emitidas")), f(cc.get("Patrimonio_Liquido"))))
    usados = {v[0] for v in mapa.values()}
    for t, d in fund_det.items():
        if t in mapa or not isinstance(d, dict) or not d.get("cotas"):
            continue
        cand = [cn for cn, c, pl in cotas_cvm if c and abs(c / d["cotas"] - 1) < 0.0005
                and (not d.get("patrimonio") or not pl or abs(pl / d["patrimonio"] - 1) < 0.05)]
        if len(cand) == 1:
            mapa[t] = (cand[0], "cotas e PL")
            por_nome.append(t)
            if cand[0] in usados:
                print("aviso: CNPJ já usado por outro ticker", t, cand[0])

    hoje = dt.date.today()
    tickers = sorted(set(fund_tab) | set(si_u))
    fundos = []
    sem_cvm = []
    for t in tickers:
        ft = fund_tab.get(t, {})
        fd = fund_det.get(t, {}) if isinstance(fund_det.get(t), dict) else {}
        s = si_u.get(t, {})
        y = yh.get(t, {}) if isinstance(yh.get(t), dict) else {}
        cnpj = mapa.get(t, (None,))[0]
        regs = mensal.get(cnpj, {}) if cnpj else {}
        liq = ft.get("liquidez") if ft.get("liquidez") is not None else s.get("liquidezmediadiaria")

        # série mensal (data, cotas, VP) para achar desdobramentos
        serie_m = []
        for d in sorted(regs):
            c = regs[d].get("c") or {}
            serie_m.append((d, f(c.get("Cotas_Emitidas")), f(c.get("Valor_Patrimonial_Cotas"))))
        ev_cotas = eventos_cotas(serie_m)

        ult_d = max(regs) if regs else None
        ult = regs.get(ult_d, {}) if ult_d else {}
        g, c, a = ult.get("g") or {}, ult.get("c") or {}, ult.get("a") or {}

        preco = ft.get("cotacao") or s.get("price") or (y.get("ult") or [None, None])[1]
        cotas = f(c.get("Cotas_Emitidas")) or fd.get("cotas") or s.get("numerocotas")
        vp_cota = f(c.get("Valor_Patrimonial_Cotas")) or fd.get("vp_cota") or s.get("valorpatrimonialcota")
        pl = f(c.get("Patrimonio_Liquido")) or fd.get("patrimonio") or s.get("patrimonio")
        vm = (preco * cotas) if (preco and cotas) else ft.get("valor_mercado")
        comp = composicao(a)

        # rendimentos (CVM): DY do mês sobre o VP. Somar o DY sobre o VP de 12 meses e dividir pelo
        # P/VP dá o DY sobre o preço, sem misturar unidades quando há desdobramento no meio do caminho.
        dy_vp = []  # [(aaaa-mm, dy sobre VP em fração, rendimento por cota no mês)]
        for d in sorted(regs):
            cc = regs[d].get("c") or {}
            x = f(cc.get("Percentual_Dividend_Yield_Mes"))
            vpm = f(cc.get("Valor_Patrimonial_Cotas"))
            if x is None:
                continue
            if x > 0.2:  # alguns administradores informam em % e não em fração
                x = x / 100
            dy_vp.append((d[:7], x, x * vpm if vpm else None))
        ult12 = dy_vp[-12:] if dy_vp else []
        dyvp_12m = sum(x for _, x, _ in ult12) if len(ult12) == 12 else None
        rend_12m = sum(r for _, _, r in ult12 if r) if len(ult12) == 12 else None
        meses_rend = sum(1 for _, x, _ in ult12 if x > 0)

        # resultado e imóveis (CVM trimestral)
        r12 = resultado_12m(res_tri.get(cnpj, {})) if cnpj else None
        im = imoveis_resumo(imov_tri.get(cnpj, {})) if cnpj else None
        div = diversificacao(imov_tri.get(cnpj, {}), ativos_tri.get(cnpj, {}), inquil_tri.get(cnpj, {})) if cnpj else None

        # histórico anual: P/VP e DY de dezembro de cada ano + atual (VP contemporâneo ao preço)
        hist_pvp, hist_dy, hist_vp, descartes = [], [], [], []
        ye = y.get("ye") or {}
        anterior = None
        for ano in sorted(ye):
            px = ye[ano]
            if px is None:
                continue
            if anterior is not None and px == anterior:
                descartes.append(f"{ano}: fechamento repetido do ano anterior (provável falta de negócio na fonte)")
                anterior = px
                continue
            anterior = px
            dez = f"{ano}-12-01"
            vp = f(((regs.get(dez) or {}).get("c") or {}).get("Valor_Patrimonial_Cotas"))
            if not vp:
                continue
            pvp = px / vp
            if not (0.2 <= pvp <= 3):
                descartes.append(f"{ano}: P/VP {pvp:.2f} fora da faixa (provável desdobramento não refletido na cotação)")
                continue
            hist_vp.append([ano, 0, round(vp, 4)])
            hist_pvp.append([ano, 0, round(pvp, 4)])
            meses_ano = [x for m, x, _ in dy_vp if m[:4] == str(ano)]
            if len(meses_ano) == 12 and min(meses_ano) >= 0:
                hist_dy.append([ano, 0, round(sum(meses_ano) / pvp * 100, 4)])
        pvp_atual = (preco / vp_cota) if (preco and vp_cota) else None
        if pvp_atual:
            hist_pvp.append([hoje.year, 1, round(pvp_atual, 4)])
            hist_vp.append([hoje.year, 1, round(vp_cota, 4)])
        dy_cvm = (dyvp_12m / pvp_atual * 100) if (dyvp_12m is not None and pvp_atual) else None
        # DY atual: rendimento por cota de 12m do Fundamentus (data com) sobre o preço; CVM como reserva.
        dy_fund = (fd["dividendo_cota"] / preco * 100) if (fd.get("dividendo_cota") and preco) else ft.get("dy")
        dy_12m = dy_fund if dy_fund is not None else dy_cvm
        fonte_dy = "fundamentus" if dy_fund is not None else ("cvm" if dy_cvm is not None else None)
        # A série da CVM só vale para o histórico quando bate com o Fundamentus no período atual.
        conf_dy = (dy_cvm / dy_fund - 1) if (dy_cvm and dy_fund) else None
        if conf_dy is not None and abs(conf_dy) > 0.15:
            descartes.append(f"histórico de DY descartado: o DY de 12m pela CVM ({dy_cvm:.2f}%) diverge do Fundamentus ({dy_fund:.2f}%)")
            hist_dy = []
        if dy_12m is not None:
            hist_dy.append([hoje.year, 1, round(dy_12m, 4)])

        ev_manual = [e for e in eventos.get("eventos", []) if e.get("ticker") == t]

        fundo = {
            "ticker": t,
            "nome": fd.get("nome") or g.get("Nome_Fundo_Classe") or s.get("companyname"),
            "cnpj": cnpj,
            "isin": g.get("Codigo_ISIN"),
            "segmento_cvm": g.get("Segmento_Atuacao"),
            "mandato_cvm": g.get("Mandato"),
            "gestao": g.get("Tipo_Gestao") or fd.get("gestao"),
            "publico_alvo": g.get("Publico_Alvo"),
            "data_funcionamento": g.get("Data_Funcionamento"),
            "administrador": g.get("Nome_Administrador"),
            "setor_si": s.get("sectorname"),
            "segmento_si": s.get("segment"),
            "segmento_fund": ft.get("segmento_fund"),
            "preco": preco,
            "data_preco": dbr(fd.get("data_ult_cot")) or (y.get("ult") or [None])[0],
            "liquidez": liq,
            "cotistas": f(c.get("Total_Numero_Cotistas")) or s.get("numerocotistas"),
            "cotas": cotas,
            "vp_cota": vp_cota,
            "patrimonio": pl,
            "valor_mercado": vm,
            "ref_mensal": ult_d,
            "composicao": comp,
            "passivo_pl": (comp["passivo_total"] / pl) if (comp and comp["passivo_total"] is not None and pl) else None,
            "taxa_adm_mes_pct": (f(c.get("Percentual_Despesas_Taxa_Administracao")) or 0) * 100 if c else None,
            "eventos_cotas": ev_cotas,
            "rend_12m_cota": rend_12m,
            "meses_com_rendimento_12m": meses_rend,
            "dy_12m": dy_12m,
            "fonte_dy": fonte_dy,
            "dy_sobre_vp_12m": dyvp_12m,
            "conf_dy_fundamentus": conf_dy,
            "rend_mensal": [[m, round(r, 6) if r else None] for m, _, r in dy_vp[-13:]],
            "resultado": r12,
            "imoveis": im,
            "diversificacao": div,
            "fund": {k: fd.get(k) for k in ("ffo_12m", "rend_distribuido_12m", "venda_ativos_12m", "receita_12m", "qtd_imoveis",
                                            "area_m2", "relatorio", "ult_trimestral")} | {
                k: ft.get(k) for k in ("ffo_yield", "dy", "p_vp", "cap_rate", "vacancia_media", "preco_m2", "aluguel_m2")},
            "vol_1a": y.get("vol"),
            "mdd_1a": y.get("mdd"),
            "saltos_1a": y.get("saltos"),
            "pregoes_1a": y.get("n"),
            "primeiro_mes_cotacao": y.get("prim"),
            "fechamento_mensal": sorted((y.get("mens") or {}).items())[-24:],
            "hist": {"p_vp": hist_pvp, "dy": hist_dy, "vp_cota": hist_vp},
            "eventos": ev_manual,
            "fontes_ok": {"cvm": bool(cnpj), "fundamentus": bool(ft), "statusinvest": bool(s), "yahoo": bool(y.get("ult"))},
            "hist_descartes": descartes,
        }
        if not cnpj:
            sem_cvm.append(t)
        fundos.append(fundo)

    base = {
        "gerado_em": dt.datetime.now().isoformat(timespec="seconds"),
        "fontes": {
            "cvm_mensal_ultimo": max((x["ref_mensal"] or "") for x in fundos),
            "cvm_trimestral_ultimo": max(((x["resultado"] or {}).get("ref") or "") for x in fundos),
            "fundamentus": (ler_json("fundamentus_fii_resultado.json") and "tabela fii_resultado.php") or None,
            "statusinvest_coletado": si.get("coletado"),
            "yahoo_coletado": "2026-11-03 (data/raw/yahoo_fii.txt)",
            "ntnb": None,
        },
        "criterios": criterios,
        "grupos": grupos,
        "eventos_fii": eventos,
        "sem_cvm": sem_cvm,
        "mapeados_por_nome": por_nome,
        "fundos": fundos,
    }
    (RAIZ / "data").mkdir(exist_ok=True)
    (RAIZ / "data" / "base_fii.json").write_text(json.dumps(base, ensure_ascii=False), "utf-8")
    (RAIZ / "data" / "mapa_ticker_cnpj.json").write_text(json.dumps({t: v[0] for t, v in sorted(mapa.items())}, ensure_ascii=False, indent=0), "utf-8")
    print(f"fundos: {len(fundos)}; sem informe CVM: {len(sem_cvm)}")


if __name__ == "__main__":
    main()
