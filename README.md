# Peneiras

Duas ferramentas de estudo para a B3, com o mesmo raciocínio em quatro passos (método de Ramiro Gomes Ferreira / Clube do Valor):

| Pasta | O que é |
|---|---|
| `acoes/` | **Peneira de Valor**: ações da B3. `site/` é a versão original; `site_cdv/` é a versão de apresentação ao Clube do Valor ("Ações Baratas"), que usa o mesmo motor. |
| `fiis/` | **Peneira FIIs**: fundos imobiliários. Projeto separado, não importa nada de `acoes/`. |

Em cada pasta, o caminho dos dados é o mesmo:

```
fontes  ->  collector/  ->  data/base*.json  ->  site/motor*.js (o método)  ->  site/app.html (a página)
```

## Como montar as páginas

```bash
python acoes/site/montar_site.py          # acoes/dist/
python acoes/site_cdv/montar_site_cdv.py  # acoes/dist_cdv/
python fiis/site/montar_site_fii.py       # fiis/dist_fii/
```

As páginas montadas a partir deste repositório são idênticas às versões publicadas em 10/11/2026.

## Integração em andamento

Hoje parte dos dados vem de sites não oficiais lidos pelo navegador (Status Invest, Fundamentus, Yahoo). A troca é por fontes oficiais e gratuitas, coletadas por um robô agendado no GitHub Actions:

- **B3, COTAHIST**: preço, volume e liquidez de todos os ativos.
- **CVM, Dados Abertos**: balanços das companhias e informes dos FIIs (já usado).
- **CVM, FundosNET**: rendimentos anunciados pelos FIIs.
- **Banco Central, SGS**: Selic, CDI e IPCA.

Os detalhes de cada peneira estão no `README.md` da própria pasta.

Não é recomendação de investimento.
