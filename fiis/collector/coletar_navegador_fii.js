/*
 * Coleta pelo navegador (Status Invest e Yahoo Finance respondem 403 ou exigem
 * sessão de navegador quando chamados do servidor).
 *
 * Como usar:
 *  1) Abra https://statusinvest.com.br/fundos-imobiliarios/busca-avancada,
 *     cole no console a função `coletarStatusInvest` e rode
 *        await coletarStatusInvest(TICKERS)
 *     Ela devolve {universo, proventos} e baixa statusinvest_fii.json.
 *  2) Abra https://query1.finance.yahoo.com/v8/finance/chart/HGLG11.SA (qualquer
 *     ticker; é só para estar no domínio), cole `coletarYahoo` e rode
 *        await coletarYahoo(TICKERS)
 *     Ela baixa yahoo_fii.json.
 *  3) Salve os dois arquivos em data/raw/ e rode collector/montar_base_fii.py.
 *
 * TICKERS = lista dos fundos com liquidez mínima (sai de data/raw/fundamentus_fii_resultado.json).
 * No site real, essas duas fontes devem ser trocadas por uma API com contrato
 * (B3, brapi com token ou base própria), mantendo o mesmo formato de saída.
 */

const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

function baixar(nome, obj) {
  const a = document.createElement("a");
  a.href = URL.createObjectURL(new Blob([JSON.stringify(obj)], { type: "application/json" }));
  a.download = nome;
  a.click();
}

// Status Invest: universo de FIIs (setor, cotistas, liquidez) e rendimentos por cota.
async function coletarStatusInvest(TICKERS, pausaMs = 600) {
  const h = { "X-Requested-With": "XMLHttpRequest" };
  const u = await fetch("/category/advancedsearchresultpaginated?search=%7B%7D&orderColumn=&isAsc=&page=0&take=3000&CategoryType=2", { headers: h }).then((r) => r.json());
  const proventos = {};
  for (let rodada = 0; rodada < 3; rodada++) {
    for (const t of TICKERS) {
      if (proventos[t] && proventos[t] !== "erro") continue;
      try {
        const d = await fetch(`/fii/companytickerprovents?ticker=${t}&chartProventsType=2`, { headers: h }).then((r) => r.json());
        // [data com, data de pagamento, valor por cota, tipo]
        proventos[t] = (d.assetEarningsModels || []).map((e) => [e.ed, e.pd, e.v, e.et]);
      } catch (e) {
        proventos[t] = "erro";
      }
      await esperar(pausaMs);
    }
  }
  const out = { coletado: new Date().toISOString(), universo: u.list, proventos };
  baixar("statusinvest_fii.json", out);
  return out;
}

// Yahoo: fechamento sem ajuste por proventos (mensal 10 anos -> fechamento de dezembro de
// cada ano; diário 2 anos -> volatilidade de 1 ano, drawdown e fechamentos mensais).
async function coletarYahoo(TICKERS, pausaMs = 150) {
  const out = {};
  for (const t of TICKERS) {
    try {
      const m = await fetch(`/v8/finance/chart/${t}.SA?range=10y&interval=1mo`).then((r) => r.json());
      const r = m.chart.result[0];
      const q = r.indicators.quote[0].close;
      const ye = {};
      (r.timestamp || []).forEach((s, i) => {
        if (q[i] == null) return;
        const d = new Date(s * 1000);
        if (d.getUTCMonth() === 11) ye[d.getUTCFullYear()] = +q[i].toFixed(4);
      });
      const prim = r.timestamp && r.timestamp.length ? new Date(r.timestamp[0] * 1000).toISOString().slice(0, 10) : null;
      const dd = await fetch(`/v8/finance/chart/${t}.SA?range=2y&interval=1d`).then((x) => x.json());
      const r2 = dd.chart.result[0];
      const c = r2.indicators.quote[0].close;
      const px = [];
      (r2.timestamp || []).forEach((s, i) => { if (c[i] != null && c[i] > 0) px.push([s, c[i]]); });
      const ult = px.slice(-253);
      const rets = [];
      let saltos = 0;
      for (let i = 1; i < ult.length; i++) {
        const x = Math.log(ult[i][1] / ult[i - 1][1]);
        if (Math.abs(x) > 0.25) { saltos++; continue; } // evento (desdobramento, falha de dado)
        rets.push(x);
      }
      const media = rets.reduce((a, b) => a + b, 0) / rets.length;
      const dp = Math.sqrt(rets.reduce((a, b) => a + (b - media) ** 2, 0) / (rets.length - 1));
      let pico = -1, mdd = 0;
      for (const [, v] of ult) { pico = Math.max(pico, v); mdd = Math.min(mdd, v / pico - 1); }
      const mens = {};
      px.forEach(([s, v]) => { mens[new Date(s * 1000).toISOString().slice(0, 7)] = +v.toFixed(4); });
      out[t] = {
        ye, prim, mens, saltos, n: ult.length,
        ult: px.length ? [new Date(px[px.length - 1][0] * 1000).toISOString().slice(0, 10), px[px.length - 1][1]] : null,
        vol: rets.length > 100 ? +(dp * Math.sqrt(252) * 100).toFixed(2) : null,
        mdd: +(mdd * 100).toFixed(2),
      };
    } catch (e) {
      out[t] = { erro: String(e).slice(0, 80) };
    }
    await esperar(pausaMs);
  }
  baixar("yahoo_fii.json", { coletado: new Date().toISOString(), cotacoes: out });
  return out;
}
