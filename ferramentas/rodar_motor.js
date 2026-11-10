// Roda o motor de uma peneira com os critérios padrão e imprime o resultado em JSON.
// Uso: node ferramentas/rodar_motor.js <motor.js> <base.json>
const fs = require("fs");
const path = require("path");
const [, , motorPath, basePath] = process.argv;
const M = require(path.resolve(motorPath));
const base = JSON.parse(fs.readFileSync(basePath, "utf-8"));
const R = M.rodar(base, {});
const itens = R.acoes || R.fundos;
const ranq = R.ranqueadas || R.ranqueados;
process.stdout.write(JSON.stringify({
  universo: itens.length,
  ranqueados: ranq.length,
  itens: itens.map((x) => ({
    t: x.ticker,
    etapa: x.etapa,
    pos: x.posicao ?? null,
    grupo: x.grupo ?? null,
    indice: x.indice ?? null,
    motivos: (x.motivos || []).map((m) => m.texto),
  })),
}));
