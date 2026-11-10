/*
 * Motor da Peneira FIIs (passos 1 a 4). Projeto separado da Peneira de Valor:
 * mesmo raciocínio, régua de fundo imobiliário. Roda no navegador (window.MotorFII)
 * e em Node (module.exports), para o site real poder rodar o mesmo cálculo no servidor.
 *
 * Entrada: base (data/base_fii.json, de collector/montar_base_fii.py) e params.
 * Saída: cada fundo com grupo, etapa em que parou, motivos, alertas, componentes do
 * índice de valor, posição no grupo e comparação com as médias de 10, 5 e 2 anos.
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.MotorFII = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  const ok = (v) => v !== null && v !== undefined && Number.isFinite(v);
  const GRUPOS = ["tijolo", "papel", "fof"];

  function paramsPadrao(c) {
    c = c || {};
    const p1 = c.passo1_operavel || {}, p2 = c.passo2_sangria_volatilidade || {};
    const p3 = c.passo3_indice_de_valor || {}, p4 = c.passo4_media_historica || {};
    return {
      liquidezMin: p1.liquidez_media_diaria_min_reais ?? 500000,
      mesesBolsa: p1.meses_minimos_de_bolsa ?? 12,
      excluirEventos: p1.excluir_eventos_pendentes ?? true,
      excluirSemCvm: p1.excluir_sem_informe_cvm ?? true,
      devPct: p1.desenvolvimento_pct_min ?? 50,
      exclResNeg12m: p2.excluir_resultado_negativo_12m ?? true,
      exclResNegTri: p2.excluir_resultado_negativo_ultimo_trimestre ?? true,
      payoutMax: p2.payout_max_pct ?? 110,
      vacMax: p2.vacancia_fisica_max_pct ?? 25,
      inadMax: p2.inadimplencia_max_pct ?? 10,
      passivoMax: p2.passivo_pl_max_pct ?? 30,
      exclUmImovel: p2.excluir_um_imovel_so ?? true,
      volPercentil: p2.excluir_percentil_mais_volateis ?? 20,
      pesos: JSON.parse(JSON.stringify(p3.pesos || {
        tijolo: { patrimonio_por_real: 1, resultado_por_real: 1, aluguel_por_real: 1, dividendo_por_real: 0 },
        papel: { patrimonio_por_real: 2, resultado_por_real: 1, aluguel_por_real: 0, dividendo_por_real: 1 },
        fof: { patrimonio_por_real: 1, resultado_por_real: 1, aluguel_por_real: 0, dividendo_por_real: 1 },
      })),
      janelas: p4.janelas_anos ?? [10, 5, 2],
    };
  }

  // ---------- grupo e subtipo ----------
  function grupoDe(f, grupos) {
    const pct = f.composicao && f.composicao.pct;
    if (!pct) return { grupo: null, hibrido: false };
    const comp = { tijolo: pct.imoveis || 0, papel: pct.papel || 0, fof: pct.fii || 0 };
    const min = (grupos && grupos.regra_pct_min ? grupos.regra_pct_min : 50) / 100;
    let melhor = null;
    for (const g of GRUPOS) if (!melhor || comp[g] > comp[melhor]) melhor = g;
    if (!(comp[melhor] > 0)) return { grupo: null, hibrido: false };
    return { grupo: melhor, hibrido: comp[melhor] < min, comp };
  }

  // Subtipo do tijolo: segmento informado à CVM (ou ao site); quando é genérico
  // ("Multicategoria", "Outros", "Híbrido"), tenta pelo nome do fundo.
  function subtipoDe(f, grupos) {
    const tipos = ((grupos && grupos.subtipos_tijolo) || []).filter((s) => s.match);
    const achar = (txt) => tipos.find((s) => new RegExp(s.match, "i").test(txt || ""));
    return achar([f.segmento_cvm, f.segmento_fund, f.segmento_si].filter(Boolean).join(" "))
      || achar(f.nome)
      || { id: "outros", nome: "Outros e híbridos" };
  }

  // ---------- percentis ----------
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

  // ---------- histórico ----------
  // Série anual de um indicador: [{ano, atual, v}], do mais recente para o mais antigo.
  function serie(f, chave) {
    return ((f.hist || {})[chave] || []).map(([ano, tp, v]) => ({ ano, atual: tp === 1, v }))
      .filter((x) => ok(x.v) && x.v > 0).sort((a, b) => (b.ano - a.ano) || (b.atual - a.atual));
  }

  const DIRECAO = { p_vp: "menor_melhor", dy: "maior_melhor" };

  function compararHistorico(f, chave, janelas) {
    const s = serie(f, chave);
    if (!s.length || !s[0].atual) return null;
    const atual = s[0].v;
    const passado = s.slice(1);
    const res = { chave, atual, serie: s.slice().reverse(), janelas: {} };
    for (const n of janelas) {
      const pts = passado.slice(0, n);
      const media = pts.length ? pts.reduce((t, x) => t + x.v, 0) / pts.length : null;
      const anos = pts.map((x) => x.ano);
      res.janelas[n] = {
        media, pontos: pts.length, completo: pts.length >= n,
        de: anos.length ? Math.min(...anos) : null, ate: anos.length ? Math.max(...anos) : null,
        desvio: ok(media) && media !== 0 ? (atual / media - 1) * 100 : null,
      };
    }
    const j5 = res.janelas[5] || res.janelas[janelas[0]];
    if (j5 && ok(j5.desvio)) {
      const melhor = DIRECAO[chave] === "menor_melhor" ? j5.desvio < 0 : j5.desvio > 0;
      res.leitura = Math.abs(j5.desvio) < 5 ? "na média" : melhor ? "mais barato que a média" : "mais caro que a média";
    }
    return res;
  }

  // ---------- preço alvo ----------
  // Preço em que o fundo voltaria à própria média de 5 anos no P/VP e no DY.
  function precoAlvo(f) {
    if (!f || !ok(f.preco) || !f.historico) return null;
    const partes = [];
    const pvp = f.historico.p_vp, dy = f.historico.dy;
    const m = (h) => h && h.janelas[5] && h.janelas[5].pontos >= 2 ? h.janelas[5] : null;
    if (m(pvp) && ok(f.vp_cota)) partes.push({ k: "P/VP", v: f.vp_cota * m(pvp).media, anos: m(pvp).pontos, peso: f.grupo === "papel" ? 2 : 1 });
    if (m(dy) && ok(f.dy_12m) && f.dy_12m > 0) {
      const rend = f.preco * f.dy_12m / 100;
      partes.push({ k: "DY", v: rend / (m(dy).media / 100), anos: m(dy).pontos, peso: 1 });
    }
    if (!partes.length) return null;
    const pt = partes.reduce((t, x) => t + x.peso, 0);
    return { v: partes.reduce((t, x) => t + x.v * x.peso, 0) / pt, partes };
  }

  // ---------- o método ----------
  function rodar(base, params) {
    const P = Object.assign(paramsPadrao(base.criterios), params || {});
    const brl = (v) => "R$ " + (v / 1e6).toLocaleString("pt-BR", { maximumFractionDigits: 2 }) + " mi";
    const pc = (v, d = 0) => v.toLocaleString("pt-BR", { maximumFractionDigits: d }) + "%";
    const hoje = new Date();
    const eventos = (base.eventos_fii && base.eventos_fii.eventos) || [];

    const fundos = base.fundos.map((f) => {
      const g = grupoDe(f, base.grupos);
      return {
        ...f, grupo: g.grupo, hibrido: g.hibrido, compGrupo: g.comp || null,
        subtipo: g.grupo === "tijolo" ? subtipoDe(f, base.grupos) : null,
        etapa: null, motivos: [], alertas: [],
      };
    });

    // Passo 1: o que não dá para operar.
    for (const f of fundos) {
      const m = [];
      if (!ok(f.liquidez) || f.liquidez < P.liquidezMin) m.push({ tipo: "liquidez", texto: `Liquidez média diária ${ok(f.liquidez) ? brl(f.liquidez) : "sem dado"} abaixo de ${brl(P.liquidezMin)}` });
      if (P.excluirSemCvm && !f.cnpj) m.push({ tipo: "universo", texto: "Sem informe mensal de FII na CVM: Fiagro, FI-Infra ou fundo sem cadastro como FII" });
      else if (!f.grupo) m.push({ tipo: "universo", texto: "Informe mensal sem composição do ativo para classificar o fundo" });
      if (f.ref_mensal) {
        const meses = (hoje - new Date(f.ref_mensal + "T12:00:00")) / 2.63e9;
        if (meses > 6) m.push({ tipo: "universo", texto: `Último informe mensal na CVM é de ${f.ref_mensal.slice(0, 7)}, há mais de 6 meses` });
      }
      const dev = f.composicao && f.composicao.pct_desenvolvimento;
      if (ok(dev) && dev * 100 >= P.devPct) m.push({ tipo: "universo", texto: `Fundo de desenvolvimento: ${pc(dev * 100)} do investido em obras, terrenos ou imóveis para venda` });
      const pregoes = f.pregoes_1a;
      if (ok(pregoes) && pregoes < 200 * (P.mesesBolsa / 12)) m.push({ tipo: "novo", texto: `Menos de ${P.mesesBolsa} meses de pregão (${pregoes} pregões na série de cotações)` });
      for (const e of eventos.filter((e) => e.ticker === f.ticker && e.pendente && e.tipo !== "credito")) {
        if (P.excluirEventos) m.push({ tipo: "evento", texto: `Evento pendente: ${e.descricao || e.tipo}`, fonte: e.fonte });
      }
      if (m.length) { f.etapa = 1; f.motivos = m; }
    }

    // Mesmo CNPJ com dois códigos (troca de ticker): fica o mais líquido.
    const porCnpj = new Map();
    for (const f of fundos.filter((x) => x.etapa === null && x.cnpj)) {
      const b = porCnpj.get(f.cnpj);
      if (!b || (f.liquidez || 0) > (b.liquidez || 0)) porCnpj.set(f.cnpj, f);
    }
    for (const f of fundos.filter((x) => x.etapa === null && x.cnpj)) {
      const b = porCnpj.get(f.cnpj);
      if (b !== f) { f.etapa = 1; f.motivos = [{ tipo: "codigo", texto: `Mesmo fundo de ${b.ticker} (código antigo ou duplicado), que é mais líquido` }]; }
    }

    // Diversificação: concentração medida sobre o ativo principal do grupo
    // (tijolo: receita por imóvel; papel: valor por CRI/LCI; FOF: valor por cota de FII).
    for (const f of fundos) {
      const d = f.diversificacao || {};
      f.conc = f.grupo === "tijolo" ? (d.imoveis && d.imoveis.conc_receita) || null
        : f.grupo === "papel" ? (d.cri && d.cri.conc) || null
        : f.grupo === "fof" ? (d.fii && d.fii.conc) || null : null;
    }

    // Passo 2: quem está sangrando e os mais voláteis.
    for (const f of fundos.filter((x) => x.etapa === null)) {
      const m = [], r = f.resultado || {}, im = f.imoveis || {};
      if (f.hibrido) f.alertas.push(`Híbrido: nenhum componente chega a 50% do investido; entra como ${f.grupo} pelo maior componente`);
      if (!ok(r.resultado_12m)) f.alertas.push("Sem dois semestres de informe trimestral para medir o resultado de 12 meses");
      if (P.exclResNeg12m && ok(r.resultado_12m) && r.resultado_12m < 0) m.push({ tipo: "resultado", texto: `Resultado financeiro negativo em 12 meses (${brl(r.resultado_12m)}, ${r.periodo})` });
      if (P.exclResNegTri && ok(r.resultado_ult_tri) && r.resultado_ult_tri < 0) m.push({ tipo: "resultado", texto: `Resultado negativo no trimestre de ${r.ref_ult_tri} (${brl(r.resultado_ult_tri)})` });
      if (ok(r.payout) && r.payout * 100 > P.payoutMax) m.push({ tipo: "payout", texto: `Distribuiu ${pc(r.payout * 100)} do resultado em 12 meses (${r.periodo}), acima de ${P.payoutMax}%` });
      if (ok(f.passivo_pl) && f.passivo_pl * 100 > P.passivoMax) m.push({ tipo: "alavancagem", texto: `Passivo de ${pc(f.passivo_pl * 100)} do PL, acima de ${P.passivoMax}%` });
      if (f.grupo === "tijolo") {
        if (ok(im.vacancia_fisica) && im.vacancia_fisica > P.vacMax) m.push({ tipo: "vacancia", texto: `Vacância física de ${pc(im.vacancia_fisica, 1)} (${im.ref}), acima de ${P.vacMax}%` });
        if (ok(im.inadimplencia) && im.inadimplencia > P.inadMax) m.push({ tipo: "inadimplencia", texto: `Inadimplência de ${pc(im.inadimplencia, 1)} da receita (${im.ref}), acima de ${P.inadMax}%` });
        const n = ok(im.n_renda) && im.n_renda > 0 ? im.n_renda : f.fund && f.fund.qtd_imoveis;
        if (P.exclUmImovel && n === 1) m.push({ tipo: "concentracao", texto: "Um imóvel só: risco binário de vacância" });
        if (!ok(im.vacancia_fisica)) f.alertas.push("Sem imóveis para renda no último informe trimestral: vacância e inadimplência não medidas");
        if (ok(im.maior_receita_pct) && im.maior_receita_pct > 50 && n > 1) f.alertas.push(`Um imóvel responde por ${pc(im.maior_receita_pct)} da receita`);
      }
      if (f.grupo === "papel" && f.conc && f.conc.maior_pct > 20) f.alertas.push(`Um só ativo responde por ${pc(f.conc.maior_pct)} da carteira de crédito`);
      if (f.grupo === "fof" && f.conc && f.conc.maior_pct > 30) f.alertas.push(`Uma só cota de FII responde por ${pc(f.conc.maior_pct)} da carteira`);
      if (f.grupo === "papel") {
        for (const e of eventos.filter((e) => e.ticker === f.ticker && e.pendente && e.tipo === "credito")) {
          m.push({ tipo: "credito", texto: `Evento de crédito: ${e.descricao}`, fonte: e.fonte });
        }
      }
      if (m.length) { f.etapa = 2; f.motivos = m; }
    }
    const cortesVol = {};
    for (const g of GRUPOS) {
      const vivos = fundos.filter((f) => f.etapa === null && f.grupo === g);
      const vols = vivos.map((f) => f.vol_1a).filter(ok).sort((a, b) => a - b);
      let corte = null;
      if (P.volPercentil > 0 && vols.length) corte = vols[Math.min(vols.length - 1, Math.floor(vols.length * (1 - P.volPercentil / 100)))];
      cortesVol[g] = corte;
      for (const f of vivos) {
        if (!ok(f.vol_1a)) { f.alertas.push("Sem histórico de cotação para medir a volatilidade"); continue; }
        if (f.saltos_1a > 0) f.alertas.push(`${f.saltos_1a} pregão(ões) com variação acima de 25% ficaram fora da volatilidade (provável desdobramento ou falha da fonte)`);
        if (ok(corte) && f.vol_1a > corte) {
          f.etapa = 2;
          f.motivos.push({ tipo: "volatilidade", texto: `Volatilidade de ${f.vol_1a.toFixed(1)}% a.a., entre os ${P.volPercentil}% mais voláteis do grupo ${g} (corte em ${corte.toFixed(1)}%)` });
        }
      }
    }

    // Passo 3: índice de valor por grupo.
    const vivos3 = fundos.filter((f) => f.etapa === null);
    for (const f of vivos3) {
      const vm = ok(f.valor_mercado) && f.valor_mercado > 0 ? f.valor_mercado : null;
      const r = f.resultado || {};
      const passivo = (f.composicao && f.composicao.passivo_total) || 0;
      const res12 = ok(r.resultado_12m) ? r.resultado_12m : (f.fund && ok(f.fund.ffo_12m) ? f.fund.ffo_12m : null);
      f.componentes = {
        patrimonio_por_real: ok(f.vp_cota) && f.preco > 0 ? f.vp_cota / f.preco : null,
        resultado_por_real: ok(res12) && vm ? res12 / vm : null,
        aluguel_por_real: f.grupo === "tijolo" && ok(r.aluguel_12m) && r.aluguel_12m > 0 && vm ? r.aluguel_12m / (vm + passivo) : null,
        dividendo_por_real: ok(f.dy_12m) ? f.dy_12m / 100 : null,
      };
      if (!ok(r.resultado_12m) && ok(res12)) f.alertas.push("Resultado de 12 meses pelo FFO do Fundamentus (informe trimestral incompleto)");
    }
    for (const g of GRUPOS) {
      const grupo = vivos3.filter((f) => f.grupo === g);
      const pesos = P.pesos[g] || {};
      const pcts = {};
      for (const k of Object.keys(pesos)) pcts[k] = percentis(grupo.map((f) => f.componentes[k]));
      grupo.forEach((f, i) => {
        f.percentis = {};
        let soma = 0, peso = 0;
        for (const [k, w] of Object.entries(pesos)) {
          if (!(w > 0)) continue;
          const p = pcts[k][i];
          f.percentis[k] = p;
          if (ok(p)) { soma += p * w; peso += w; }
          else f.alertas.push(`Sem dado para ${k.replace(/_/g, " ")}`);
        }
        f.indice = peso ? soma / peso : null;
      });
    }
    for (const f of vivos3) if (!ok(f.indice)) { f.etapa = 3; f.motivos = [{ tipo: "dados", texto: "Sem dados suficientes para calcular o índice de valor" }]; }

    // Passo 4: média histórica.
    for (const f of vivos3.filter((x) => x.etapa === null)) {
      f.historico = {};
      for (const k of ["p_vp", "dy"]) {
        const h = compararHistorico(f, k, P.janelas);
        if (h) f.historico[k] = h;
      }
      const d = [];
      const pv = f.historico.p_vp && f.historico.p_vp.janelas[5];
      const dy = f.historico.dy && f.historico.dy.janelas[5];
      if (pv && ok(pv.desvio)) d.push(-pv.desvio);
      if (dy && ok(dy.desvio)) d.push(dy.desvio);
      f.descontoHist = d.length ? d.reduce((t, x) => t + x, 0) / d.length : null;
      f.anosHist = Math.max(0, ...Object.values(f.historico).map((h) => h.janelas[P.janelas[0]].pontos));
      f.alvo = precoAlvo(f);
      if ((f.hist_descartes || []).length) f.alertas.push(...f.hist_descartes.map((x) => "Histórico: " + x));
      f.etapa = 4;
    }

    const ranqueados = vivos3.filter((f) => f.etapa === 4).sort((a, b) => b.indice - a.indice);
    const porGrupo = {};
    for (const g of GRUPOS) {
      porGrupo[g] = ranqueados.filter((f) => f.grupo === g);
      porGrupo[g].forEach((f, i) => { f.posicao = i + 1; });
    }
    ranqueados.forEach((f, i) => { f.posicaoGeral = i + 1; });

    const conta = (fn) => fundos.filter(fn).length;
    const tem = (f, t) => f.motivos.some((m) => m.tipo === t);
    const funil = {
      universo: fundos.length,
      passo1: {
        saem: conta((f) => f.etapa === 1),
        liquidez: conta((f) => f.etapa === 1 && tem(f, "liquidez")),
        universo: conta((f) => f.etapa === 1 && !tem(f, "liquidez") && tem(f, "universo")),
        novo: conta((f) => f.etapa === 1 && !tem(f, "liquidez") && tem(f, "novo")),
        outros: conta((f) => f.etapa === 1 && !tem(f, "liquidez") && !tem(f, "universo") && !tem(f, "novo")),
      },
      passo2: {
        saem: conta((f) => f.etapa === 2),
        sangria: conta((f) => f.etapa === 2 && f.motivos.some((m) => m.tipo !== "volatilidade")),
        volatilidade: conta((f) => f.etapa === 2 && f.motivos.every((m) => m.tipo === "volatilidade")),
        cortesVol,
      },
      passo3: { saem: conta((f) => f.etapa === 3) },
      ranqueados: ranqueados.length,
      grupos: Object.fromEntries(GRUPOS.map((g) => [g, porGrupo[g].length])),
    };
    return { params: P, fundos, ranqueados, porGrupo, funil };
  }

  return { rodar, paramsPadrao, percentis, serie, precoAlvo, grupoDe, GRUPOS };
});
