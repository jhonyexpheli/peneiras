# Peneira de Valor (screener B3)

Screener de ações da B3 pelo método em 4 passos (estratégia Ramiro Gomes Ferreira / Clube do Valor).
Hoje é uma página HTML estática; a estrutura já está separada para virar site real
(coleta → base normalizada → motor do método → interface).

## Os 4 passos

1. **Tira o que não dá pra operar**: liquidez média diária abaixo de R$ 1 milhão; companhias em
   recuperação judicial, extrajudicial, falência ou liquidação (cadastro oficial da CVM); OPA pendente
   (`config/opa.json`, mantido à mão).
2. **Tira prejuízo e as mais voláteis**: prejuízo nos últimos 12 meses, no último trimestre ou no último
   exercício fechado; depois saem os 20% mais voláteis (desvio-padrão anualizado dos retornos diários,
   252 pregões).
3. **Ordena por um índice de valor**: quanto vem por real pago de caixa (líquido ou bruto), de lucro
   operacional (EBIT 12m / valor da firma) e de patrimônio (PL / valor de mercado). Cada componente vira
   percentil 0–100 dentro do grupo; o índice é a média ponderada. Bancos e seguradoras formam grupo próprio
   (lucro, patrimônio e dividendo por real pago).
4. **Compara com a média histórica** de 10, 5 e 2 anos (pontos anuais: ano corrente em 12 meses + até 9
   exercícios fechados). Sem o período inteiro, informa o escopo máximo usado. KPIs por setor em
   `config/setores.json` (ex.: bancos com DY e ROE para regressão à média).

## Carteira

Aba para acompanhar as posições montadas a partir da peneira: ticker, quantidade, preço de entrada, data,
preço alvo e observação. Mostra investido, caixa livre, valor na cotação da base, resultado, peso de cada
ativo, quanto falta até o alvo e a posição da ação no ranking com os critérios do momento. Da ficha de
qualquer ação dá para mandar o ticker para o formulário ("Adicionar à carteira").

**Preço alvo do método**: preço em que a ação voltaria à própria média de 5 anos nos múltiplos do passo 4.
Não financeiras: média do preço implícito no P/VP e no EV/EBIT (o EV volta à média e a dívida líquida é
descontada). Bancos e seguradoras: P/VP e P/L. É sugestão; o alvo de cada posição é editável.

**Onde fica salvo** (`site/carteira.js`, objeto `Armazem`):
- publicado como Artifact: banco do artifact (capability `db`), coleção `carteira` (um documento por
  ticker) e documento `ajustes/carteira` (`{capital}`); regras: todos leem, só o dono/editores gravam;
- fora do Artifact (site estático): `localStorage` do navegador (`peneira-carteira-v1`).

Documento de posição: `{ticker, qtd, preco_entrada, data_entrada (AAAA-MM-DD), preco_alvo, nota, atualizado}`.
No site real, troque o `Armazem` por chamadas à API própria mantendo essa forma.

## Versão de apresentação ao Clube do Valor (`site_cdv/`)

Cópia da Peneira com o layout do documento "Peneira de Valor × Clube do Valor: identidade e layout"
(Claude Docs, 02/11/2026). A versão original em `site/` não muda. Usa o mesmo `site/motor.js`.

- Paleta e fontes do site do Clube: fundo #F5F6FA, azul de ação #3271DC, marinho #1C1B35 (faixa do topo e
  cabeçalho das tabelas), ouro #F5C400 só no selo "abaixo da média de 5 anos"; Lexend nos títulos, Inter no texto.
- Sem logotipo nem nome do Clube como autoria; rodapé identifica o protótipo como independente.
- Aba "Ações Baratas": coluna Earning Yield (EBIT/EV; bancos: lucro/preço) como primeira métrica, top 20 em azul
  claro com corte "fim do top 20", selo ouro no desconto.
- Ficha: três números grandes (Earning Yield, desconto vs média 5a, preço alvo do método).
- Carteira: botão "Montar carteira Ações Baratas (20 × 5%)" (substitui as posições, com confirmação) e aviso da
  próxima revisão trimestral.
- Montagem: `python site_cdv/montar_site_cdv.py` → `dist_cdv/`. Publicada como artifact próprio, com banco
  separado do original (mesmas regras de acesso).

## Estrutura

```
config/
  criterios.json      parâmetros do método (cortes, pesos, janelas)
  setores.json        perfis de setor, KPIs preponderantes e direção de cada indicador
  opa.json            OPAs pendentes/concluídas, com fonte
collector/
  fontes.py           clientes HTTP de cada fonte (todos os endpoints num lugar só)
  coletar.py          coleta completa pelo servidor (Status Invest hoje responde 403 ao servidor)
  coletar_direto.py   CVM + fichas do Fundamentus (funcionam pelo servidor)
  coletar_navegador.js  Status Invest e cotações ajustadas do Fundamentus, rodando numa aba do navegador
  montar_base.py      junta as fontes por ticker -> data/base.json (sem aplicar o método)
site/
  motor.js            o método (passos 1 a 4); roda no navegador e em Node
  carteira.js         aba Carteira (posições, preço alvo, armazenamento)
  app.html            interface (ranking, carteira, eliminadas, ficha da ação, método e fontes)
  montar_site.py      gera dist/index.html (site estático) e dist/artifact.html, embutindo motor.js e carteira.js
site_cdv/             versão de apresentação ao Clube do Valor (app.html, carteira.js, montar_site_cdv.py)
data/raw/             dados crus de cada coleta (JSON; fora do repositório)
data/base.json        base normalizada que o site lê
```

## Atualizar os dados (processo atual, a ser substituído pelo coletor oficial)

```bash
# 1) no navegador (aba do Status Invest e aba do Fundamentus): ver collector/coletar_navegador.js
#    -> salvar statusinvest_navegador.json e cotacoes_fundamentus.json em data/raw/
# 2) no servidor
pip install requests beautifulsoup4 lxml
python collector/coletar_direto.py
python collector/montar_base.py
python site/montar_site.py          # dist/index.html + dist/base.json
```

Ao publicar como Artifact, declarar `capabilities: {db: {rules: [{path: "carteira", read: "view", write: "admin"},
{path: "ajustes", read: "view", write: "admin"}]}, user: {}}`. A carteira salva não depende do HTML: republicar
a página não apaga as posições.

## Fontes

| Fonte | Endpoint | Dados | Acesso |
|---|---|---|---|
| Status Invest | `category/advancedsearchresultpaginated` | universo, liquidez, setor, indicadores atuais | navegador |
| Status Invest | `acao/indicatorhistoricallist` (time=7) | histórico anual de ~30 indicadores | navegador |
| Status Invest | `acao/tickerprice` (type=4) | cotações 5 anos, sem ajuste | navegador |
| Fundamentus | `detalhes.php` | caixa, dívida, PL, EBIT e lucro 12m e do trimestre | servidor |
| Fundamentus | `amline/cot_hist.php` | fechamento diário ajustado | navegador |
| CVM | `dados.cvm.gov.br/.../cad_cia_aberta.csv` | situação do emissor (RJ, falência…) | servidor |
| brapi.dev | `api/quote/{ticker}` | cotações (token para a maioria dos papéis) | servidor |

Para produção: trocar as fontes não oficiais por fontes oficiais (B3 COTAHIST para preços e liquidez;
demonstrativos da CVM, DFP/ITR, para caixa, EBIT, PL e lucro oficiais por período).

Não é recomendação de investimento.
