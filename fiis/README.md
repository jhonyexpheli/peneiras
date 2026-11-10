# Peneira FIIs (screener de fundos imobiliários da B3)

Versão da Peneira de Valor para FIIs: mesmo raciocínio em 4 passos, régua própria de fundo
imobiliário. **Projeto separado de `acoes/`**: não importa código, não lê a base e não usa a
carteira da Peneira de Valor. Escopo e análise ponderada dos filtros: doc "Peneira FIIs: análise e
escopo do método" (Claude Docs, 03/11/2026).

Hoje é uma página HTML estática; a estrutura já está separada para virar site real
(coleta -> base normalizada -> motor do método -> interface).

## Os 4 passos

1. **Tira o que não dá para operar**: liquidez média diária abaixo de R$ 500 mil (Fundamentus, 2 meses);
   sem informe mensal de FII na CVM (Fiagro, FI-Infra); fundo de desenvolvimento (50% ou mais do
   investido em obras, terrenos ou imóveis para venda); menos de 12 meses de pregão; informe mensal com
   mais de 6 meses; código antigo de fundo que trocou de ticker; evento pendente em `config/eventos_fii.json`.
2. **Tira quem está sangrando e os mais voláteis**: resultado financeiro negativo em 12 meses ou no último
   trimestre; rendimentos declarados acima de 110% do resultado dos dois últimos semestres; passivo acima de
   30% do PL; tijolo com vacância física acima de 25%, inadimplência acima de 10% da receita ou um imóvel só;
   papel com evento de crédito registrado à mão; depois os 20% mais voláteis de cada grupo.
3. **Ordena por quanto se leva por real pago**, dentro de cada grupo. O grupo sai da composição do ativo no
   informe mensal (50% ou mais em imóveis = tijolo; em CRI/LCI/LIG = papel; em cotas de FII = FOF; nenhum = híbrido,
   vai para o maior componente com alerta). Componentes em percentil 0-100, índice = média ponderada:

   | Componente | Fórmula | Tijolo | Papel | FOF |
   |---|---|---|---|---|
   | Patrimônio por real | VP da cota ÷ preço | 1 | 2 | 1 |
   | Resultado por real | resultado financeiro 12m (CVM) ÷ valor de mercado | 1 | 1 | 1 |
   | Aluguel por real | aluguel 12m (CVM) ÷ (valor de mercado + passivo) | 1 | – | – |
   | Dividendo por real | rendimentos 12m ÷ preço | – | 1 | 1 |

4. **Compara com a própria história**: P/VP e DY de dezembro de cada ano contra o atual, médias de 10, 5 e 2
   anos (informa quantos anos entraram quando falta período). Prêmio do DY sobre a NTN-B: pendente.

**Preço alvo do método**: preço em que o fundo voltaria à média de 5 anos no P/VP (VP atual × P/VP médio) e no
DY (rendimento 12m ÷ DY médio). Tijolo e FOF: média simples; papel: P/VP com peso 2. Editável na carteira.

## Diversificação do portfólio (ficha do fundo)

Pizza com a distribuição da carteira do fundo, lida do informe trimestral da CVM (8 maiores fatias e "Outros"):
receita por imóvel, área, área vaga (onde está a vacância), estados (lido do endereço; só aparece quando 70% da
receita tem estado identificado), inquilinos por setor, CRIs e LCIs (papel) e cotas de FII (FOF). Medidas: número
de ativos, número efetivo (ativos de mesmo peso que dariam a mesma concentração, 1/HHI), maior ativo e 3 maiores.
O ranking tem a coluna "Diversificação" com o número de ativos do grupo e o número efetivo.

## Carteira

Coleção `carteira_fii` e documento `ajustes/carteira_fii` no banco do artifact próprio da Peneira FIIs
(fora do artifact: `localStorage` `peneira-fii-carteira-v1`). Documento de posição:
`{ticker, qtd, preco_entrada, data_entrada (AAAA-MM-DD), preco_alvo, nota, atualizado}`. Mostra rendimento
estimado por mês e yield on cost. "Montar carteira com 10 da peneira": prioriza quem está abaixo da média de
5 anos, teto de 30% por subtipo de tijolo e 40% em papel (`criterios_fii.json`, bloco `carteira`).

Ao publicar como Artifact: `capabilities: {db: {rules: [{path: "carteira_fii", read: "view", write: "admin"},
{path: "ajustes", read: "view", write: "admin"}]}, user: {}}`.

## Estrutura

```
config/
  criterios_fii.json     cortes, pesos, janelas e regras da carteira
  grupos_fii.json        regra de grupo (50%) e subtipos do tijolo (por segmento CVM ou nome)
  eventos_fii.json       liquidação, incorporação, venda total, evento de crédito (com fonte)
collector/
  fontes_fii.py          endpoints e leitores (CVM, Fundamentus; Status Invest e Yahoo documentados)
  coletar_direto_fii.py  baixa os zips da CVM e as páginas do Fundamentus pelo servidor
  coletar_navegador_fii.js  Yahoo (e Status Invest, opcional) numa aba do navegador
  montar_base_fii.py     junta tudo por ticker -> data/base_fii.json e data/mapa_ticker_cnpj.json
site/
  motor_fii.js           o método (passos 1 a 4); navegador e Node
  carteira_fii.js        aba Carteira
  app.html               interface (ranking por grupo, eliminados, ficha, carteira, método e fontes)
  montar_site_fii.py     gera dist_fii/index.html (estático e artifact) e dist_fii/base_fii.json
data/raw/                coletas cruas (fora do repositório)
data/base_fii.json       base que o site lê (nesta primeira versão, a versão enxuta extraída da página publicada)
```

## Atualizar os dados (processo atual, a ser substituído pelo coletor oficial)

```bash
pip install requests beautifulsoup4 lxml
python collector/coletar_direto_fii.py        # CVM + Fundamentus
# no navegador: collector/coletar_navegador_fii.js -> data/raw/yahoo_fii.txt
python collector/montar_base_fii.py
python site/montar_site_fii.py
```

## Como cada dado é obtido (e as correções)

- **Ticker x CNPJ**: pelo código ISIN do informe mensal (BRxxxxCTF...). ISIN no formato novo (BR0...) ou fundo que
  trocou de ticker (o ISIN guarda o código antigo, ex.: CVBI -> PCIP): casa pelo número de cotas (diferença < 0,05%)
  e PL (< 5%) informados ao Fundamentus. Quando dois códigos apontam para o mesmo CNPJ, fica o mais líquido.
- **Resultado 12m**: soma do resultado financeiro acumulado dos dois últimos semestres do informe trimestral
  (2º e 4º trimestres acumulam o semestre). Rendimentos declarados idem. Aluguel: soma dos 4 trimestres.
- **Vacância**: física, ponderada pela área dos imóveis para renda acabados; inadimplência ponderada pela
  participação de cada imóvel na receita (informe trimestral).
- **DY atual**: rendimento por cota de 12 meses do Fundamentus ÷ cotação. **DY histórico**: DY mensal sobre o
  VP informado à CVM, somado no ano e dividido pelo P/VP de dezembro (não mistura unidades em desdobramentos);
  descartado quando o DY de 12m pela CVM diverge mais de 15% do Fundamentus.
- **P/VP histórico**: fechamento de dezembro (Yahoo, sem ajuste por rendimentos) ÷ VP do informe de dezembro.
  Pontos fora de 0,2–3,0 e fechamentos repetidos são descartados e listados na ficha.

## Fontes

| Fonte | Endpoint | Dados | Acesso |
|---|---|---|---|
| CVM | `dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/` | PL, VP, cotas, cotistas, ativo e passivo, DY mensal (desde 2016) | servidor |
| CVM | `dados.cvm.gov.br/dados/FII/DOC/INF_TRIMESTRAL/DADOS/` | resultado, rendimentos, aluguel, imóveis | servidor |
| Fundamentus | `fii_resultado.php`, `detalhes.php` | universo, cotação, liquidez, rendimento e FFO 12m | servidor |
| Yahoo Finance | `v8/finance/chart/{ticker}.SA` | fechamento diário (2 anos) e mensal (10 anos) sem ajuste | navegador |
| Status Invest | `category/advancedsearchresultpaginated?CategoryType=2`, `fii/companytickerprovents` | setor, cotistas, rendimentos por data com (opcional) | navegador |

Para produção: trocar Fundamentus, Yahoo e Status Invest por fontes oficiais (B3 COTAHIST e FundosNET) e
ler os zips da CVM direto no servidor, como já é feito.

Não é recomendação de investimento.
