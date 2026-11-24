# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-24 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-19 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | – | – | ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer')) |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 34 | 1 |
| Liquidez diária (R$) | 381 | 2,0% | 92 | 21 |
| Volatilidade 1 ano (%) | 392 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 398 | 0,0% | 8 | 1 |
| Valor de mercado (R$) | 582 | 0,2% | 34 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 266 | 8,8% | 11,4% | 151 |
| 2 meses so dias com negocio | 266 | 8,8% | 11,3% | 149 |
| 21 pregoes | 266 | -0,8% | 1,8% | 18 |
| 42 pregoes | 266 | 1,4% | 9,0% | 119 |
| 63 pregoes | 266 | -10,1% | 14,0% | 179 |

### O que muda no resultado do método

Ranqueados: 109 antes, 110 depois. Entraram 1, saíram 0, continuaram 109.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| SOJA3 | Volatilidade de 49.4% a.a. entre os 20% mais voláteis (corte em 48.4%) | 70º  |

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | LREN3 | ALLD3 |
| 3 | ALLD3 | LREN3 |
| 4 | VLID3 | VLID3 |
| 5 | MDIA3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | DEXP3 | DEXP3 |
| 8 | BLAU3 | ALOS3 |
| 9 | GMAT3 | BMGB4 |
| 10 | BMGB4 | GMAT3 |
| 11 | ALOS3 | BLAU3 |
| 12 | JHSF3 | JHSF3 |
| 13 | ABCB4 | BBDC4 |
| 14 | VIVA3 | VIVA3 |
| 15 | GOAU4 | GOAU4 |
| 16 | FESA4 | FESA4 |
| 17 | SYNE3 | BRBI11 |
| 18 | BBDC4 | SYNE3 |
| 19 | BRBI11 | INTB3 (novo) |
| 20 | GGBR4 | ABCB4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: BRKM3 3,10 → 3,80 (23%); FIQE3 5,73 → 6,85 (20%); TXRX3 5,46 → 6,50 (19%); SEQL3 7,37 → 6,20 (-16%); NUTR3 2,97 → 2,51 (-15%); AZEV3 10,51 → 11,95 (14%); INEP4 1,15 → 1,00 (-13%); BRKM5 2,60 → 2,91 (12%)

**Liquidez diária (R$)**: RPAD6 71 → 429 (500%); PATI4 332 → 0 (-100%); BAUH4 8.151 → 13.133 (61%); PLAS3 1.613 → 850 (-47%); CTAX3 10.189 → 5.451 (-46%); GSHP3 455 → 253 (-45%); EMAE4 27.705 → 16.510 (-40%); CRPG6 4.298 → 2.652 (-38%)

**Volatilidade 1 ano (%)**: FIQE3 45,1 → 48,5 (8%); CGAS5 19,6 → 20,8 (6%); BRKM3 67,3 → 70,4 (5%); HBOR3 66,5 → 63,7 (-4%); LEVE3 32,0 → 31,1 (-3%); INEP4 59,7 → 61,4 (3%); NUTR3 73,8 → 75,7 (3%); BRAP3 27,0 → 26,4 (-2%)

**Maior queda 1 ano (%)**: TXRX4 -20,1 → -24,7 (23%); CALI3 -16,9 → -14,8 (-12%); EALT4 -35,6 → -39,1 (10%); PETR3 -26,9 → -29,3 (9%); GMAT3 -44,4 → -40,8 (-8%); PETR4 -28,5 → -30,8 (8%); PSSA3 -21,2 → -22,6 (7%); WHRL3 -33,9 → -35,9 (6%)

**Valor de mercado (R$)**: BRKM3 2,37 bi → 2,90 bi (23%); FIQE3 2,29 bi → 2,73 bi (20%); TXRX3 11,1 mi → 13,2 mi (19%); SEQL3 313,0 mi → 263,3 mi (-16%); NUTR3 39,3 mi → 33,2 mi (-15%); AZEV3 1,17 bi → 1,33 bi (14%); INEP4 59,8 mi → 52,0 mi (-13%); BRKM5 2,07 bi → 2,32 bi (12%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 22 | 0 |
| Liquidez diária (R$) | 356 | 0,8% | 30 | 12 |
| Volatilidade 1 ano (%) | 323 | 0,1% | 6 | 0 |
| Maior queda 1 ano (%) | 346 | 0,0% | 48 | 5 |
| DY 12 meses (%) | 382 | 0,6% | 19 | 1 |
| P/VP | 470 | 0,3% | 21 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 202 | 6,5% | 7,9% | 77 |
| 2 meses so dias com negocio | 202 | 7,1% | 8,3% | 83 |
| 21 pregoes | 202 | 7,1% | 14,7% | 131 |
| 42 pregoes | 202 | 0,6% | 0,9% | 8 |
| 63 pregoes | 202 | -5,8% | 9,1% | 90 |

### O que muda no resultado do método

Ranqueados: 58 antes, 60 depois. Entraram 2, saíram 0, continuaram 58.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| HGBL11 | Liquidez média diária R$ 0,46 mi abaixo de R$ 0,5 mi | 11º (fof) |
| SNME11 | Liquidez média diária R$ 0,34 mi abaixo de R$ 0,5 mi | 14º (fof) |

**Top 12 fof**: 12 de 12 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | CPTS11 | RBRX11 |
| 3 | RBRX11 | CPTS11 |
| 4 | JSAF11 | JSAF11 |
| 5 | HFOF11 | HFOF11 |
| 6 | BTHF11 | BTHF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | RINV11 | GARE11 |
| 9 | GARE11 | RINV11 |
| 10 | SNEL11 | SNEL11 |
| 11 | RZLC11 | HGBL11 (novo) |
| 12 | SEED11 | RZLC11 |
| 13 |  | SEED11 |
| 14 |  | SNME11 (novo) |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | RZAK11 |
| 3 | RZAK11 | VCJR11 |
| 4 | VGIP11 | RECR11 |
| 5 | RECR11 | VGIP11 |
| 6 | VRTA11 | VRTA11 |
| 7 | VGIR11 | VGIR11 |
| 8 | RBRR11 | PORD11 |
| 9 | RBRY11 | BTCI11 |
| 10 | CLIN11 | RBRY11 |
| 11 | BTCI11 | RBRR11 |
| 12 | PORD11 | XPCI11 |
| 13 | ICRI11 | CLIN11 |
| 14 | XPCI11 | ICRI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNIP11 | KNIP11 |
| 17 | KNHY11 | KNHY11 |
| 18 | MCCI11 | MCCI11 |
| 19 | HREC11 | KNSC11 (novo) |
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
| 11 | HGRU11 | TJKB11 |
| 12 | KNHF11 | LVBI11 |
| 13 | LVBI11 | HGBS11 |
| 14 | TJKB11 | HGRU11 |
| 15 | HGBS11 | BRCO11 |
| 16 | BRCO11 | KNHF11 |
| 17 | XPLG11 | XPLG11 |
| 18 | KNRI11 | KNRI11 |
| 19 | PMLL11 | PMLL11 |
| 20 | HGLG11 | HGLG11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: RBOP11 187,49 → 164,37 (-12%); OCRE11 79,69 → 69,99 (-12%); WTSP11 69,88 → 62,05 (-11%); MGHT11 11,18 → 12,42 (11%); ONDA11 6,80 → 6,08 (-11%); FPAB11 219,97 → 201,06 (-9%); CACR11 8,38 → 7,75 (-8%); EMET11 9,98 → 9,29 (-7%)

**Liquidez diária (R$)**: PNPR11 128.007 → 318.482 (149%); VGII11 249.860 → 0 (-100%); PATA11 5.612 → 10.436 (86%); SNME11 336.507 → 624.504 (86%); GSFI11 212.384 → 327.796 (54%); AJFI11 263.497 → 385.287 (46%); RECD11 2.953 → 1.675 (-43%); ADSH11 3,6 mi → 2,3 mi (-35%)

**Volatilidade 1 ano (%)**: TORD11 31,7 → 29,0 (-8%); RZAK11 14,4 → 15,5 (7%); PORD11 13,7 → 14,6 (7%); BTAL11 20,7 → 21,9 (6%); EXES11 10,8 → 11,3 (5%); RBOP11 39,3 → 41,4 (5%); INLG11 16,4 → 17,1 (4%); BTCI11 16,2 → 16,9 (4%)

**Maior queda 1 ano (%)**: PORD11 -9,2 → -13,1 (42%); BTAL11 -16,3 → -22,0 (35%); EQIR11 -10,8 → -13,5 (25%); NEXG11 -9,0 → -11,1 (23%); RZAK11 -21,5 → -25,9 (20%); HOFC11 -21,9 → -26,1 (19%); ALZC11 -19,6 → -22,9 (17%); EXES11 -4,9 → -5,7 (15%)

**DY 12 meses (%)**: RBIR11 14,32 → 19,23 (34%); RBOP11 12,73 → 14,52 (14%); OCRE11 5,97 → 6,80 (14%); WTSP11 9,09 → 10,23 (13%); ONDA11 16,98 → 19,00 (12%); FPAB11 10,97 → 12,00 (9%); CACR11 91,89 → 99,35 (8%); EMET11 12,73 → 13,67 (7%)

**P/VP**: GSFI11 0,89 → 0,72 (-18%); RBOP11 0,26 → 0,23 (-12%); OCRE11 0,60 → 0,53 (-12%); WTSP11 0,74 → 0,65 (-11%); MGHT11 0,58 → 0,65 (11%); FPAB11 0,62 → 0,57 (-9%); CACR11 0,09 → 0,09 (-8%); EMET11 1,10 → 1,02 (-7%)

