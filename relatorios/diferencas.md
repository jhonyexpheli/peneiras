# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-26 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-24 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | – | – | ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer')) |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 45 | 2 |
| Liquidez diária (R$) | 383 | 2,4% | 100 | 16 |
| Volatilidade 1 ano (%) | 394 | 0,1% | 3 | 0 |
| Maior queda 1 ano (%) | 400 | 0,0% | 4 | 1 |
| Valor de mercado (R$) | 582 | 0,2% | 45 | 2 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 262 | 9,1% | 12,5% | 153 |
| 2 meses so dias com negocio | 262 | 9,1% | 12,4% | 153 |
| 21 pregoes | 262 | -1,7% | 2,5% | 13 |
| 42 pregoes | 262 | 4,9% | 10,3% | 135 |
| 63 pregoes | 262 | -7,4% | 13,1% | 164 |

### O que muda no resultado do método

Ranqueados: 110 antes, 109 depois. Entraram 1, saíram 2, continuaram 108.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| MBRF3 | Volatilidade de 49.3% a.a. entre os 20% mais voláteis (corte em 49.0%) | 107º  |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| CSUD3 | 25º  | Liquidez média diária R$ 1 mi abaixo de R$ 1 mi |
| CAML3 | 88º  | Volatilidade de 49.1% a.a. entre os 20% mais voláteis (corte em 49.0%) |

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | LREN3 |
| 3 | LREN3 | ALLD3 |
| 4 | MDIA3 | MDIA3 |
| 5 | VLID3 | VLID3 |
| 6 | EUCA4 | BMGB4 |
| 7 | BLAU3 | EUCA4 |
| 8 | DEXP3 | DEXP3 |
| 9 | BMGB4 | ALOS3 |
| 10 | GMAT3 | BLAU3 |
| 11 | ALOS3 | GMAT3 |
| 12 | JHSF3 | JHSF3 |
| 13 | BBDC4 | ABCB4 |
| 14 | VIVA3 | VIVA3 |
| 15 | FESA4 | FESA4 |
| 16 | GOAU4 | GOAU4 |
| 17 | SYNE3 | SYNE3 |
| 18 | INTB3 | INTB3 |
| 19 | VALE3 | VALE3 |
| 20 | ABCB4 | GGBR4 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: CEGR3 57,00 → 97,00 (70%); UCAS3 0,93 → 1,15 (24%); EQPA7 7,58 → 6,50 (-14%); AALR3 0,74 → 0,64 (-14%); PLAS3 3,93 → 3,50 (-11%); NATU3 4,26 → 4,71 (11%); BRKM5 2,50 → 2,24 (-10%); PTBL3 1,28 → 1,40 (9%)

**Liquidez diária (R$)**: CEGR3 271 → 2.010 (640%); JOPA4 86 → 0 (-100%); EMAE4 13.349 → 0 (-100%); DOHL3 31 → 0 (-100%); ARND3 8.008 → 1.045 (-87%); BDLL3 346 → 155 (-55%); AFLT3 7.437 → 4.106 (-45%); EQPA7 74 → 105 (42%)

**Volatilidade 1 ano (%)**: UCAS3 47,3 → 51,4 (9%); SEER3 55,4 → 52,1 (-6%); CBAV3 22,7 → 21,5 (-5%); RAIL3 42,0 → 40,9 (-3%); AFLT3 53,1 → 51,9 (-2%); NATU3 49,9 → 50,9 (2%); AALR3 70,9 → 72,3 (2%); CLSC4 24,6 → 24,2 (-2%)

**Maior queda 1 ano (%)**: EQPA7 -24,5 → -35,3 (44%); MBRF3 -43,3 → -38,3 (-11%); BMGB4 -32,6 → -34,7 (6%); LAND3 -20,5 → -21,8 (6%); WHRL3 -37,5 → -39,2 (5%); VSTE3 -56,9 → -55,2 (-3%); HAGA3 -23,9 → -24,6 (3%); ENMT4 -53,5 → -54,9 (3%)

**Valor de mercado (R$)**: CEGR3 14,80 bi → 25,18 bi (70%); UCAS3 61,5 mi → 76,0 mi (24%); EQPA7 10,44 bi → 8,95 bi (-14%); AALR3 112,7 mi → 97,5 mi (-14%); PLAS3 48,8 mi → 43,5 mi (-11%); NATU3 5,86 bi → 6,47 bi (11%); BRKM5 1,99 bi → 1,79 bi (-10%); PTBL3 180,5 mi → 197,4 mi (9%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 18 | 1 |
| Liquidez diária (R$) | 355 | 0,7% | 35 | 10 |
| Volatilidade 1 ano (%) | 323 | 0,2% | 1 | 0 |
| Maior queda 1 ano (%) | 347 | 0,0% | 8 | 4 |
| DY 12 meses (%) | 382 | 0,5% | 15 | 1 |
| P/VP | 470 | 0,2% | 15 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 201 | 4,8% | 5,6% | 45 |
| 2 meses so dias com negocio | 201 | 4,9% | 5,8% | 51 |
| 21 pregoes | 201 | 4,7% | 14,7% | 120 |
| 42 pregoes | 201 | 0,3% | 0,7% | 5 |
| 63 pregoes | 201 | -6,6% | 9,2% | 95 |

### O que muda no resultado do método

Ranqueados: 61 antes, 61 depois. Entraram 1, saíram 1, continuaram 60.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| JSRE11 | Volatilidade de 23.2% a.a., entre os 20% mais voláteis do grupo tijolo (corte em 23.0%) | 3º (tijolo) |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| LIFE11 | 1º (tijolo) | Volatilidade de 23.3% a.a., entre os 20% mais voláteis do grupo tijolo (corte em 23.2%) |

**Top 14 fof**: 14 de 14 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | CPTS11 | RBRX11 |
| 3 | JSAF11 | CPTS11 |
| 4 | RBRX11 | JSAF11 |
| 5 | HFOF11 | HFOF11 |
| 6 | BTHF11 | BTHF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | GARE11 | GARE11 |
| 9 | RINV11 | RINV11 |
| 10 | HGBL11 | HGBL11 |
| 11 | RZLC11 | RZLC11 |
| 12 | SNEL11 | SNEL11 |
| 13 | SEED11 | SEED11 |
| 14 | SNME11 | SNME11 |

**Top 20 papel**: 18 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | RZAK11 | RZAK11 |
| 3 | VCJR11 | VCJR11 |
| 4 | VGIP11 | VGIP11 |
| 5 | RECR11 | VRTA11 |
| 6 | HSAF11 | RECR11 |
| 7 | VRTA11 | HSAF11 |
| 8 | VGIR11 | VGIR11 |
| 9 | BTCI11 | RBRR11 |
| 10 | RBRR11 | BTCI11 |
| 11 | PORD11 | PORD11 |
| 12 | RBRY11 | RBRY11 |
| 13 | CLIN11 | XPCI11 |
| 14 | XPCI11 | CLIN11 |
| 15 | KNIP11 | ICRI11 |
| 16 | HGCR11 | HGCR11 |
| 17 | ICRI11 | KNHY11 |
| 18 | KNHY11 | KNIP11 |
| 19 | MCCI11 | MXRF11 (novo) |
| 20 | KNSC11 | HREC11 (novo) |

**Top 20 tijolo**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | BRCR11 |
| 2 | BRCR11 | GTWR11 |
| 3 | GTWR11 | JSRE11 (novo) |
| 4 | TVRI11 | TVRI11 |
| 5 | HGRE11 | RCRB11 |
| 6 | RCRB11 | HGRE11 |
| 7 | RBRP11 | RBRP11 |
| 8 | VILG11 | VILG11 |
| 9 | FATN11 | FATN11 |
| 10 | TJKB11 | TJKB11 |
| 11 | CPSH11 | CPSH11 |
| 12 | HGBS11 | BRCO11 |
| 13 | KNHF11 | HGRU11 |
| 14 | HGRU11 | HGBS11 |
| 15 | BRCO11 | LVBI11 |
| 16 | XPLG11 | KNHF11 |
| 17 | LVBI11 | XPLG11 |
| 18 | KNRI11 | PMLL11 |
| 19 | PMLL11 | HGLG11 |
| 20 | HGLG11 | KNRI11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: HGAG11 19,95 → 13,00 (-35%); RZEO11 95,95 → 115,00 (20%); HUCG11 70,02 → 80,00 (14%); PMFO11 88,03 → 75,72 (-14%); HOFC11 29,30 → 32,90 (12%); NCRI11 6,70 → 6,06 (-10%); RBOP11 167,01 → 182,13 (9%); EMET11 9,16 → 9,94 (9%)

**Liquidez diária (R$)**: RZZI11 30.952 → 0 (-100%); VXXV11 4,2 mi → 7,7 mi (86%); PDBM11 14 → 3 (-81%); LSOP11 80.668 → 23.324 (-71%); PMFO11 12.281 → 20.480 (67%); CXRI11 58.414 → 26.752 (-54%); HBCR11 8,1 mi → 10,8 mi (33%); CPOF11 10,9 mi → 8,4 mi (-23%)

**Volatilidade 1 ano (%)**: DCRA11 24,0 → 25,4 (6%); NCRI11 35,3 → 36,7 (4%); RURA11 13,7 → 14,2 (4%); HOFC11 42,0 → 43,5 (4%); BTLG11 9,6 → 9,9 (4%); XPLG11 15,0 → 15,5 (4%); RZLC11 4,7 → 4,8 (3%); XPML11 15,6 → 16,1 (3%)

**Maior queda 1 ano (%)**: PMFO11 -8,3 → -17,1 (106%); NCRI11 -30,6 → -37,2 (22%); SNME11 -11,9 → -14,4 (21%); DCRA11 -28,9 → -34,7 (20%); JFLL11 -34,9 → -38,3 (10%); SPTW11 -43,3 → -47,6 (10%); GCRI11 -14,1 → -15,4 (10%); IAGR11 -21,9 → -23,1 (6%)

**DY 12 meses (%)**: RBIR11 14,11 → 19,50 (38%); PMFO11 11,64 → 13,40 (15%); HUCG11 11,53 → 10,10 (-12%); NCRI11 17,69 → 19,55 (11%); VOTS11 13,69 → 14,86 (9%); RBOP11 14,29 → 13,11 (-8%); SPTW11 23,32 → 25,21 (8%); EMET11 13,86 → 12,78 (-8%)

**P/VP**: HGAG11 0,85 → 0,55 (-35%); RZEO11 0,47 → 0,57 (20%); HUCG11 0,55 → 0,63 (14%); PMFO11 1,09 → 0,94 (-14%); HOFC11 0,48 → 0,54 (12%); NCRI11 0,67 → 0,61 (-10%); RBOP11 0,23 → 0,25 (9%); EMET11 1,01 → 1,09 (9%)

