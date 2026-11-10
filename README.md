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

## Robôs (GitHub Actions)

| Robô | Quando roda | O que faz |
|---|---|---|
| **Coletor oficial** (`.github/workflows/coletor-oficial.yml`) | dias úteis às 22h37 de Brasília, ou pelo botão *Run workflow* | baixa B3, CVM, Banco Central e Tesouro, monta as bases, grava o quadro de diferenças em `relatorios/diferencas.md` e, se houve pregão novo, publica o site |
| **Publicar site** (`.github/workflows/publicar-site.yml`) | quando o `main` muda, ou chamado pelo coletor | monta as páginas e publica em https://jhonyexpheli.github.io/peneiras |

Se uma coleta falhar, o GitHub manda e-mail e o registro fica em `relatorios/execucao.log`; a base que está no ar não é tocada.

## Integração em andamento

Hoje parte dos dados vem de sites não oficiais lidos pelo navegador (Status Invest, Fundamentus, Yahoo). A troca é por fontes oficiais e gratuitas, coletadas por um robô agendado no GitHub Actions:

- **B3, COTAHIST**: preço, volume e liquidez de todos os ativos.
- **CVM, Dados Abertos**: balanços das companhias e informes dos FIIs (já usado).
- **CVM, FundosNET**: rendimentos anunciados pelos FIIs.
- **Banco Central, SGS**: Selic, CDI e IPCA.

Os detalhes de cada peneira estão no `README.md` da própria pasta.

Não é recomendação de investimento.
