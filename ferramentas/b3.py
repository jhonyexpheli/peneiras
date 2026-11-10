"""Leitura do COTAHIST compacto (baixar_cotahist.py) e as medidas de preço que as peneiras usam.

Ferramenta neutra: não conhece o método de nenhuma das peneiras. Cada peneira importa daqui
só a leitura da série e o resumo de preço; o que fazer com eles fica no coletor de cada uma.

O COTAHIST traz o preço negociado, sem ajuste por proventos. Para volatilidade, maior queda e
gráfico mensal, os desdobramentos e grupamentos são detectados na própria série e corrigidos
(ver ajustar_eventos). Rendimentos e dividendos não são ajustados: a queda na data ex entra como
variação normal do dia, o que mexe pouco na volatilidade anual.
"""
from __future__ import annotations

import csv
import gzip
import math
from collections import defaultdict

FATORES = [2, 3, 4, 5, 6, 8, 10, 15, 20, 25, 30, 40, 50, 100, 200, 1000]


def ler_vista(caminho: str, filtro=None):
    """{ticker: [(data, fechamento, volume, negocios, codbdi, isin), ...]} em ordem de data, e a lista de pregões.

    filtro(ticker, codbdi, isin) -> bool escolhe as séries que interessam.
    """
    series = defaultdict(list)
    pregoes = set()
    with gzip.open(caminho, "rt", encoding="utf-8") as fh:
        for r in csv.DictReader(fh):
            pregoes.add(r["data"])
            if filtro and not filtro(r["ticker"], r["codbdi"], r["isin"]):
                continue
            series[r["ticker"]].append((r["data"], float(r["fechamento"]), float(r["volume"]),
                                        int(r["negocios"]), r["codbdi"], r["isin"]))
    for s in series.values():
        s.sort()
    return dict(series), sorted(pregoes)


def ajustar_eventos(pontos):
    """Corrige desdobramentos e grupamentos: [(data, preço)] -> ([(data, preço ajustado)], eventos).

    Um evento é uma variação de um dia que bate com um fator redondo (1 para 2, 10 para 1...) com
    folga de 7% e que se mantém no pregão seguinte. Os preços anteriores são multiplicados pelo
    fator, para a série ficar na base de cotas de hoje.
    """
    eventos = []
    for i in range(1, len(pontos)):
        p0, p1 = pontos[i - 1][1], pontos[i][1]
        if not (p0 > 0 and p1 > 0):
            continue
        r = p1 / p0
        if 0.6 < r < 1.6:
            continue
        fator = None
        for k in FATORES:
            if abs(r * k - 1) < 0.07:
                fator = 1 / k   # desdobramento: cada cota virou k
            elif abs(r / k - 1) < 0.07:
                fator = k       # grupamento: k cotas viraram uma
            if fator:
                break
        if not fator:
            continue
        if i + 1 < len(pontos) and not (0.7 < pontos[i + 1][1] / p1 < 1.4):
            continue  # salto que volta no dia seguinte é erro de registro, não evento
        if i >= 2 and 0.7 < p1 / pontos[i - 2][1] < 1.4:
            continue  # é a volta de um erro de registro do pregão anterior
        eventos.append({"data": pontos[i][0], "fator": fator})
    if not eventos:
        return list(pontos), []
    ajustado, mult, j = [], 1.0, len(eventos) - 1
    for d, p in reversed(pontos):
        while j >= 0 and d < eventos[j]["data"]:
            mult *= eventos[j]["fator"]
            j -= 1
        ajustado.append((d, p * mult))
    ajustado.reverse()
    return ajustado, eventos


def _vol(rets):
    """Desvio-padrão anualizado (%) sem os saltos acima de 25% num dia; devolve (vol, saltos)."""
    bons = [r for r in rets if abs(r) <= 0.25]
    if len(bons) < 100:
        return None, len(rets) - len(bons)
    m = sum(bons) / len(bons)
    return math.sqrt(sum((r - m) ** 2 for r in bons) / (len(bons) - 1)) * math.sqrt(252) * 100, len(rets) - len(bons)


def _liquidez(serie, pregoes, inicio=None, n=None, so_negociados=False):
    """Volume médio por pregão na janela (data inicial ou últimos n pregões da bolsa)."""
    janela = pregoes[-n:] if n else [d for d in pregoes if d >= inicio]
    if not janela:
        return None
    vols = [v for d, _, v, *_ in serie if d >= janela[0]]
    if so_negociados:
        return sum(vols) / len(vols) if vols else 0.0
    return sum(vols) / len(janela)


def resumo(serie, pregoes, meses_liquidez: int = 2, meses_mensal: int = 121, max_sem_negocio: int = 22):
    """Medidas de preço de uma série do ler_vista.

    preco, data_preco    último fechamento negociado
    liquidez             volume financeiro médio por pregão nos últimos `meses_liquidez` meses
                         (pregões sem negócio contam como zero)
    vol_1a, vol_2a       volatilidade anualizada dos retornos diários (252 e 504 últimos negócios)
    saltos_1a            dias com variação acima de 25% que ficaram fora da volatilidade
    mdd_1a               maior queda do pico ao vale no último ano (%)
    pregoes_1a           pregões da bolsa no último ano desde o primeiro negócio do ativo (máx. 252)
    primeiro             primeiro negócio dentro da base baixada
    mensal               [[AAAA-MM, fechamento ajustado]] dos últimos meses
    dezembro             {ano: fechamento de dezembro sem ajuste} (para P/VP contra o VP da época)
    eventos              desdobramentos e grupamentos detectados
    ativo                negociou nos últimos `max_sem_negocio` pregões; quando não, volatilidade e
                         maior queda ficam vazias e a liquidez é zero (o ativo saiu de bolsa,
                         foi incorporado ou trocou de código)
    liquidez_variantes   outras janelas de liquidez, para comparar com as fontes antigas
    """
    if not serie:
        return None
    ult_data = pregoes[-1]
    pts = [(d, p) for d, p, *_ in serie if p > 0]
    if not pts:
        return None
    adj, eventos = ajustar_eventos(pts)

    sem_negocio = sum(1 for d in pregoes if d > pts[-1][0])
    ativo = sem_negocio <= max_sem_negocio
    rets = [math.log(adj[i][1] / adj[i - 1][1]) for i in range(1, len(adj))]
    v1, s1 = _vol(rets[-252:])
    v2, _ = _vol(rets[-504:])

    um_ano = pregoes[-252:]
    pico, mdd, no_ano = -1.0, 0.0, 0
    for d, p in adj:
        if d >= um_ano[0]:
            no_ano += 1
            pico = max(pico, p)
            mdd = min(mdd, p / pico - 1)
    pregoes_1a = sum(1 for d in um_ano if d >= pts[0][0])

    a, m = int(ult_data[:4]), int(ult_data[5:7]) - meses_liquidez + 1
    while m <= 0:
        a, m = a - 1, m + 12
    inicio = f"{a}-{m:02d}-01"
    liquidez = _liquidez(serie, pregoes, inicio=inicio)
    variantes = {
        "2_meses": liquidez,
        "2_meses_so_dias_com_negocio": _liquidez(serie, pregoes, inicio=inicio, so_negociados=True),
        "21_pregoes": _liquidez(serie, pregoes, n=21),
        "42_pregoes": _liquidez(serie, pregoes, n=42),
        "63_pregoes": _liquidez(serie, pregoes, n=63),
    }

    mensal = {}
    for d, p in adj:
        mensal[d[:7]] = p
    dezembro = {}
    for d, p in pts:
        if d[5:7] == "12":
            dezembro[int(d[:4])] = p

    return {
        "preco": pts[-1][1],
        "data_preco": pts[-1][0],
        "liquidez": liquidez if ativo else 0.0,
        "liquidez_variantes": {k: (round(v, 2) if v is not None else None) for k, v in variantes.items()},
        "vol_1a": v1 if ativo else None,
        "vol_2a": v2 if ativo else None,
        "saltos_1a": s1,
        "mdd_1a": mdd * 100 if ativo and no_ano > 1 else None,
        "ativo": ativo,
        "pregoes_sem_negocio": sem_negocio,
        "pregoes_1a": pregoes_1a,
        "primeiro": pts[0][0],
        "mensal": [[k, round(mensal[k], 4)] for k in sorted(mensal)[-meses_mensal:]],
        "dezembro": {k: round(v, 4) for k, v in sorted(dezembro.items())},
        "eventos": eventos,
        "isin": serie[-1][5],
        "codbdi": serie[-1][4],
    }
