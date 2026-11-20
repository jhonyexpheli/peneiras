# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-20 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-18 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,60 | 2026-11-18 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 39 | 1 |
| Liquidez diária (R$) | 380 | 2,1% | 91 | 16 |
| Volatilidade 1 ano (%) | 391 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 397 | 0,0% | 8 | 2 |
| Valor de mercado (R$) | 582 | 0,1% | 39 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 266 | 7,2% | 9,8% | 131 |
| 2 meses so dias com negocio | 266 | 7,2% | 9,8% | 131 |
| 21 pregoes | 266 | -1,6% | 2,1% | 22 |
| 42 pregoes | 266 | -0,8% | 7,9% | 111 |
| 63 pregoes | 266 | -11,8% | 15,4% | 187 |

### O que muda no resultado do método

Ranqueados: 109 antes, 109 depois. Entraram 0, saíram 0, continuaram 109.

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | LREN3 |
| 3 | LREN3 | ALLD3 |
| 4 | MDIA3 | VLID3 |
| 5 | VLID3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | DEXP3 | DEXP3 |
| 8 | GMAT3 | BLAU3 |
| 9 | BLAU3 | GMAT3 |
| 10 | BMGB4 | BMGB4 |
| 11 | ALOS3 | ALOS3 |
| 12 | JHSF3 | JHSF3 |
| 13 | ABCB4 | ABCB4 |
| 14 | GOAU4 | VIVA3 |
| 15 | VIVA3 | GOAU4 |
| 16 | FESA4 | FESA4 |
| 17 | SYNE3 | SYNE3 |
| 18 | GGBR4 | BBDC4 |
| 19 | CSUD3 | BRBI11 (novo) |
| 20 | BBDC4 | GGBR4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: AGXY3 0,21 → 0,30 (43%); VIVR3 3,40 → 2,73 (-20%); SEQL3 6,20 → 7,37 (19%); AALR3 0,74 → 0,83 (12%); AZTE3 0,66 → 0,60 (-9%); AZEV4 0,68 → 0,62 (-9%); IFCM3 0,92 → 0,84 (-9%); BIOM3 5,80 → 5,33 (-8%)

**Liquidez diária (R$)**: BAUH4 4.981 → 8.151 (64%); MNDL3 5.627 → 2.825 (-50%); TXRX4 483 → 263 (-46%); BALM3 1.152 → 629 (-45%); GSHP3 820 → 455 (-45%); COCE3 6.760 → 4.008 (-41%); DOHL4 7.388 → 4.575 (-38%); HAGA3 8.021 → 5.296 (-34%)

**Volatilidade 1 ano (%)**: VIVR3 58,6 → 62,5 (7%); CGAS5 18,5 → 19,6 (6%); HBOR3 70,0 → 66,5 (-5%); SOJA3 51,9 → 49,4 (-5%); TAEE4 23,3 → 22,7 (-3%); TAEE3 25,3 → 24,7 (-3%); TAEE11 25,8 → 25,1 (-2%); MILS3 26,7 → 26,3 (-1%)

**Maior queda 1 ano (%)**: CGAS5 -16,5 → -21,7 (31%); PEAB3 -16,7 → -20,8 (25%); HAPV3 -87,8 → -78,9 (-10%); CRPG6 -68,3 → -62,2 (-9%); EALT4 -32,8 → -35,6 (9%); DEXP3 -25,9 → -27,9 (8%); CRPG5 -67,8 → -63,7 (-6%); AGRO3 -25,2 → -26,7 (6%)

**Valor de mercado (R$)**: AGXY3 4,2 mi → 5,9 mi (43%); VIVR3 16,6 mi → 13,3 mi (-20%); SEQL3 263,3 mi → 313,0 mi (19%); AALR3 112,7 mi → 126,5 mi (12%); AZTE3 26,4 mi → 24,0 mi (-9%); AZEV4 75,6 mi → 69,0 mi (-9%); IFCM3 25,7 mi → 23,4 mi (-9%); BIOM3 793,7 mi → 729,4 mi (-8%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 15 | 2 |
| Liquidez diária (R$) | 355 | 0,6% | 37 | 8 |
| Volatilidade 1 ano (%) | 323 | 0,1% | 0 | 0 |
| Maior queda 1 ano (%) | 346 | 0,0% | 28 | 0 |
| DY 12 meses (%) | 382 | 0,3% | 10 | 1 |
| P/VP | 469 | 0,1% | 15 | 2 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 201 | 6,4% | 7,8% | 75 |
| 2 meses so dias com negocio | 201 | 6,9% | 8,1% | 80 |
| 21 pregoes | 201 | 5,2% | 14,3% | 129 |
| 42 pregoes | 201 | 0,0% | 0,6% | 7 |
| 63 pregoes | 201 | -6,9% | 9,5% | 90 |

### O que muda no resultado do método

Ranqueados: 57 antes, 58 depois. Entraram 1, saíram 0, continuaram 57.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| HREC11 | Liquidez média diária R$ 0,49 mi abaixo de R$ 0,5 mi | 19º (papel) |

**Top 12 fof**: 12 de 12 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | JSAF11 | CPTS11 |
| 3 | RBRX11 | RBRX11 |
| 4 | CPTS11 | JSAF11 |
| 5 | BTHF11 | HFOF11 |
| 6 | HFOF11 | BTHF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | RINV11 | RINV11 |
| 9 | GARE11 | GARE11 |
| 10 | SNEL11 | SNEL11 |
| 11 | RZLC11 | RZLC11 |
| 12 | SEED11 | SEED11 |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | RZAK11 | RZAK11 |
| 4 | VGIP11 | VGIP11 |
| 5 | RECR11 | RECR11 |
| 6 | VGIR11 | VRTA11 |
| 7 | VRTA11 | VGIR11 |
| 8 | RBRY11 | RBRR11 |
| 9 | RBRR11 | RBRY11 |
| 10 | BTCI11 | CLIN11 |
| 11 | PORD11 | BTCI11 |
| 12 | CLIN11 | PORD11 |
| 13 | ICRI11 | ICRI11 |
| 14 | XPCI11 | XPCI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNIP11 | KNIP11 |
| 17 | KNHY11 | KNHY11 |
| 18 | MCCI11 | MCCI11 |
| 19 | KNUQ11 | HREC11 (novo) |
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
| 11 | LVBI11 | HGRU11 |
| 12 | HGRU11 | KNHF11 |
| 13 | KNHF11 | LVBI11 |
| 14 | BRCO11 | TJKB11 |
| 15 | XPLG11 | HGBS11 |
| 16 | HGBS11 | BRCO11 |
| 17 | TJKB11 | XPLG11 |
| 18 | PMLL11 | KNRI11 |
| 19 | KNRI11 | PMLL11 |
| 20 | HGLG11 | HGLG11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: KNRE11 0,25 → 0,17 (-32%); SJAU11 0,70 → 0,89 (27%); RBTS11 201,50 → 178,03 (-12%); MGHT11 12,60 → 11,18 (-11%); VOTS11 94,99 → 87,49 (-8%); TRNT11 129,99 → 120,00 (-8%); ARTE11 5,45 → 5,85 (7%); CYLD11 129,20 → 120,00 (-7%)

**Liquidez diária (R$)**: RZEO11 14.832 → 2,3 mi (15.081%); SNME11 168.273 → 336.507 (100%); BRIP11 374 → 606 (62%); TEPP11 3,4 mi → 2,2 mi (-37%); GLCR11 1.355 → 1.788 (32%); LSOP11 177.811 → 137.811 (-22%); FMOF11 1.317 → 1.596 (21%); MIDW11 3,5 mi → 4,2 mi (20%)

**Volatilidade 1 ano (%)**: NEXG11 28,5 → 27,2 (-5%); XPML11 14,9 → 15,6 (4%); RECM11 22,5 → 23,4 (4%); VGIR11 14,1 → 14,6 (4%); LSAG11 25,9 → 26,8 (4%); RZLC11 4,7 → 4,5 (-3%); VCRI11 16,4 → 16,9 (3%); FIGS11 16,6 → 17,0 (2%)

**Maior queda 1 ano (%)**: LSAG11 -25,2 → -30,1 (19%); BTLG11 -8,3 → -9,8 (19%); XPML11 -23,4 → -26,8 (15%); HOFC11 -19,4 → -21,9 (13%); HGCR11 -14,2 → -16,0 (13%); CPTR11 -22,1 → -24,9 (13%); RBTS11 -49,6 → -55,5 (12%); RZAK11 -19,4 → -21,5 (11%)

**DY 12 meses (%)**: KNRE11 0,49 → 0,73 (49%); RBTS11 3,11 → 3,52 (13%); VOTS11 13,86 → 15,05 (9%); ARTE11 23,30 → 21,71 (-7%); RECM11 12,50 → 13,33 (7%); CBOP11 8,37 → 8,92 (7%); CACR11 86,52 → 91,89 (6%); EMET11 13,47 → 12,73 (-6%)

**P/VP**: KNRE11 0,73 → 0,50 (-32%); SJAU11 0,05 → 0,06 (27%); RBTS11 0,82 → 0,72 (-12%); MGHT11 0,65 → 0,58 (-11%); VOTS11 1,08 → 0,99 (-8%); TRNT11 0,76 → 0,71 (-8%); ARTE11 0,53 → 0,57 (7%); CYLD11 1,07 → 0,99 (-7%)

