# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-18 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-16 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,60 | 2026-11-16 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 38 | 3 |
| Liquidez diária (R$) | 381 | 1,5% | 69 | 12 |
| Volatilidade 1 ano (%) | 391 | 0,1% | 0 | 0 |
| Maior queda 1 ano (%) | 397 | 0,0% | 2 | 0 |
| Valor de mercado (R$) | 582 | 0,2% | 38 | 3 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 265 | 7,2% | 9,4% | 124 |
| 2 meses so dias com negocio | 265 | 7,2% | 9,4% | 124 |
| 21 pregoes | 265 | -0,9% | 1,5% | 9 |
| 42 pregoes | 265 | -2,6% | 8,9% | 114 |
| 63 pregoes | 265 | -14,5% | 16,4% | 192 |

### O que muda no resultado do método

Ranqueados: 109 antes, 109 depois. Entraram 0, saíram 0, continuaram 109.

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | LREN3 | ALLD3 |
| 3 | ALLD3 | LREN3 |
| 4 | VLID3 | VLID3 |
| 5 | MDIA3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | BLAU3 | DEXP3 |
| 8 | DEXP3 | GMAT3 |
| 9 | GMAT3 | BLAU3 |
| 10 | BMGB4 | BMGB4 |
| 11 | ALOS3 | ALOS3 |
| 12 | JHSF3 | JHSF3 |
| 13 | VIVA3 | ABCB4 |
| 14 | ABCB4 | VIVA3 |
| 15 | GOAU4 | GOAU4 |
| 16 | GGBR4 | GGBR4 |
| 17 | BBDC4 | FESA4 |
| 18 | FESA4 | SYNE3 |
| 19 | SYNE3 | CSUD3 (novo) |
| 20 | BRBI11 | BBDC4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: OSXB3 2,20 → 1,31 (-40%); AZEV3 8,75 → 11,47 (31%); VIVR3 2,41 → 3,10 (29%); SEQL3 8,26 → 6,70 (-19%); LJQQ3 0,97 → 1,14 (18%); INEP3 1,34 → 1,12 (-16%); UCAS3 0,80 → 0,91 (14%); AALR3 0,95 → 0,83 (-13%)

**Liquidez diária (R$)**: CTKA3 326 → 0 (-100%); BAUH4 1.359 → 2.717 (100%); PDGR3 538.463 → 287.342 (-47%); NORD3 1.272 → 1.781 (40%); BRKM6 1.159 → 793 (-32%); HBSA3 8,1 mi → 10,6 mi (31%); AALR3 182.704 → 231.695 (27%); JFEN3 91.179 → 67.449 (-26%)

**Volatilidade 1 ano (%)**: MDIA3 38,3 → 36,5 (-5%); UCAS3 45,6 → 47,4 (4%); INEP3 67,2 → 69,4 (3%); CBAV3 24,3 → 23,7 (-2%); BAZA3 34,1 → 34,9 (2%); SCAR3 41,0 → 41,9 (2%); LJQQ3 80,4 → 81,9 (2%); WDCN3 45,8 → 46,5 (2%)

**Maior queda 1 ano (%)**: CBAV3 -11,2 → -9,9 (-12%); MGEL4 -39,5 → -37,2 (-6%); MTSA4 -37,0 → -38,3 (3%); OBTC3 -58,2 → -56,4 (-3%); BRAV3 -36,0 → -37,0 (3%); AALR3 -82,4 → -84,6 (3%); BPAC3 -54,6 → -56,1 (3%); BBAS3 -45,8 → -47,0 (3%)

**Valor de mercado (R$)**: OSXB3 6,9 mi → 4,1 mi (-40%); AZEV3 973,2 mi → 1,28 bi (31%); VIVR3 11,8 mi → 15,1 mi (29%); SEQL3 350,8 mi → 284,5 mi (-19%); LJQQ3 189,2 mi → 222,4 mi (18%); INEP3 73,9 mi → 61,8 mi (-16%); UCAS3 52,9 mi → 60,1 mi (14%); AALR3 144,7 mi → 126,5 mi (-13%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 18 | 1 |
| Liquidez diária (R$) | 354 | 0,7% | 28 | 9 |
| Volatilidade 1 ano (%) | 322 | 0,1% | 4 | 1 |
| Maior queda 1 ano (%) | 346 | 0,0% | 7 | 1 |
| DY 12 meses (%) | 382 | 0,2% | 21 | 7 |
| P/VP | 469 | 0,1% | 15 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 201 | 8,2% | 9,4% | 96 |
| 2 meses so dias com negocio | 201 | 9,1% | 10,5% | 103 |
| 21 pregoes | 201 | 6,7% | 14,3% | 126 |
| 42 pregoes | 201 | 0,0% | 0,7% | 9 |
| 63 pregoes | 201 | -5,4% | 8,8% | 89 |

### O que muda no resultado do método

Ranqueados: 56 antes, 57 depois. Entraram 1, saíram 0, continuaram 56.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| TJKB11 | Liquidez média diária R$ 0,05 mi abaixo de R$ 0,5 mi | 17º (tijolo) |

**Top 12 fof**: 12 de 12 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | JSAF11 | CPTS11 |
| 3 | RBRX11 | RBRX11 |
| 4 | CPTS11 | JSAF11 |
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
| 3 | VGIP11 | VGIP11 |
| 4 | RZAK11 | RZAK11 |
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
| 16 | KNIP11 | KNHY11 |
| 17 | KNHY11 | KNIP11 |
| 18 | MCCI11 | MCCI11 |
| 19 | KNUQ11 | KNUQ11 |
| 20 | MXRF11 | MXRF11 |

**Top 20 tijolo**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | BRCR11 | BRCR11 |
| 3 | GTWR11 | GTWR11 |
| 4 | TVRI11 | TVRI11 |
| 5 | RCRB11 | HGRE11 |
| 6 | HGRE11 | RCRB11 |
| 7 | RBRP11 | RBRP11 |
| 8 | VILG11 | VILG11 |
| 9 | FATN11 | FATN11 |
| 10 | CPSH11 | CPSH11 |
| 11 | LVBI11 | HGRU11 |
| 12 | HGRU11 | LVBI11 |
| 13 | KNHF11 | BRCO11 |
| 14 | BRCO11 | KNHF11 |
| 15 | HGBS11 | XPLG11 |
| 16 | XPLG11 | HGBS11 |
| 17 | PMLL11 | TJKB11 (novo) |
| 18 | HGLG11 | PMLL11 |
| 19 | KNRI11 | HGLG11 |
| 20 | ALZR11 | KNRI11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: KNRE11 0,20 → 0,25 (25%); SHPP11 13,41 → 10,99 (-18%); BLOG11 9,49 → 8,00 (-16%); RECD11 5,89 → 5,04 (-14%); ONDA11 7,49 → 6,67 (-11%); CARE11 3,35 → 3,05 (-9%); CPOF11 125,00 → 115,00 (-8%); CBOP11 26,00 → 27,96 (8%)

**Liquidez diária (R$)**: TJKB11 47.167 → 964.589 (1.945%); SEED11 596.910 → 1,6 mi (174%); HBCR11 3,5 mi → 7,9 mi (127%); HIRE11 50 → 17 (-67%); CPOF11 8,9 mi → 13,0 mi (46%); GSFI11 168.870 → 225.054 (33%); RBRL11 1,0 mi → 1,3 mi (30%); XLPR11 42.870 → 30.739 (-28%)

**Volatilidade 1 ano (%)**: CPOF11 10,1 → 13,1 (30%); ADSH11 13,8 → 15,2 (10%); IBBP11 45,2 → 42,0 (-7%); TJKB11 16,7 → 17,9 (7%); SHPP11 76,2 → 79,7 (5%); BLOG11 59,5 → 61,9 (4%); HGBL11 18,1 → 18,8 (4%); FLRP11 22,0 → 22,8 (4%)

**Maior queda 1 ano (%)**: CPOF11 -5,5 → -8,0 (47%); VRTM11 -20,1 → -22,5 (12%); CPTS11 -17,1 → -18,7 (9%); XPML11 -20,1 → -21,3 (6%); PMIS11 -18,7 → -19,9 (6%); RZAG11 -18,8 → -19,8 (6%); ICRI11 -17,2 → -18,2 (6%); EDGA11 -21,5 → -20,5 (-5%)

**DY 12 meses (%)**: IVBP11 1,27 → 1,91 (50%); RBIR11 13,88 → 19,35 (39%); HBCR11 4,75 → 6,14 (29%); SHPP11 4,66 → 5,80 (24%); TJKB11 13,92 → 10,72 (-23%); KNRE11 0,62 → 0,49 (-21%); MIDW11 4,82 → 5,82 (21%); ONDA11 14,76 → 17,31 (17%)

**P/VP**: KNRE11 0,59 → 0,73 (25%); SHPP11 1,38 → 1,13 (-18%); BLOG11 0,84 → 0,71 (-16%); CARE11 0,10 → 0,09 (-9%); CPOF11 0,97 → 0,89 (-8%); CBOP11 0,36 → 0,39 (8%); WTSP11 0,74 → 0,68 (-7%); NVHO11 0,82 → 0,76 (-7%)

