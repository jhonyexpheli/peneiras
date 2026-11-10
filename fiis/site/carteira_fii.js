/*
 * Aba Carteira da Peneira FIIs: posições em fundos com quantidade de cotas, preço de
 * entrada, data e preço alvo. Separada da carteira de ações da Peneira de Valor.
 *
 * Onde fica salvo:
 *  - publicado como Artifact: banco do artifact (capability `db`), coleção
 *    `carteira_fii` (um documento por ticker) e documento `ajustes/carteira_fii` (capital);
 *  - fora do Artifact (site estático): localStorage deste navegador (`peneira-fii-carteira-v1`).
 * No site real, troque `Armazem` por chamadas à API própria mantendo a forma dos documentos:
 * {ticker, qtd, preco_entrada, data_entrada, preco_alvo, nota, atualizado}.
 *
 * Usa da interface: $, ok, nf, esc, R, BASE, abrir, fechar, trocarAba (no momento da chamada).
 */
const Carteira = (() => {
  "use strict";
  const COL = "carteira_fii", DOC_AJ = "ajustes/carteira_fii", LS = "peneira-fii-carteira-v1";
  const CAPITAL_PADRAO = 10000;
  let modo = "carregando";
  let db = null, podeEditar = true, aviso = "", timer = null, iniciado = false;
  let posicoes = new Map(), capital = CAPITAL_PADRAO;
  let editando = null, removendo = null, gravando = false, confirmandoMontar = false;

  const brl = (v, d = 2) => ok(v) ? (v < 0 ? "−" : "") + "R$ " + nf(Math.abs(v), d) : "–";
  const sinal = (v, d = 1) => ok(v) ? (v > 0 ? "+" : v < 0 ? "−" : "") + nf(Math.abs(v), d) + "%" : "–";
  const hojeISO = () => { const d = new Date(); return new Date(d - d.getTimezoneOffset() * 6e4).toISOString().slice(0, 10); };
  const dataBR = (iso) => iso ? iso.split("-").reverse().join("/") : "";
  const fundo = (t) => (R?.fundos || []).find((f) => f.ticker === t);
  const alvoMetodo = (f) => f && f.alvo ? f.alvo : null;

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
      if (modo === "db") { await db.doc(DOC_AJ).set({ capital: v, atualizado: new Date().toISOString() }); return; }
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
    try { localStorage.setItem(LS, JSON.stringify({ capital, posicoes: Object.fromEntries(posicoes) })); } catch (e) {}
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
      const f = fundo(p.ticker);
      const cot = ok(f?.preco) ? f.preco : null;
      const custo = p.qtd * p.preco_entrada;
      const valor = ok(cot) ? p.qtd * cot : custo;
      const alvo = ok(p.preco_alvo) && p.preco_alvo > 0 ? p.preco_alvo : null;
      const ref = ok(cot) ? cot : p.preco_entrada;
      const rendCota = ok(f?.dy_12m) && ok(f?.preco) ? f.dy_12m / 100 * f.preco : null; // rendimento por cota em 12m
      return {
        p, f, cot, custo, valor, alvo, res: valor - custo, resPct: custo > 0 ? (valor / custo - 1) * 100 : null,
        ate: alvo ? (alvo / ref - 1) * 100 : null, valorAlvo: alvo ? p.qtd * alvo : null, metodo: alvoMetodo(f),
        rendMes: ok(rendCota) ? p.qtd * rendCota / 12 : null, yoc: ok(rendCota) && p.preco_entrada > 0 ? rendCota / p.preco_entrada * 100 : null,
      };
    }).sort((x, y) => y.valor - x.valor);
  }

  function totais(L) {
    const investido = L.reduce((t, l) => t + l.custo, 0), mercado = L.reduce((t, l) => t + l.valor, 0);
    const comAlvo = L.filter((l) => l.alvo);
    const baseAlvo = comAlvo.reduce((t, l) => t + l.valor, 0), noAlvo = comAlvo.reduce((t, l) => t + l.valorAlvo, 0);
    const rendMes = L.reduce((t, l) => t + (l.rendMes || 0), 0);
    const caixa = capital - investido;
    return {
      investido, mercado, caixa, patrimonio: mercado + caixa, res: mercado - investido, rendMes,
      resPct: investido > 0 ? (mercado / investido - 1) * 100 : null,
      potencial: baseAlvo > 0 ? (noAlvo / baseAlvo - 1) * 100 : null, potencialR: noAlvo - baseAlvo,
    };
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
    const cel = (lab, val, sub, c = "") => `<div><span class="lab">${lab}</span><span class="val ${c}">${val}</span>${sub ? `<span class="lab sub-lab">${sub}</span>` : ""}</div>`;
    $("#cart-resumo").innerHTML =
      cel("Investido", brl(T.investido), `${L.length} ${L.length === 1 ? "fundo" : "fundos"} · ${capital > 0 ? nf(T.investido / capital * 100, 1) : "–"}% do capital`) +
      cel("Caixa livre", brl(T.caixa), T.caixa < 0 ? "acima do capital informado" : "para novas compras", T.caixa < 0 ? "neg-v" : "") +
      cel("Valor na cotação", brl(T.mercado), `resultado ${brl(T.res)} (${sinal(T.resPct)})`) +
      cel("Rendimento estimado", brl(T.rendMes) + "<small>/mês</small>", "pelo rendimento dos últimos 12 meses") +
      cel("Até os preços alvo", sinal(T.potencial, 0), ok(T.potencialR) && L.some((l) => l.alvo) ? `${brl(T.potencialR)} se todos chegarem ao alvo` : "defina os alvos", cls(T.potencial));
  }

  function desenharDist(L, T) {
    const box = $("#cart-dist");
    if (!L.length) { box.innerHTML = ""; return; }
    const tot = Math.max(T.patrimonio, T.mercado);
    const porGrupo = {};
    for (const l of L) { const g = l.f?.grupo || "fora"; porGrupo[g] = (porGrupo[g] || 0) + l.valor; }
    const nomes = { tijolo: "Tijolo", papel: "Papel", fof: "FOF", fora: "Fora da base" };
    const seg = Object.entries(porGrupo).map(([g, v]) => ({ t: nomes[g], w: tot > 0 ? v / tot * 100 : 0, cor: `var(--g-${g in nomes && g !== "fora" ? g : "outros"})` }));
    if (T.caixa > 0 && tot > 0) seg.push({ t: "Caixa", w: T.caixa / tot * 100, cor: "var(--line)" });
    box.innerHTML = `<div class="dist-barra" role="img" aria-label="Carteira por grupo">${seg.map((s) => `<i style="flex:${s.w.toFixed(3)} 1 0;background:${s.cor}" title="${s.t}: ${nf(s.w, 1)}%"></i>`).join("")}</div>
      <ul class="dist-leg">${seg.map((s) => `<li><span class="sw" style="background:${s.cor}"></span>${s.t} <b>${nf(s.w, 1)}%</b></li>`).join("")}</ul>`;
  }

  function situacao(f) {
    if (!f) return `<span class="chip">fora da base</span>`;
    if (f.etapa === 4) {
      const d = f.descontoHist;
      return `<b>${f.posicao}º</b> <span class="sub">${GRUPO_NOME[f.grupo]}, ${ok(d) ? (d > 0 ? "abaixo" : "acima") + " da média 5a" : "sem média"}</span>`;
    }
    return `<span class="chip chip-alerta" title="${esc((f.motivos || []).map((m) => m.texto).join("; "))}">saiu no passo ${f.etapa}</span>`;
  }

  function desenharTabela(L) {
    const tb = $("#tab-cart tbody");
    if (modo === "carregando") { tb.innerHTML = `<tr><td colspan="10" class="vazio">Abrindo a carteira…</td></tr>`; return; }
    if (!L.length) {
      tb.innerHTML = `<tr><td colspan="10" class="vazio"><p>Nenhum fundo na carteira ainda. Adicione o primeiro no formulário abaixo${podeEditar ? ", ou monte uma carteira com os 10 primeiros da peneira, respeitando os tetos por segmento" : ""}.</p>${podeEditar ? `<button type="button" class="botao" id="cart-sugerir">Montar com 10 da peneira</button>` : ""}</td></tr>`;
      const b = $("#cart-sugerir"); if (b) b.onclick = () => sugerir();
      return;
    }
    tb.innerHTML = L.map((l) => {
      const p = l.p, f = l.f, t = p.ticker;
      const acoes = !podeEditar ? "" : removendo === t
        ? `<button type="button" class="mini perigo" data-acao="confirmar" data-t="${t}">Remover ${t}</button><button type="button" class="mini" data-acao="manter">Manter</button>`
        : `<button type="button" class="mini" data-acao="editar" data-t="${t}">Editar</button><button type="button" class="mini" data-acao="remover" data-t="${t}">Remover</button>`;
      return `<tr>
        <td class="esq"><button type="button" class="tk-btn" data-acao="ficha" data-t="${t}">${t}</button><span class="emp">${esc(nomeCurto(f?.nome || ""))}</span>${p.nota ? `<span class="sub">${esc(p.nota)}</span>` : ""}</td>
        <td>${nf(p.qtd, 0)}</td>
        <td>${brl(p.preco_entrada)}<span class="sub">${dataBR(p.data_entrada)}</span></td>
        <td>${brl(l.cot)}</td>
        <td>${brl(l.alvo)}${l.metodo ? `<span class="sub">método ${brl(l.metodo.v)}</span>` : ""}</td>
        <td class="${ok(l.ate) ? (l.ate >= 0 ? "pos-v" : "neg-v") : ""}">${sinal(l.ate, 0)}</td>
        <td>${brl(l.valor)}<span class="sub">custo ${brl(l.custo)}</span></td>
        <td class="${l.res > 0.005 ? "pos-v" : l.res < -0.005 ? "neg-v" : ""}">${brl(l.res)}<span class="sub">${sinal(l.resPct)}</span></td>
        <td>${brl(l.rendMes)}<span class="sub">yield on cost ${ok(l.yoc) ? nf(l.yoc, 1) + "%" : "–"}</span></td>
        <td class="esq">${situacao(f)}<div class="acoes-cel">${acoes}</div></td></tr>`;
    }).join("");
  }

  function desenharStatus() {
    const s = $("#cart-status"); if (!s) return;
    const onde = modo === "db" ? "Salva no sistema: a mesma carteira aparece em qualquer aparelho em que você abrir esta página. É separada da carteira de ações."
      : modo === "local" ? "Salva só neste navegador. Na página publicada, a carteira fica guardada no sistema."
      : "Abrindo a carteira…";
    s.innerHTML = (aviso ? `<span class="alerta">${esc(aviso)}</span> ` : "") + (gravando ? "Salvando… " : "") + esc(onde);
  }

  // ---------- formulário ----------
  function montarForm() {
    $("#cart-tickers").innerHTML = BASE.fundos.filter((f) => (f.liquidez || 0) > 0).map((f) => `<option value="${f.ticker}">${esc(nomeCurto(f.nome || ""))}</option>`).join("");
    $("#cart-data").value = hojeISO();
    $("#cart-ticker").addEventListener("input", () => { $("#cart-ticker").value = $("#cart-ticker").value.toUpperCase().trim(); preencherPeloTicker(false); });
    for (const id of ["cart-qtd", "cart-entrada", "cart-alvo"]) $("#" + id).addEventListener("input", atualizarDica);
    $("#cart-usar-cot").onclick = () => { const f = fundo($("#cart-ticker").value); if (f?.preco) { $("#cart-entrada").value = f.preco.toFixed(2); atualizarDica(); } };
    $("#cart-usar-alvo").onclick = () => { const m = alvoMetodo(fundo($("#cart-ticker").value)); if (m) { $("#cart-alvo").value = m.v.toFixed(2); atualizarDica(); } };
    $("#cart-cancelar").onclick = limparForm;
    $("#cart-form").addEventListener("submit", (e) => { e.preventDefault(); salvarForm(); });
    $("#cart-capital").addEventListener("change", () => {
      const v = Number($("#cart-capital").value);
      if (ok(v) && v >= 0 && v !== capital) gravar(() => Armazem.capital(v));
    });
    $("#cart-montar").onclick = () => { confirmandoMontar = true; desenharMontar(); };
    $("#tab-cart tbody").addEventListener("click", (e) => {
      const b = e.target.closest("button[data-acao]"); if (!b) return;
      const t = b.dataset.t, ac = b.dataset.acao;
      if (ac === "ficha") abrir(t);
      else if (ac === "editar") editar(t);
      else if (ac === "remover") { removendo = t; desenhar(); }
      else if (ac === "manter") { removendo = null; desenhar(); }
      else if (ac === "confirmar") { removendo = null; if (editando === t) limparForm(); gravar(() => Armazem.remover(t)); }
    });
    desenharMontar();
  }

  function desenharMontar() {
    const box = $("#cart-montar-conf"), b = $("#cart-montar");
    if (!box) return;
    b.hidden = !podeEditar || confirmandoMontar;
    box.hidden = !confirmandoMontar;
    if (!confirmandoMontar) return;
    const sel = escolher();
    box.innerHTML = `<p>Substituir as posições atuais por ${sel.length} fundos (${sel.map((f) => f.ticker).join(", ")}), com o capital de ${brl(capital)} em partes iguais?</p>
      <button type="button" class="botao" id="cart-montar-sim">Substituir carteira</button> <button type="button" class="mini" id="cart-montar-nao">Cancelar</button>`;
    $("#cart-montar-nao").onclick = () => { confirmandoMontar = false; desenharMontar(); };
    $("#cart-montar-sim").onclick = async () => { confirmandoMontar = false; desenharMontar(); await sugerir(true); };
  }

  function preencherPeloTicker(forcar) {
    const f = fundo($("#cart-ticker").value);
    if (f && !editando) {
      if (forcar || !$("#cart-entrada").value) $("#cart-entrada").value = ok(f.preco) ? f.preco.toFixed(2) : "";
      const m = alvoMetodo(f);
      if (forcar || !$("#cart-alvo").value) $("#cart-alvo").value = m ? m.v.toFixed(2) : "";
    }
    atualizarDica();
  }

  function atualizarDica() {
    const el = $("#cart-dica"); if (!el || !BASE) return;
    const t = $("#cart-ticker").value, f = fundo(t);
    $("#cart-usar-cot").disabled = !f?.preco; $("#cart-usar-alvo").disabled = !alvoMetodo(f);
    if (!t) { el.textContent = "Escolha um fundo da base para ver a cotação e o alvo do método."; return; }
    if (!f) { el.innerHTML = `<span class="alerta">${esc(t)} não está na base. Use um ticker da lista.</span>`; return; }
    const m = alvoMetodo(f), T = totais(linhas());
    const ent = Number($("#cart-entrada").value), q = Number($("#cart-qtd").value), alvo = Number($("#cart-alvo").value);
    const ja = posicoes.get(t);
    const livre = T.caixa + (editando === t && ja ? ja.qtd * ja.preco_entrada : 0);
    const cabe = ent > 0 ? Math.floor(Math.max(0, livre) / ent) : null;
    const partes = [
      `${esc(nomeCurto(f.nome || ""))} · cotação ${brl(f.preco)}`,
      m ? `alvo do método ${brl(m.v)} (${m.partes.map((x) => `${x.k} ${brl(x.v)}`).join(", ")})` : "sem histórico suficiente para o alvo do método",
      f.etapa === 4 ? `${f.posicao}º do grupo ${GRUPO_NOME[f.grupo]}` : `fora do ranking hoje (passo ${f.etapa})`,
    ];
    if (q > 0 && ent > 0) partes.push(`total ${brl(q * ent)}${alvo > 0 ? `, ${sinal((alvo / ent - 1) * 100, 0)} até o alvo` : ""}`);
    if (cabe !== null) partes.push(`o caixa livre (${brl(livre)}) compra até ${nf(cabe, 0)} cotas`);
    if (ja && !editando) partes.push(`já está na carteira com ${nf(ja.qtd, 0)} cotas: a compra soma e recalcula o preço médio`);
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
    $("#cart-form").scrollIntoView({ behavior: "smooth", block: "nearest" }); $("#cart-qtd").focus();
  }

  function limparForm() {
    editando = null;
    $("#cart-form").reset(); $("#cart-ticker").readOnly = false; $("#cart-data").value = hojeISO();
    $("#cart-salvar").textContent = "Adicionar à carteira"; $("#cart-cancelar").hidden = true;
    $("#cart-form-tit").textContent = "Adicionar fundo";
    $("#cart-erro").textContent = "";
    atualizarDica();
  }

  async function salvarForm() {
    const t = $("#cart-ticker").value.toUpperCase().trim(), f = fundo(t);
    const qtd = Math.round(Number($("#cart-qtd").value)), ent = Number($("#cart-entrada").value);
    const alvoTxt = $("#cart-alvo").value, alvo = alvoTxt === "" ? null : Number(alvoTxt);
    const erro = !f ? "Escolha um fundo que esteja na base."
      : !(qtd > 0) ? "Informe a quantidade de cotas (número inteiro maior que zero)."
      : !(ent > 0) ? "Informe o preço de entrada."
      : alvo !== null && !(alvo > 0) ? "O preço alvo precisa ser maior que zero, ou fique em branco."
      : "";
    $("#cart-erro").textContent = erro;
    if (erro) return;
    const ja = posicoes.get(t);
    let corpo = {
      ticker: t, qtd, preco_entrada: +ent.toFixed(4), data_entrada: $("#cart-data").value || hojeISO(),
      preco_alvo: alvo === null ? null : +alvo.toFixed(2), nota: $("#cart-nota").value.trim(), atualizado: new Date().toISOString(),
    };
    if (ja && editando !== t) {
      const q2 = ja.qtd + qtd;
      corpo = {
        ...corpo, qtd: q2, preco_entrada: +((ja.qtd * ja.preco_entrada + qtd * ent) / q2).toFixed(4),
        data_entrada: [ja.data_entrada, corpo.data_entrada].filter(Boolean).sort()[0], nota: corpo.nota || ja.nota || "",
        preco_alvo: corpo.preco_alvo ?? ja.preco_alvo ?? null,
      };
    }
    if (await gravar(() => Armazem.salvar(t, corpo))) limparForm();
  }

  // Os N primeiros da peneira (índice dentro do grupo, intercalando grupos pelo índice),
  // preferindo os abaixo da média de 5 anos, com tetos por subtipo de tijolo e para papel.
  function escolher() {
    const cfg = (BASE.criterios && BASE.criterios.carteira) || {};
    const N = cfg.fundos || 10;
    const tetoSub = Math.max(1, Math.floor(N * (cfg.teto_subtipo_tijolo_pct ?? 30) / 100));
    const tetoPapel = Math.max(1, Math.floor(N * (cfg.teto_papel_pct ?? 40) / 100));
    const sel = [], cont = {};
    const ordem = [...R.ranqueados].sort((a, b) => ((b.descontoHist > 0) - (a.descontoHist > 0)) || (b.indice - a.indice));
    for (const f of ordem) {
      if (!(f.preco > 0)) continue;
      const chave = f.grupo === "tijolo" ? "tijolo:" + (f.subtipo?.id || "outros") : f.grupo;
      const teto = f.grupo === "papel" ? tetoPapel : tetoSub;
      if ((cont[chave] || 0) >= teto) continue;
      cont[chave] = (cont[chave] || 0) + 1; sel.push(f);
      if (sel.length === N) break;
    }
    return sel;
  }

  async function sugerir(substituir) {
    const sel = escolher();
    const parte = capital / Math.max(1, sel.length);
    await gravar(async () => {
      if (substituir) for (const t of [...posicoes.keys()]) if (!sel.some((f) => f.ticker === t)) await Armazem.remover(t);
      for (const f of sel) {
        const q = Math.floor(parte / f.preco); if (q < 1) continue;
        const m = alvoMetodo(f);
        await Armazem.salvar(f.ticker, {
          ticker: f.ticker, qtd: q, preco_entrada: f.preco, data_entrada: f.data_preco || hojeISO(),
          preco_alvo: m ? +m.v.toFixed(2) : null, nota: `${f.posicao}º do grupo ${GRUPO_NOME[f.grupo]} ao montar`, atualizado: new Date().toISOString(),
        });
      }
    });
  }

  // Chamado pela ficha: leva o ticker para o formulário.
  function preparar(t) {
    fechar(); trocarAba("carteira");
    if (!podeEditar) return;
    limparForm(); $("#cart-ticker").value = t; preencherPeloTicker(true);
    $("#cart-form").scrollIntoView({ behavior: "smooth", block: "nearest" }); $("#cart-qtd").focus();
  }

  return { iniciar, desenhar, preparar, tem: (t) => posicoes.has(t) };
})();
