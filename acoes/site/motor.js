/*
 * Motor do método (4 passos) — estratégia Ramiro Gomes Ferreira / Clube do Valor.
 * Funciona no navegador (window.Motor) e em Node (module.exports), para o site
 * real poder rodar o mesmo cálculo no servidor.
 *
 * Entrada: base (data/base.json, gerada por collector/montar_base.py) e params.
 * Saída: cada ação com a etapa em que parou, os motivos, os componentes do
 * índice de valor e a comparação com as médias históricas (10, 5 e 2 anos).
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.Motor = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  const SIT_NOME = {
    RJ: "Em recuperação judicial",
    REJ: "Em recuperação extrajudicial",
    FAL: "Falida",
    LE: "Em liquidação extrajudicial",
    LJ: "Em liquidação judicial",
  };

  function paramsPadrao(criterios) {
    const c = criterios || {};
    const p1 = c.passo1_operavel || {};
    const p2 = c.passo2_prejuizo_volatilidade || {};
    const p3 = c.passo3_indice_de_valor || {};
    const p4 = c.passo4_media_historica || {};
    const pesos = (o) => Object.fromEntries(Object.entries(o || {}).filter(([k]) => !k.startsWith("_")).map(([k, v]) => [k, v.peso]));
    return {
      liquidezMin: p1.liquidez_media_diaria_min_reais ?? 1e6,
      excluirSituacoes: p1.excluir_situacoes_cvm ?? ["RJ", "REJ", "FAL", "LE", "LJ"],
      excluirOpa: p1.excluir_opa_pendente ?? true,
      excluirPrejuizo12m: p2.excluir_prejuizo_12m ?? true,
      excluirPrejuizoTri: p2.excluir_prejuizo_ultimo_trimestre ?? true,
      excluirPrejuizoExercicio: p2.excluir_prejuizo_ultimo_exercicio ?? true,
      volPercentil: p2.excluir_percentil_mais_volateis ?? 20,
      volTeto: p2.volatilidade_teto_absoluto_pct ?? null,
      pesosPadrao: pesos(p3.componentes_padrao) || { caixa_por_real: 1, lucro_operacional_por_real: 1, patrimonio_por_real: 1 },
      pesosFinanceiro: pesos(p3.componentes_financeiro) || { lucro_por_real: 1, patrimonio_por_real: 1, dividendo_por_real: 1 },
      umaClasse: p3.uma_classe_por_empresa ?? true,
      caixaBase: ((p3.componentes_padrao || {}).caixa_por_real || {}).base || "liquido",
      janelas: p4.janelas_anos ?? [10, 5, 2],
      baseHist: p4.indicadores_base ?? ["ev_ebit", "p_vp", "p_l", "caixa_liquido_por_real"],
    };
  }

  const ok = (v) => v !== null && v !== undefined && Number.isFinite(v);

  function perfilDe(a, setores) {
    for (const p of setores.perfis) {
      const m = p.match || {};
      const t = (re, s) => !re || new RegExp(re, "i").test(s || "");
      if (t(m.setor, a.setor) && t(m.subsetor, a.subsetor) && t(m.segmento, a.segmento)) return p;
    }
    return setores.perfis[setores.perfis.length - 1];
  }

  // Percentil (0-100) de cada valor dentro da lista; maior valor = maior percentil.
  function percentis(valores) {
    const pares = valores.map((v, i) => [v, i]).filter(([v]) => ok(v)).sort((a, b) => a[0] - b[0]);
    const out = new Array(valores.length).fill(null);
    const n = pares.length;
    for (let k = 0; k < n; ) {
      let j = k;
      while (j + 1 < n && pares[j + 1][0] === pares[k][0]) j++;
      const p = n === 1 ? 100 : (((k + j) / 2) / (n - 1)) * 100;
      for (let q = k; q <= j; q++) out[pares[q][1]] = p;
      k = j + 1;
    }
    return out;
  }

  // Série anual de um indicador: [{ano, atual (bool), v}], do mais recente para o mais antigo.
  function serie(a, chave) {
    const h = a.hist || {};
    if (chave === "caixa_liquido_por_real") {
      const dl = h.dividaliquida_patrimonioliquido || [], pvp = h.p_vp || [];
      const mapa = new Map(pvp.map(([ano, tp, v]) => [ano + ":" + tp, v]));
      return dl.map(([ano, tp, v]) => {
        const p = mapa.get(ano + ":" + tp);
        return { ano, atual: tp === 1, v: ok(v) && ok(p) && p > 0 ? -v / p : null };
      }).filter((x) => ok(x.v)).sort((x, y) => y.ano - x.ano);
    }
    return (h[chave] || []).map(([ano, tp, v]) => ({ ano, atual: tp === 1, v })).filter((x) => ok(x.v)).sort((x, y) => y.ano - x.ano);
  }

  const MULTIPLO = new Set(["p_l", "p_vp", "ev_ebit", "ev_ebitda", "dividaliquida_ebitda", "dividaliquida_ebit"]);

  function compararHistorico(a, chave, janelas, ind) {
    const s = serie(a, chave);
    if (!s.length) return null;
    const atual = s[0].atual ? s[0].v : null;
    const res = { chave, atual, anoAtual: s[0].atual ? s[0].ano : null, serie: s.slice().reverse(), janelas: {} };
    for (const n of janelas) {
      const pts = s.slice(0, n);
      // Múltiplos negativos (ano de prejuízo) não entram na média de valuation.
      const validos = MULTIPLO.has(chave) ? pts.filter((x) => x.v > 0) : pts;
      const media = validos.length ? validos.reduce((t, x) => t + x.v, 0) / validos.length : null;
      const anos = pts.map((x) => x.ano);
      res.janelas[n] = {
        media,
        pontos: pts.length,
        usados: validos.length,
        completo: pts.length >= n,
        de: anos.length ? Math.min(...anos) : null,
        ate: anos.length ? Math.max(...anos) : null,
        desvio: ok(atual) && ok(media) && media !== 0 ? (atual / media - 1) * 100 : null,
      };
    }
    const dir = (ind[chave] || {}).direcao || "maior_melhor";
    const j5 = res.janelas[5] || res.janelas[janelas[0]];
    if (j5 && ok(j5.desvio)) {
      const melhor = dir === "menor_melhor" ? j5.desvio < 0 : j5.desvio > 0;
      res.leitura = Math.abs(j5.desvio) < 5 ? "na média" : melhor ? "melhor que a média" : "pior que a média";
    }
    return res;
  }

  function ultimoExercicio(a) {
    const s = serie(a, "lpa").filter((x) => !x.atual);
    return s.length ? s[0] : null;
  }

  function rodar(base, params) {
    const P = Object.assign(paramsPadrao(base.criterios), params || {});
    const setores = base.setores;
    const ind = setores.indicadores;
    const brl = (v) => "R$ " + (v / 1e6).toLocaleString("pt-BR", { maximumFractionDigits: 1 }) + " mi";

    const acoes = base.acoes.map((a) => ({
      ...a,
      perfil: perfilDe(a, setores),
      etapa: null, // 1..3 = eliminada no passo; 4 = ranqueada; "classe" = outra classe da mesma empresa
      motivos: [],
      alertas: [],
    }));

    // Passo 1: o que não dá para operar.
    for (const a of acoes) {
      const m = [];
      if (!ok(a.liquidez) || a.liquidez < P.liquidezMin) m.push({ tipo: "liquidez", texto: `Liquidez média diária ${ok(a.liquidez) ? brl(a.liquidez) : "sem dado"} abaixo de ${brl(P.liquidezMin)}` });
      if (a.cvm && P.excluirSituacoes.includes(a.cvm.cod)) m.push({ tipo: "cvm", texto: `${SIT_NOME[a.cvm.cod] || a.cvm.cod} (CVM, desde ${(a.cvm.desde || "").slice(0, 7)})` });
      if (a.opa && P.excluirOpa) m.push({ tipo: "opa", texto: `OPA pendente: ${a.opa.tipo}` });
      if (m.length) { a.etapa = 1; a.motivos = m; }
    }

    // Passo 2: prejuízo (12m, trimestre, último exercício) e as mais voláteis.
    const vivos2 = acoes.filter((a) => a.etapa === null);
    for (const a of vivos2) {
      const m = [];
      if (!a.tem_ficha) m.push({ tipo: "dados", texto: "Sem balanço disponível no Fundamentus" });
      if (P.excluirPrejuizo12m && ok(a.lucro_12m) && a.lucro_12m < 0) m.push({ tipo: "prejuizo", texto: `Prejuízo nos últimos 12 meses (${brl(a.lucro_12m)})` });
      if (P.excluirPrejuizoTri && ok(a.lucro_3m) && a.lucro_3m < 0) m.push({ tipo: "prejuizo", texto: `Prejuízo no último trimestre (${brl(a.lucro_3m)}, balanço de ${a.ultimo_balanco || "?"})` });
      const ex = ultimoExercicio(a);
      if (P.excluirPrejuizoExercicio && ex && ex.v < 0) m.push({ tipo: "prejuizo", texto: `Prejuízo no exercício de ${ex.ano} (LPA ${ex.v.toLocaleString("pt-BR")})` });
      if (m.length) { a.etapa = 2; a.motivos = m; }
    }
    const vivosVol = acoes.filter((a) => a.etapa === null);
    const vols = vivosVol.map((a) => a.vol_1a).filter(ok).sort((x, y) => x - y);
    let corteVol = null;
    if (P.volPercentil > 0 && vols.length) corteVol = vols[Math.min(vols.length - 1, Math.floor(vols.length * (1 - P.volPercentil / 100)))];
    for (const a of vivosVol) {
      if (!ok(a.vol_1a)) { a.alertas.push("Sem histórico de preço para medir a volatilidade"); continue; }
      if (a.saltos_1a > 0) a.alertas.push(`${a.saltos_1a} dia(s) com variação acima de 25% ficaram fora da volatilidade (provável evento societário ou falha de ajuste)`);
      const acimaPct = ok(corteVol) && a.vol_1a > corteVol;
      const acimaTeto = ok(P.volTeto) && a.vol_1a > P.volTeto;
      if (acimaPct || acimaTeto) {
        a.etapa = 2;
        a.motivos.push({ tipo: "volatilidade", texto: `Volatilidade de ${a.vol_1a.toFixed(1)}% a.a. ${acimaTeto ? `acima do teto de ${P.volTeto}%` : `entre os ${P.volPercentil}% mais voláteis (corte em ${corteVol.toFixed(1)}%)`}` });
      }
    }

    // Uma classe por empresa: mantém a mais líquida.
    if (P.umaClasse) {
      const melhor = new Map();
      for (const a of acoes.filter((x) => x.etapa === null)) {
        const k = a.empresa_id ?? a.empresa;
        const b = melhor.get(k);
        if (!b || (a.liquidez || 0) > (b.liquidez || 0)) melhor.set(k, a);
      }
      for (const a of acoes.filter((x) => x.etapa === null)) {
        const b = melhor.get(a.empresa_id ?? a.empresa);
        if (b !== a) { a.etapa = "classe"; a.motivos = [{ tipo: "classe", texto: `Mesma empresa de ${b.ticker}, que é mais líquida` }]; }
      }
    }

    // Passo 3: índice de valor — quanto se leva por real pago.
    const vivos3 = acoes.filter((a) => a.etapa === null);
    for (const a of vivos3) {
      const vm = a.valor_mercado, ev = a.valor_firma;
      if (a.perfil.financeiro) {
        a.componentes = {
          lucro_por_real: ok(a.lucro_12m) && vm > 0 ? a.lucro_12m / vm : null,
          patrimonio_por_real: ok(a.patrimonio) && vm > 0 ? a.patrimonio / vm : null,
          dividendo_por_real: ok(a.ind.dy) ? a.ind.dy / 100 : null,
        };
      } else {
        a.componentes = {
          // Caixa líquido = disponibilidades - dívida bruta (= -dívida líquida do Fundamentus).
          caixa_por_real: vm > 0 ? (P.caixaBase === "bruto" ? (ok(a.caixa) ? a.caixa / vm : null) : (ok(a.divida_liquida) ? -a.divida_liquida / vm : null)) : null,
          // EV negativo (caixa maior que valor de mercado + dívida) é o caso mais barato possível.
          lucro_operacional_por_real: ok(a.ebit_12m) && ok(ev) ? (ev > 0 ? a.ebit_12m / ev : (a.ebit_12m > 0 ? 9.99 : null)) : null,
          patrimonio_por_real: ok(a.patrimonio) && vm > 0 ? a.patrimonio / vm : null,
        };
      }
    }
    for (const fin of [false, true]) {
      const grupo = vivos3.filter((a) => !!a.perfil.financeiro === fin);
      const pesos = fin ? P.pesosFinanceiro : P.pesosPadrao;
      const pcts = {};
      for (const k of Object.keys(pesos)) pcts[k] = percentis(grupo.map((a) => a.componentes[k]));
      grupo.forEach((a, i) => {
        a.percentis = {};
        let soma = 0, peso = 0;
        for (const [k, w] of Object.entries(pesos)) {
          const p = pcts[k][i];
          a.percentis[k] = p;
          if (ok(p) && w > 0) { soma += p * w; peso += w; }
          if (!ok(p)) a.alertas.push(`Sem dado para ${k.replace(/_/g, " ")}`);
        }
        a.indice = peso ? soma / peso : null;
        a.grupo = fin ? "financeiro" : "padrao";
      });
    }

    // Sem nenhum componente calculável, não há como ordenar.
    for (const a of vivos3) if (!ok(a.indice)) { a.etapa = 3; a.motivos = [{ tipo: "dados", texto: "Sem dados de balanço suficientes para calcular o índice de valor" }]; }

    // Passo 4: média histórica (10, 5 e 2 anos) dos KPIs-base e dos setoriais.
    for (const a of vivos3) {
      if (a.etapa === 3) continue;
      const chaves = [...new Set([...(a.perfil.financeiro ? ["p_vp", "p_l", "dy", "roe"] : P.baseHist), ...a.perfil.kpis])];
      a.historico = {};
      for (const k of chaves) {
        const r = compararHistorico(a, k, P.janelas, ind);
        if (r) a.historico[k] = r;
      }
      // Desconto vs média de 5 anos nos múltiplos de preço do índice.
      const alvo = a.perfil.financeiro ? ["p_vp", "p_l"] : ["ev_ebit", "p_vp"];
      const d = alvo.map((k) => a.historico[k]?.janelas?.[5]?.desvio).filter(ok);
      a.descontoHist = d.length ? -d.reduce((t, x) => t + x, 0) / d.length : null;
      const anos = Object.values(a.historico).map((h) => h.janelas[P.janelas[0]]?.pontos || 0);
      a.anosHist = anos.length ? Math.max(...anos) : 0;
      a.etapa = 4;
    }

    const ranqueadas = vivos3.filter((a) => ok(a.indice)).sort((x, y) => y.indice - x.indice);
    ranqueadas.forEach((a, i) => (a.posicao = i + 1));

    const conta = (f) => acoes.filter(f).length;
    const funil = {
      universo: acoes.length,
      passo1: { saem: conta((a) => a.etapa === 1), liquidez: conta((a) => a.etapa === 1 && a.motivos.some((m) => m.tipo === "liquidez")), cvm: conta((a) => a.etapa === 1 && a.motivos.some((m) => m.tipo === "cvm")), opa: conta((a) => a.etapa === 1 && a.motivos.some((m) => m.tipo === "opa")) },
      passo2: { saem: conta((a) => a.etapa === 2), prejuizo: conta((a) => a.etapa === 2 && a.motivos.some((m) => m.tipo === "prejuizo")), volatilidade: conta((a) => a.etapa === 2 && a.motivos.some((m) => m.tipo === "volatilidade")), dados: conta((a) => a.etapa === 2 && a.motivos.some((m) => m.tipo === "dados")), corteVol },
      classes: conta((a) => a.etapa === "classe"),
      passo3: { saem: conta((a) => a.etapa === 3) },
      ranqueadas: ranqueadas.length,
    };
    return { params: P, acoes, ranqueadas, funil };
  }

  return { rodar, paramsPadrao, perfilDe, percentis, serie, SIT_NOME };
});
