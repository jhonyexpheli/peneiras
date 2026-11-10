/*
 * Aba Carteira: posições montadas a partir da peneira, cada uma com quantidade,
 * preço de entrada, data e preço alvo. Compara com a cotação da base e com o
 * ranking do dia.
 *
 * Onde fica salvo:
 *  - publicado como Artifact: banco do artifact (capability `db`), coleção
 *    `carteira` (um documento por ticker) e documento `ajustes/carteira` (capital);
 *  - fora do Artifact (site estático): localStorage deste navegador.
 * No site real, troque `Armazem` por chamadas à API própria mantendo a mesma forma
 * dos documentos: {ticker, qtd, preco_entrada, data_entrada, preco_alvo, nota, atualizado}.
 *
 * Usa as funções da interface principal ($, ok, nf, esc, R, BASE, Motor, abrir,
 * trocarAba), sempre no momento da chamada.
 */
const Carteira = (() => {
  "use strict";
  const COL = "carteira", DOC_AJ = "ajustes/carteira", LS = "peneira-carteira-v1";
  const CAPITAL_PADRAO = 10000;
  let modo = "carregando";          // "db" | "local" | "carregando"
  let db = null, podeEditar = true, aviso = "", timer = null, iniciado = false;
  let posicoes = new Map(), capital = CAPITAL_PADRAO;
  let editando = null, removendo = null, gravando = false;

  const brl = (v, d = 2) => ok(v) ? (v < 0 ? "−" : "") + "R$ " + nf(Math.abs(v), d) : "–";
  const sinal = (v, d = 1) => ok(v) ? (v > 0 ? "+" : v < 0 ? "−" : "") + nf(Math.abs(v), d) + "%" : "–";
  const hojeISO = () => { const d = new Date(); return new Date(d - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
  const dataBR = (iso) => iso ? iso.split("-").reverse().join("/") : "";
  const isoDeBR = (br) => /^\d{2}\/\d{2}\/\d{4}$/.test(br || "") ? br.split("/").reverse().join("-") : null;
  const acao = (t) => (R?.acoes || BASE?.acoes || []).find((a) => a.ticker === t);

  // Preço alvo pelo método: o preço em que a ação voltaria à própria média de 5 anos
  // nos múltiplos do passo 4 (EV/EBIT e P/VP; bancos e seguradoras P/VP e P/L).
  // EV/EBIT é convertido em preço descontando a dívida líquida do valor da firma.
  function alvoMetodo(a) {
    if (!a || !ok(a.preco) || a.preco <= 0) return null;
    const media5 = (k) => {
      const s = Motor.serie(a, k);
      if (!s.length || !s[0].atual || !(s[0].v > 0)) return null;
      const v = s.slice(0, 5).filter((x) => x.v > 0);
      return v.length ? {atual: s[0].v, media: v.reduce((t, x) => t + x.v, 0) / v.length, anos: v.length} : null;
    };
    const p = a.preco, partes = [];
    const pvp = media5("p_vp");
    if (pvp) partes.push({k: "P/VP", v: p * pvp.media / pvp.atual, anos: pvp.anos});
    const fin = a.perfil ? !!a.perfil.financeiro : /financeiro|seguro|banco/i.test(a.setor || "");
    if (fin) {
      const pl = media5("p_l");
      if (pl) partes.push({k: "P/L", v: p * pl.media / pl.atual, anos: pl.anos});
    } else {
      const ev = media5("ev_ebit"), vf = a.valor_firma, vm = a.valor_mercado;
      if (ev && ok(vf) && vf > 0 && ok(vm) && vm > 0) {
        const equity = vf * ev.media / ev.atual - (vf - vm);
        if (equity > 0) partes.push({k: "EV/EBIT", v: equity / (vm / p), anos: ev.anos});
      }
    }
    if (!partes.length) return null;
    return {v: partes.reduce((t, x) => t + x.v, 0) / partes.length, partes};
  }

  // ---------- armazenamento ----------
  const Armazem = {
    async salvar(t, corpo) {
      if (modo === "db") { await db.collection(COL).doc(t).set(corpo); return; }
      posicoes.set(t, corpo); gravarLocal(); desenhar();
    },
    async remover(t) {
      if (modo === "db") { await db.collection(COL).doc(t).delete(); return; }
      posicoes.delete(t); gravarLocal(); desenhar();
    },
    async capital(v) {
      if (modo === "db") { await db.doc(DOC_AJ).set({capital: v, atualizado: new Date().toISOString()}); return; }
      capital = v; gravarLocal(); desenhar();
    },
  };
  function lerLocal() {
    try {
      const o = JSON.parse(localStorage.getItem(LS) || "null");
      if (o) { posicoes = new Map(Object.entries(o.posicoes || {})); if (ok(o.capital)) capital = o.capital; }
    } catch (e) {}
  }
  function gravarLocal() {
    try { localStorage.setItem(LS, JSON.stringify({capital, posicoes: Object.fromEntries(posicoes)})); } catch (e) {}
  }

  async function iniciar() {
    if (iniciado) return; iniciado = true;
    montarForm();
    desenhar();
    const usar = window.claude && typeof window.claude.use === "function" ? (n) => window.claude.use(n).catch(() => null) : async () => null;
    const [d, u] = await Promise.all([usar("db"), usar("user")]);
    if (u && typeof u.canEdit === "function") {
      try { const c = await u.canEdit(); if (c === false) podeEditar = false; } catch (e) {}
    }
    if (!d) { modo = "local"; lerLocal(); desenhar(); return; }
    db = d; modo = "db";
    let chegou = false;
    timer = setTimeout(() => { if (!chegou) { aviso = "A carteira salva ainda não respondeu. O que aparece pode estar desatualizado."; desenhar(); } }, 10000);
    const erro = (e) => { clearTimeout(timer); aviso = "Não foi possível ler a carteira salva agora. Recarregue a página mais tarde."; console.warn("carteira", e?.code); desenhar(); };
    db.collection(COL).onSnapshot((s) => {
      posicoes = new Map(s.docs.map((x) => [x.id, x.data()]));
      if (!s.metadata.fromCache) { chegou = true; clearTimeout(timer); aviso = ""; }
      desenhar();
    }, erro);
    db.doc(DOC_AJ).onSnapshot((s) => {
      const c = s.exists ? s.data().capital : null;
      capital = ok(c) ? c : CAPITAL_PADRAO;
      desenhar();
    }, erro);
  }

  async function gravar(fn) {
    if (gravando) return false;
    gravando = true; desenharStatus();
    try { await fn(); return true; }
    catch (e) {
      if (e?.code === "invalid_argument" || e?.code === "not_granted") { podeEditar = false; aviso = "Esta visualização é só de leitura: a carteira só pode ser alterada pelo dono do sistema."; }
      else if (e?.code === "quota_exceeded") aviso = "O espaço da carteira está cheio. Remova posições antigas para incluir novas.";
      else aviso = "Não foi possível salvar agora. Tente de novo em instantes.";
      return false;
    } finally { gravando = false; desenhar(); }
  }

  // ---------- cálculo ----------
  function linhas() {
    return [...posicoes.values()].filter((p) => p && p.ticker).map((p) => {
      const a = acao(p.ticker);
      const cot = ok(a?.preco) ? a.preco : null;
      const custo = p.qtd * p.preco_entrada;
      const valor = ok(cot) ? p.qtd * cot : custo;
      const alvo = ok(p.preco_alvo) && p.preco_alvo > 0 ? p.preco_alvo : null;
      const ref = ok(cot) ? cot : p.preco_entrada;
      return {p, a, cot, custo, valor, alvo, res: valor - custo, resPct: custo > 0 ? (valor / custo - 1) * 100 : null,
        ate: alvo ? (alvo / ref - 1) * 100 : null, valorAlvo: alvo ? p.qtd * alvo : null, metodo: alvoMetodo(a)};
    }).sort((x, y) => y.valor - x.valor);
  }

  function totais(L) {
    const investido = L.reduce((t, l) => t + l.custo, 0), mercado = L.reduce((t, l) => t + l.valor, 0);
    const comAlvo = L.filter((l) => l.alvo);
    const baseAlvo = comAlvo.reduce((t, l) => t + l.valor, 0), noAlvo = comAlvo.reduce((t, l) => t + l.valorAlvo, 0);
    const caixa = capital - investido;
    return {investido, mercado, caixa, patrimonio: mercado + caixa, res: mercado - investido,
      resPct: investido > 0 ? (mercado / investido - 1) * 100 : null,
      potencial: baseAlvo > 0 ? (noAlvo / baseAlvo - 1) * 100 : null, potencialR: noAlvo - baseAlvo};
  }

  // ---------- desenho ----------
  function desenhar() {
    const sec = $("#carteira"); if (!sec || !BASE) return;
    const L = linhas(), T = totais(L);
    const cap = $("#cart-capital");
    if (cap && document.activeElement !== cap) cap.value = capital;
    if (cap) cap.disabled = !podeEditar || modo === "carregando";
    desenharResumo(L, T); desenharDist(L, T); desenharTabela(L, T); desenharStatus(); atualizarDica();
    $("#cart-form").hidden = !podeEditar;
  }

  function desenharResumo(L, T) {
    const cls = (v) => ok(v) ? (v >= 0 ? "pos-v" : "neg-v") : "";
    const cel = (lab, val, sub, c = "") => `<div><span class="lab">${lab}</span><span class="val ${c}">${val}</span>${sub ? `<span class="lab">${sub}</span>` : ""}</div>`;
    $("#cart-resumo").innerHTML =
      cel("Investido", brl(T.investido), `${L.length} ${L.length === 1 ? "ativo" : "ativos"} · ${capital > 0 ? nf(T.investido / capital * 100, 1) : "–"}% do capital`) +
      cel("Caixa livre", brl(T.caixa), T.caixa < 0 ? "acima do capital informado" : "para novas compras", T.caixa < 0 ? "neg-v" : "") +
      cel("Valor na cotação", brl(T.mercado), `resultado ${brl(T.res)} (${sinal(T.resPct)})`, "") +
      cel("Até os preços alvo", sinal(T.potencial, 0), ok(T.potencialR) && L.some((l) => l.alvo) ? `${brl(T.potencialR)} se todos chegarem ao alvo` : "defina os alvos", cls(T.potencial));
  }

  function desenharDist(L, T) {
    const box = $("#cart-dist");
    if (!L.length) { box.innerHTML = ""; return; }
    const tot = Math.max(T.patrimonio, T.mercado);
    const tons = [100, 80, 62, 90, 72, 54, 85, 67, 48, 76];
    const seg = L.map((l, i) => ({t: l.p.ticker, w: tot > 0 ? l.valor / tot * 100 : 0, cor: `color-mix(in srgb, var(--brass) ${tons[i % tons.length]}%, var(--surface))`}));
    if (T.caixa > 0 && tot > 0) seg.push({t: "Caixa", w: T.caixa / tot * 100, cor: "var(--track)"});
    box.innerHTML = `<div class="dist-barra" role="img" aria-label="Distribuição da carteira">${seg.map((s) => `<i style="flex:${s.w.toFixed(3)} 1 0;background:${s.cor}" title="${s.t}: ${nf(s.w, 1)}%"></i>`).join("")}</div>
      <ul class="dist-leg">${seg.map((s) => `<li><span class="sw" style="background:${s.cor}"></span>${s.t} <b>${nf(s.w, 1)}%</b></li>`).join("")}</ul>`;
  }

  function situacao(a) {
    if (!a) return `<span class="chip">fora da base</span>`;
    if (a.etapa === 4) {
      const d = a.descontoHist;
      return `<b>${a.posicao}º</b><span class="sub">${ok(d) ? (d > 0 ? "abaixo" : "acima") + " da média 5a" : "sem média"}</span>`;
    }
    const rot = a.etapa === "classe" ? "outra classe" : "saiu no passo " + a.etapa;
    return `<span class="chip alerta-chip" title="${esc((a.motivos || []).map((m) => m.texto).join("; "))}">${rot}</span>`;
  }

  function trajeto(l) {
    if (!l.alvo || !ok(l.cot) || l.alvo === l.p.preco_entrada) return "";
    const f = Math.max(0, Math.min(1, (l.cot - l.p.preco_entrada) / (l.alvo - l.p.preco_entrada)));
    return `<span class="traj" title="Caminho percorrido da entrada até o alvo: ${nf(f * 100, 0)}%"><i style="width:${(f * 100).toFixed(1)}%"></i></span>`;
  }

  function desenharTabela(L, T) {
    const tb = $("#tab-cart tbody");
    if (modo === "carregando") { tb.innerHTML = `<tr><td colspan="11" class="vazio esq">Abrindo a carteira…</td></tr>`; return; }
    if (!L.length) {
      tb.innerHTML = `<tr><td colspan="11" class="vazio esq"><p style="margin:0 0 10px">Nenhum ativo na carteira ainda. Adicione o primeiro no formulário abaixo${podeEditar ? ", ou comece pelas 8 melhores da peneira de hoje com o capital dividido em partes iguais" : ""}.</p>${podeEditar ? `<button type="button" class="botao" id="cart-sugerir">Montar com as 8 da peneira</button>` : ""}</td></tr>`;
      const b = $("#cart-sugerir"); if (b) b.onclick = sugerir;
      return;
    }
    const tot = Math.max(T.patrimonio, T.mercado);
    tb.innerHTML = L.map((l) => {
      const p = l.p, a = l.a, t = p.ticker;
      const acoes = !podeEditar ? "" : removendo === t
        ? `<button type="button" class="mini perigo" data-acao="confirmar" data-t="${t}">Remover ${t}</button><button type="button" class="mini" data-acao="manter">Manter</button>`
        : `<button type="button" class="mini" data-acao="editar" data-t="${t}">Editar</button><button type="button" class="mini" data-acao="remover" data-t="${t}">Remover</button>`;
      return `<tr data-cart="${t}">
        <td class="esq"><button type="button" class="tk-btn" data-acao="ficha" data-t="${t}"><span class="tk">${t}</span></button><span class="emp">${esc(a?.empresa || "")}</span>${p.nota ? `<span class="sub nota-pos">${esc(p.nota)}</span>` : ""}</td>
        <td class="esq">${a?.perfil ? `<span class="chip ${a.perfil.financeiro ? "fin" : ""}">${esc(a.perfil.nome.split(" (")[0])}</span>` : "–"}</td>
        <td>${nf(p.qtd, 0)}</td>
        <td>${brl(p.preco_entrada)}<span class="sub">${dataBR(p.data_entrada)}</span></td>
        <td>${brl(l.cot)}<span class="sub">${esc(a?.data_cotacao || "")}</span></td>
        <td>${brl(l.alvo)}${l.metodo ? `<span class="sub" title="Média dos preços em que ${l.metodo.partes.map((x) => x.k).join(" e ")} voltariam à média de 5 anos">método ${brl(l.metodo.v)}</span>` : ""}</td>
        <td class="${ok(l.ate) ? (l.ate >= 0 ? "pos-v" : "neg-v") : ""}">${sinal(l.ate, 0)}${trajeto(l)}</td>
        <td>${tot > 0 ? nf(l.valor / tot * 100, 1) + "%" : "–"}</td>
        <td>${brl(l.valor)}<span class="sub">custo ${brl(l.custo)}</span></td>
        <td class="${l.res > 0.005 ? "pos-v" : l.res < -0.005 ? "neg-v" : ""}">${brl(l.res)}<span class="sub">${sinal(l.resPct)}</span></td>
        <td>${situacao(a)}</td>
        <td class="esq acoes-cel">${acoes}</td></tr>`;
    }).join("");
  }

  function desenharStatus() {
    const s = $("#cart-status"); if (!s) return;
    const onde = modo === "db" ? "Salva no sistema: a mesma carteira aparece em qualquer aparelho em que você abrir esta página."
      : modo === "local" ? "Salva só neste navegador. No site publicado, a carteira fica guardada no sistema."
      : "Abrindo a carteira…";
    s.innerHTML = (aviso ? `<span class="alerta">${esc(aviso)}</span> ` : "") + (gravando ? "Salvando… " : "") + esc(onde) +
      (BASE ? ` Cotações de fechamento de ${esc(BASE.acoes.find((a) => a.data_cotacao)?.data_cotacao || "")}, coleta de ${dt(BASE.meta.fontes.precos)}.` : "");
  }

  // ---------- formulário ----------
  function montarForm() {
    const dl = $("#cart-tickers");
    dl.innerHTML = BASE.acoes.map((a) => `<option value="${a.ticker}">${esc(a.empresa)}</option>`).join("");
    $("#cart-data").value = hojeISO();
    $("#cart-ticker").addEventListener("input", () => { $("#cart-ticker").value = $("#cart-ticker").value.toUpperCase().trim(); preencherPeloTicker(false); });
    for (const id of ["cart-qtd", "cart-entrada", "cart-alvo"]) $("#" + id).addEventListener("input", atualizarDica);
    $("#cart-usar-cot").onclick = () => { const a = acao($("#cart-ticker").value); if (a?.preco) { $("#cart-entrada").value = a.preco.toFixed(2); atualizarDica(); } };
    $("#cart-usar-alvo").onclick = () => { const m = alvoMetodo(acao($("#cart-ticker").value)); if (m) { $("#cart-alvo").value = m.v.toFixed(2); atualizarDica(); } };
    $("#cart-cancelar").onclick = limparForm;
    $("#cart-form").addEventListener("submit", (e) => { e.preventDefault(); salvarForm(); });
    $("#cart-capital").addEventListener("change", () => {
      const v = Number($("#cart-capital").value);
      if (ok(v) && v >= 0 && v !== capital) gravar(() => Armazem.capital(v));
    });
    $("#tab-cart tbody").addEventListener("click", (e) => {
      const b = e.target.closest("button[data-acao]"); if (!b) return;
      const t = b.dataset.t, ac = b.dataset.acao;
      if (ac === "ficha") abrir(t);
      else if (ac === "editar") editar(t);
      else if (ac === "remover") { removendo = t; desenhar(); }
      else if (ac === "manter") { removendo = null; desenhar(); }
      else if (ac === "confirmar") { removendo = null; if (editando === t) limparForm(); gravar(() => Armazem.remover(t)); }
    });
  }

  function preencherPeloTicker(forcar) {
    const a = acao($("#cart-ticker").value);
    if (a && !editando) {
      if (forcar || !$("#cart-entrada").value) $("#cart-entrada").value = ok(a.preco) ? a.preco.toFixed(2) : "";
      const m = alvoMetodo(a);
      if (forcar || !$("#cart-alvo").value) $("#cart-alvo").value = m ? m.v.toFixed(2) : "";
    }
    atualizarDica();
  }

  function atualizarDica() {
    const el = $("#cart-dica"); if (!el || !BASE) return;
    const t = $("#cart-ticker").value, a = acao(t);
    $("#cart-usar-cot").disabled = !a?.preco; $("#cart-usar-alvo").disabled = !alvoMetodo(a);
    if (!t) { el.textContent = "Escolha um ticker da base para ver a cotação e o alvo do método."; return; }
    if (!a) { el.innerHTML = `<span class="alerta">${esc(t)} não está na base da peneira. Use um ticker da lista.</span>`; return; }
    const m = alvoMetodo(a), L = linhas(), T = totais(L);
    const ent = Number($("#cart-entrada").value), q = Number($("#cart-qtd").value), alvo = Number($("#cart-alvo").value);
    const ja = posicoes.get(t);
    const livre = T.caixa + (editando === t && ja ? ja.qtd * ja.preco_entrada : 0);
    const cabe = ent > 0 ? Math.floor(Math.max(0, livre) / ent) : null;
    const partes = [
      `${esc(a.empresa)} · cotação ${brl(a.preco)} em ${esc(a.data_cotacao || "")}`,
      m ? `alvo do método ${brl(m.v)} (${m.partes.map((x) => `${x.k} ${brl(x.v)}`).join(", ")})` : "sem histórico suficiente para o alvo do método",
      a.etapa === 4 ? `${a.posicao}º na peneira hoje` : `fora do ranking hoje (${a.etapa === "classe" ? "outra classe" : "passo " + a.etapa})`,
    ];
    if (q > 0 && ent > 0) partes.push(`total ${brl(q * ent)}${alvo > 0 ? `, ${sinal((alvo / ent - 1) * 100, 0)} até o alvo` : ""}`);
    if (cabe !== null) partes.push(`o caixa livre (${brl(livre)}) compra até ${nf(cabe, 0)} ações`);
    if (ja && !editando) partes.push(`já está na carteira com ${nf(ja.qtd, 0)} ações: a compra soma e recalcula o preço médio`);
    el.innerHTML = partes.join(" · ");
  }

  function editar(t) {
    const p = posicoes.get(t); if (!p) return;
    editando = t;
    $("#cart-ticker").value = t; $("#cart-ticker").readOnly = true;
    $("#cart-qtd").value = p.qtd; $("#cart-entrada").value = p.preco_entrada;
    $("#cart-alvo").value = ok(p.preco_alvo) ? p.preco_alvo : ""; $("#cart-data").value = p.data_entrada || "";
    $("#cart-nota").value = p.nota || "";
    $("#cart-salvar").textContent = `Salvar ${t}`; $("#cart-cancelar").hidden = false;
    $("#cart-form-tit").textContent = `Editar ${t}`;
    atualizarDica();
    $("#cart-form").scrollIntoView({behavior: "smooth", block: "nearest"}); $("#cart-qtd").focus();
  }

  function limparForm() {
    editando = null;
    $("#cart-form").reset(); $("#cart-ticker").readOnly = false; $("#cart-data").value = hojeISO();
    $("#cart-salvar").textContent = "Adicionar à carteira"; $("#cart-cancelar").hidden = true;
    $("#cart-form-tit").textContent = "Adicionar ativo";
    $("#cart-erro").textContent = "";
    atualizarDica();
  }

  async function salvarForm() {
    const t = $("#cart-ticker").value.toUpperCase().trim(), a = acao(t);
    const qtd = Math.round(Number($("#cart-qtd").value)), ent = Number($("#cart-entrada").value);
    const alvoTxt = $("#cart-alvo").value, alvo = alvoTxt === "" ? null : Number(alvoTxt);
    const erro = !a ? "Escolha um ticker que esteja na base da peneira."
      : !(qtd > 0) ? "Informe a quantidade de ações (número inteiro maior que zero)."
      : !(ent > 0) ? "Informe o preço de entrada."
      : alvo !== null && !(alvo > 0) ? "O preço alvo precisa ser maior que zero, ou fique em branco."
      : "";
    $("#cart-erro").textContent = erro;
    if (erro) return;
    const ja = posicoes.get(t);
    let corpo = {ticker: t, qtd, preco_entrada: +ent.toFixed(4), data_entrada: $("#cart-data").value || hojeISO(),
      preco_alvo: alvo === null ? null : +alvo.toFixed(2), nota: $("#cart-nota").value.trim(), atualizado: new Date().toISOString()};
    if (ja && editando !== t) {
      const q2 = ja.qtd + qtd;
      corpo = {...corpo, qtd: q2, preco_entrada: +((ja.qtd * ja.preco_entrada + qtd * ent) / q2).toFixed(4),
        data_entrada: [ja.data_entrada, corpo.data_entrada].filter(Boolean).sort()[0], nota: corpo.nota || ja.nota || "",
        preco_alvo: corpo.preco_alvo ?? ja.preco_alvo ?? null};
    }
    if (await gravar(() => Armazem.salvar(t, corpo))) limparForm();
  }

  // Monta 8 posições com as primeiras da peneira que estão abaixo da média de 5 anos,
  // no máximo 2 por setor, capital dividido em partes iguais e lotes fracionários.
  async function sugerir() {
    const escolhidas = [], porSetor = {};
    for (const a of R.ranqueadas) {
      if (!(ok(a.descontoHist) && a.descontoHist > 0 && a.anosHist >= 5 && a.preco > 0)) continue;
      if ((porSetor[a.perfil.id] || 0) >= 2) continue;
      porSetor[a.perfil.id] = (porSetor[a.perfil.id] || 0) + 1; escolhidas.push(a);
      if (escolhidas.length === 8) break;
    }
    const parte = capital / Math.max(1, escolhidas.length);
    await gravar(async () => {
      for (const a of escolhidas) {
        const q = Math.floor(parte / a.preco); if (q < 1) continue;
        const m = alvoMetodo(a);
        await Armazem.salvar(a.ticker, {ticker: a.ticker, qtd: q, preco_entrada: a.preco, data_entrada: isoDeBR(a.data_cotacao) || hojeISO(),
          preco_alvo: m ? +m.v.toFixed(2) : null, nota: `${a.posicao}º na peneira ao montar`, atualizado: new Date().toISOString()});
      }
    });
  }

  // Chamado pela ficha da ação: leva o ticker para o formulário.
  function preparar(t) {
    fechar(); trocarAba("carteira");
    if (!podeEditar) return;
    limparForm(); $("#cart-ticker").value = t; preencherPeloTicker(true);
    $("#cart-form").scrollIntoView({behavior: "smooth", block: "nearest"}); $("#cart-qtd").focus();
  }

  return {iniciar, desenhar, preparar, alvoMetodo, tem: (t) => posicoes.has(t)};
})();
