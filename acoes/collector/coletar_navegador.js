/*
 * Coletor de navegador.
 *
 * Por que existe: o Status Invest bloqueia chamadas de servidor (Cloudflare, HTTP 403)
 * e o endpoint de cotações do Fundamentus devolve corpo vazio fora de uma sessão de
 * navegador. As duas fontes respondem normalmente quando a chamada parte de uma aba
 * aberta no próprio site. Este arquivo tem duas rotinas para colar no console (F12)
 * ou rodar via Claude in Chrome; cada uma gera um JSON e oferece o download.
 *
 * 1) Em https://statusinvest.com.br/acoes/busca-avancada  -> coletarStatusInvest()
 *    Gera statusinvest_navegador.json  (universo + histórico anual + cotações 5 anos).
 * 2) Em https://www.fundamentus.com.br/resultado.php      -> coletarCotacoesFundamentus(tickers)
 *    Gera cotacoes_fundamentus.json     (fechamento diário ajustado, ~10 anos).
 *
 * Coloque os dois arquivos em data/raw/ e rode:
 *    python collector/coletar_direto.py   (CVM + fichas do Fundamentus, direto do servidor)
 *    python collector/montar_base.py
 *    python site/montar_site.py
 *
 * Endpoints (não oficiais, sujeitos a mudança):
 *   GET  /category/advancedsearchresultpaginated?search={}&page=0&take=3000&CategoryType=1
 *   POST /acao/indicatorhistoricallist   codes[]=TICKER&time=7&byQuarter=false&futureData=false
 *        (aceita vários codes[], mas só responde o primeiro: chamar um a um)
 *   GET  /acao/tickerprice?ticker=TICKER&type=4&currences[]=1   (5 anos diários, SEM ajuste)
 *   GET  https://www.fundamentus.com.br/amline/cot_hist.php?papel=TICKER  (ajustado; limita taxa)
 */

const espera = (ms) => new Promise((r) => setTimeout(r, ms));

function baixarJSON(obj, nome) {
  // Botão visível: o Chrome bloqueia vários downloads automáticos seguidos,
  // mas um clique de verdade sempre passa.
  const blob = new Blob([JSON.stringify(obj)], { type: "application/json" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = nome;
  a.textContent = "BAIXAR " + nome;
  a.style.cssText = "position:fixed;top:20px;left:20px;z-index:999999;background:#c00;color:#fff;font:bold 22px sans-serif;padding:24px";
  document.body.appendChild(a);
  return a;
}

async function coletarStatusInvest({ liquidezMin = 5e5, pausa = 250 } = {}) {
  const uni = (await (await fetch("/category/advancedsearchresultpaginated?search=%7B%7D&orderColumn=&isAsc=&page=0&take=3000&CategoryType=1")).json()).list;
  const out = { fonte: "statusinvest.com.br", coletado_em: new Date().toISOString(), universo: uni, historico: {}, precos: {}, erros: {} };
  const alvo = uni.filter((x) => (x.liquidezmediadiaria || 0) >= liquidezMin).map((x) => x.ticker);
  for (const c of alvo) {
    const fd = new FormData();
    fd.append("codes[]", c); fd.append("time", "7"); fd.append("byQuarter", "false"); fd.append("futureData", "false");
    try {
      const j = await (await fetch("/acao/indicatorhistoricallist", { method: "POST", body: fd })).json();
      const arr = Object.values(j.data || {})[0] || [];
      const o = {};
      for (const ind of arr) o[ind.key] = (ind.ranks || []).map((r) => [r.rank, r.timeType, r.value]);
      out.historico[c] = o;
    } catch (e) { out.erros["hist:" + c] = e.message; }
    await espera(pausa);
  }
  console.log("Status Invest:", Object.keys(out.historico).length, "históricos");
  return baixarJSON(out, "statusinvest_navegador.json");
}

async function coletarCotacoesFundamentus(tickers, { pausa = 1800 } = {}) {
  const out = { fonte: "fundamentus.com.br/amline/cot_hist.php (fechamento ajustado)", coletado_em: new Date().toISOString(), dados: {}, erros: {} };
  for (const p of tickers) {
    let ok = false;
    for (let k = 0; k < 3 && !ok; k++) {
      try {
        const t = await (await fetch("/amline/cot_hist.php?papel=" + p)).text();
        if (t.length > 10) {
          // [dias desde 1970, preço] dos últimos ~10 anos
          out.dados[p] = JSON.parse(t).slice(-2600).map((x) => [Math.round(x[0] / 864e5), x[1]]);
          ok = true;
        } else await espera(6000 * (k + 1)); // corpo vazio = limite de taxa
      } catch (e) { out.erros[p] = e.message; }
    }
    if (!ok) out.erros[p] = out.erros[p] || "vazio";
    await espera(pausa);
  }
  console.log("Fundamentus:", Object.keys(out.dados).length, "séries");
  return baixarJSON(out, "cotacoes_fundamentus.json");
}

if (typeof module === "object" && module.exports) module.exports = { coletarStatusInvest, coletarCotacoesFundamentus };
