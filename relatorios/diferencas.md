# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-19 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-17 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,60 | 2026-11-17 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,3% | 27 | 1 |
| Liquidez diária (R$) | 380 | 1,5% | 60 | 10 |
| Volatilidade 1 ano (%) | 391 | 0,1% | 1 | 0 |
| Maior queda 1 ano (%) | 397 | 0,0% | 8 | 1 |
| Valor de mercado (R$) | 582 | 0,3% | 27 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 266 | 7,2% | 10,0% | 133 |
| 2 meses so dias com negocio | 266 | 7,2% | 10,0% | 133 |
| 21 pregoes | 266 | -0,7% | 1,6% | 6 |
| 42 pregoes | 266 | -1,0% | 8,2% | 115 |
| 63 pregoes | 266 | -12,9% | 15,9% | 189 |

### O que muda no resultado do método

Ranqueados: 109 antes, 109 depois. Entraram 0, saíram 0, continuaram 109.

**Top 20**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | ALLD3 |
| 3 | LREN3 | LREN3 |
| 4 | VLID3 | MDIA3 |
| 5 | MDIA3 | VLID3 |
| 6 | EUCA4 | EUCA4 |
| 7 | DEXP3 | DEXP3 |
| 8 | GMAT3 | GMAT3 |
| 9 | BLAU3 | BLAU3 |
| 10 | BMGB4 | BMGB4 |
| 11 | ALOS3 | ALOS3 |
| 12 | JHSF3 | JHSF3 |
| 13 | ABCB4 | ABCB4 |
| 14 | VIVA3 | GOAU4 |
| 15 | GOAU4 | VIVA3 |
| 16 | GGBR4 | FESA4 |
| 17 | FESA4 | SYNE3 |
| 18 | SYNE3 | GGBR4 |
| 19 | CSUD3 | CSUD3 |
| 20 | BBDC4 | BBDC4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: ESTR4 2,33 → 1,27 (-45%); AALR3 0,83 → 0,74 (-11%); AVLL3 5,23 → 4,69 (-10%); VIVR3 3,10 → 3,40 (10%); AZEV4 0,75 → 0,68 (-9%); SOND6 82,00 → 75,00 (-9%); AMBP3 0,12 → 0,11 (-8%); CSED3 3,85 → 3,56 (-8%)

**Liquidez diária (R$)**: BAUH4 2.717 → 4.981 (83%); GSHP3 2.036 → 820 (-60%); RPAD6 143 → 71 (-50%); HAGA3 13.654 → 8.021 (-41%); TXRX4 793 → 483 (-39%); RCSL3 106.211 → 145.994 (37%); NEXP3 1.138 → 788 (-31%); SOND6 4.725 → 6.161 (30%)

**Volatilidade 1 ano (%)**: NATU3 51,9 → 49,0 (-5%); PSSA3 28,2 → 27,2 (-4%); EVEN3 48,5 → 47,3 (-2%); PASS3 37,3 → 38,1 (2%); BRKM5 79,0 → 77,2 (-2%); MOVI3 74,0 → 72,6 (-2%); MATD3 40,3 → 39,6 (-2%); TAEE3 25,7 → 25,3 (-2%)

**Maior queda 1 ano (%)**: CBAV3 -9,9 → -7,4 (-25%); CGAS3 -13,9 → -16,1 (16%); SOJA3 -56,2 → -48,4 (-14%); BBSE3 -14,8 → -16,1 (8%); BRAV3 -37,0 → -39,5 (7%); HBOR3 -75,1 → -70,3 (-6%); TGMA3 -33,7 → -35,7 (6%); NEXP3 -37,5 → -39,6 (5%)

**Valor de mercado (R$)**: ESTR4 20,7 mi → 11,3 mi (-45%); AALR3 126,5 mi → 112,7 mi (-11%); AVLL3 40,9 mi → 36,6 mi (-10%); VIVR3 15,1 mi → 16,6 mi (10%); AZEV4 83,4 mi → 75,6 mi (-9%); SOND6 146,7 mi → 134,2 mi (-9%); AMBP3 200,5 mi → 183,7 mi (-8%); CSED3 1,40 bi → 1,30 bi (-8%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 17 | 0 |
| Liquidez diária (R$) | 354 | 0,7% | 32 | 5 |
| Volatilidade 1 ano (%) | 322 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 346 | 0,0% | 22 | 1 |
| DY 12 meses (%) | 382 | 0,4% | 18 | 1 |
| P/VP | 470 | 0,2% | 14 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 201 | 7,4% | 8,3% | 88 |
| 2 meses so dias com negocio | 201 | 8,0% | 9,4% | 94 |
| 21 pregoes | 201 | 6,9% | 15,5% | 127 |
| 42 pregoes | 201 | 0,0% | 0,7% | 7 |
| 63 pregoes | 201 | -5,7% | 9,0% | 85 |

### O que muda no resultado do método

Ranqueados: 57 antes, 57 depois. Entraram 0, saíram 0, continuaram 57.

**Top 12 fof**: 12 de 12 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | CPTS11 | JSAF11 |
| 3 | RBRX11 | RBRX11 |
| 4 | JSAF11 | CPTS11 |
| 5 | BTHF11 | BTHF11 |
| 6 | HFOF11 | HFOF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | RINV11 | RINV11 |
| 9 | GARE11 | GARE11 |
| 10 | SNEL11 | SNEL11 |
| 11 | RZLC11 | RZLC11 |
| 12 | SEED11 | SEED11 |

**Top 20 papel**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | VGIP11 | RZAK11 |
| 4 | RZAK11 | VGIP11 |
| 5 | RECR11 | RECR11 |
| 6 | VGIR11 | VGIR11 |
| 7 | VRTA11 | VRTA11 |
| 8 | RBRY11 | RBRY11 |
| 9 | RBRR11 | RBRR11 |
| 10 | BTCI11 | BTCI11 |
| 11 | PORD11 | PORD11 |
| 12 | CLIN11 | CLIN11 |
| 13 | ICRI11 | ICRI11 |
| 14 | XPCI11 | XPCI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNHY11 | KNIP11 |
| 17 | KNIP11 | KNHY11 |
| 18 | MCCI11 | MCCI11 |
| 19 | KNUQ11 | KNUQ11 |
| 20 | MXRF11 | MXRF11 |

**Top 20 tijolo**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | BRCR11 | BRCR11 |
| 3 | GTWR11 | GTWR11 |
| 4 | TVRI11 | TVRI11 |
| 5 | HGRE11 | HGRE11 |
| 6 | RCRB11 | RCRB11 |
| 7 | RBRP11 | RBRP11 |
| 8 | VILG11 | VILG11 |
| 9 | FATN11 | FATN11 |
| 10 | CPSH11 | CPSH11 |
| 11 | HGRU11 | LVBI11 |
| 12 | LVBI11 | HGRU11 |
| 13 | BRCO11 | KNHF11 |
| 14 | KNHF11 | BRCO11 |
| 15 | XPLG11 | XPLG11 |
| 16 | HGBS11 | HGBS11 |
| 17 | TJKB11 | TJKB11 |
| 18 | PMLL11 | PMLL11 |
| 19 | HGLG11 | KNRI11 |
| 20 | KNRI11 | HGLG11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: RECD11 5,04 → 5,89 (17%); VVRI11 8,17 → 6,94 (-15%); OCRE11 70,00 → 79,69 (14%); MGHT11 11,30 → 12,60 (12%); HGIC11 43,39 → 40,14 (-7%); WTSP11 65,00 → 69,80 (7%); EDFO11 129,00 → 120,00 (-7%); EIRA11 98,00 → 104,60 (7%)

**Liquidez diária (R$)**: BRIP11 906 → 374 (-59%); PLRI11 375 → 496 (32%); PEMA11 3.035 → 2.183 (-28%); VXXV11 8,1 mi → 6,1 mi (-25%); BLOG11 33 → 40 (22%); SNME11 140.580 → 168.273 (20%); MIDW11 2,9 mi → 3,5 mi (20%); LSOP11 215.906 → 177.811 (-18%)

**Volatilidade 1 ano (%)**: CPOF11 13,1 → 14,1 (7%); EIRA11 23,5 → 25,0 (6%); VRTM11 15,6 → 16,3 (4%); VGIR11 13,6 → 14,1 (3%); BCRI11 21,3 → 22,0 (3%); SNEL11 12,3 → 12,7 (3%); RBVA11 15,8 → 16,2 (3%); HGBL11 18,8 → 19,2 (2%)

**Maior queda 1 ano (%)**: VXXV11 -0,4 → -0,6 (67%); VRTM11 -22,5 → -26,1 (16%); VGIR11 -18,5 → -21,4 (16%); FYTO11 -15,6 → -17,9 (14%); RZAG11 -19,8 → -22,4 (13%); SHPP11 -21,6 → -24,1 (12%); SNEL11 -20,7 → -23,1 (11%); BCRI11 -33,3 → -36,6 (10%)

**DY 12 meses (%)**: RBIR11 19,35 → 14,31 (-26%); VVRI11 1,84 → 2,16 (18%); RECD11 16,14 → 13,81 (-14%); OCRE11 6,80 → 5,97 (-12%); TSER11 16,40 → 14,75 (-10%); HGIC11 17,88 → 19,33 (8%); EDFO11 7,61 → 8,18 (7%); CACR11 80,88 → 86,52 (7%)

**P/VP**: VVRI11 0,95 → 0,81 (-15%); OCRE11 0,53 → 0,60 (14%); MGHT11 0,59 → 0,65 (12%); HGIC11 0,39 → 0,36 (-7%); WTSP11 0,68 → 0,74 (7%); EDFO11 0,68 → 0,63 (-7%); EIRA11 0,95 → 1,01 (7%); EDGA11 0,29 → 0,31 (7%)

