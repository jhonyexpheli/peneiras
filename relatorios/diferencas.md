# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-25 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-23 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | – | – | ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer')) |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 35 | 1 |
| Liquidez diária (R$) | 381 | 1,7% | 91 | 15 |
| Volatilidade 1 ano (%) | 393 | 0,1% | 0 | 0 |
| Maior queda 1 ano (%) | 399 | 0,0% | 9 | 1 |
| Valor de mercado (R$) | 582 | 0,2% | 35 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 262 | 8,8% | 11,8% | 150 |
| 2 meses so dias com negocio | 262 | 8,8% | 11,8% | 148 |
| 21 pregoes | 262 | -0,9% | 1,7% | 12 |
| 42 pregoes | 262 | 3,3% | 9,3% | 119 |
| 63 pregoes | 262 | -8,9% | 14,2% | 171 |

### O que muda no resultado do método

Ranqueados: 110 antes, 110 depois. Entraram 1, saíram 1, continuaram 109.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| CAML3 | Volatilidade de 49.0% a.a. entre os 20% mais voláteis (corte em 48.9%) | 88º  |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| SOJA3 | 70º  | Volatilidade de 49.1% a.a. entre os 20% mais voláteis (corte em 49.0%) |

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | ALLD3 |
| 3 | LREN3 | LREN3 |
| 4 | VLID3 | MDIA3 |
| 5 | MDIA3 | VLID3 |
| 6 | EUCA4 | EUCA4 |
| 7 | DEXP3 | BLAU3 |
| 8 | ALOS3 | DEXP3 |
| 9 | BMGB4 | BMGB4 |
| 10 | GMAT3 | GMAT3 |
| 11 | BLAU3 | ALOS3 |
| 12 | JHSF3 | JHSF3 |
| 13 | BBDC4 | BBDC4 |
| 14 | VIVA3 | VIVA3 |
| 15 | GOAU4 | FESA4 |
| 16 | FESA4 | GOAU4 |
| 17 | BRBI11 | SYNE3 |
| 18 | SYNE3 | INTB3 |
| 19 | INTB3 | VALE3 (novo) |
| 20 | ABCB4 | ABCB4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: FASA3 0,22 → 6,51 (2.859%); AZEV3 11,95 → 14,01 (17%); BRKM3 3,80 → 3,24 (-15%); BRKM5 2,91 → 2,50 (-14%); AALR3 0,86 → 0,74 (-14%); OSXB3 1,31 → 1,16 (-11%); TOKY3 3,70 → 3,31 (-11%); PMAM3 0,19 → 0,17 (-11%)

**Liquidez diária (R$)**: EQPA7 38 → 74 (95%); BAUH4 13.133 → 21.737 (66%); USIM6 241 → 84 (-65%); EQPA5 560 → 199 (-65%); FIEI3 860 → 491 (-43%); EALT3 2.465 → 3.377 (37%); LUPA3 99.963 → 67.486 (-32%); OSXB3 3.519 → 2.497 (-29%)

**Volatilidade 1 ano (%)**: LPSB3 56,8 → 54,7 (-4%); MDIA3 36,5 → 37,7 (3%); GMAT3 47,3 → 46,0 (-3%); MBRF3 50,6 → 49,3 (-3%); BRKM3 70,4 → 71,9 (2%); AALR3 69,4 → 70,9 (2%); CMIG4 27,3 → 26,8 (-2%); VALE3 29,0 → 29,6 (2%)

**Maior queda 1 ano (%)**: EQPA7 -20,2 → -24,5 (21%); ALLD3 -55,4 → -48,5 (-12%); BRAP3 -29,5 → -33,0 (12%); VALE3 -35,2 → -38,7 (10%); BRSR3 -24,2 → -26,7 (10%); BRAP4 -35,3 → -38,2 (8%); PSSA3 -22,6 → -24,4 (8%); BMGB4 -30,8 → -32,6 (6%)

**Valor de mercado (R$)**: FASA3 9,6 mi → 285,5 mi (2.859%); AZEV3 1,33 bi → 1,56 bi (17%); BRKM3 2,90 bi → 2,47 bi (-15%); BRKM5 2,32 bi → 1,99 bi (-14%); AALR3 131,0 mi → 112,7 mi (-14%); OSXB3 4,1 mi → 3,7 mi (-11%); TOKY3 10,0 mi → 9,0 mi (-11%); PMAM3 801,3 mi → 717,0 mi (-11%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 17 | 3 |
| Liquidez diária (R$) | 355 | 0,6% | 37 | 11 |
| Volatilidade 1 ano (%) | 323 | 0,1% | 0 | 0 |
| Maior queda 1 ano (%) | 347 | 0,0% | 12 | 4 |
| DY 12 meses (%) | 382 | 0,4% | 14 | 5 |
| P/VP | 470 | 0,2% | 15 | 3 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 201 | 5,0% | 6,5% | 50 |
| 2 meses so dias com negocio | 201 | 5,8% | 7,0% | 55 |
| 21 pregoes | 201 | 5,7% | 14,5% | 124 |
| 42 pregoes | 201 | 0,0% | 0,6% | 9 |
| 63 pregoes | 201 | -6,5% | 9,4% | 95 |

### O que muda no resultado do método

Ranqueados: 60 antes, 61 depois. Entraram 1, saíram 0, continuaram 60.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| HSAF11 | Liquidez média diária R$ 0,47 mi abaixo de R$ 0,5 mi | 6º (papel) |

**Top 14 fof**: 14 de 14 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | RBRX11 | CPTS11 |
| 3 | CPTS11 | JSAF11 |
| 4 | JSAF11 | RBRX11 |
| 5 | HFOF11 | HFOF11 |
| 6 | BTHF11 | BTHF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | GARE11 | GARE11 |
| 9 | RINV11 | RINV11 |
| 10 | SNEL11 | HGBL11 |
| 11 | HGBL11 | RZLC11 |
| 12 | RZLC11 | SNEL11 |
| 13 | SEED11 | SEED11 |
| 14 | SNME11 | SNME11 |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | RZAK11 | RZAK11 |
| 3 | VCJR11 | VCJR11 |
| 4 | RECR11 | VGIP11 |
| 5 | VGIP11 | RECR11 |
| 6 | VRTA11 | HSAF11 (novo) |
| 7 | VGIR11 | VRTA11 |
| 8 | PORD11 | VGIR11 |
| 9 | BTCI11 | BTCI11 |
| 10 | RBRY11 | RBRR11 |
| 11 | RBRR11 | PORD11 |
| 12 | XPCI11 | RBRY11 |
| 13 | CLIN11 | CLIN11 |
| 14 | ICRI11 | XPCI11 |
| 15 | HGCR11 | KNIP11 |
| 16 | KNIP11 | HGCR11 |
| 17 | KNHY11 | ICRI11 |
| 18 | MCCI11 | KNHY11 |
| 19 | KNSC11 | MCCI11 |
| 20 | MXRF11 | KNSC11 |

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
| 10 | CPSH11 | TJKB11 |
| 11 | TJKB11 | CPSH11 |
| 12 | LVBI11 | HGBS11 |
| 13 | HGBS11 | KNHF11 |
| 14 | HGRU11 | HGRU11 |
| 15 | BRCO11 | BRCO11 |
| 16 | KNHF11 | XPLG11 |
| 17 | XPLG11 | LVBI11 |
| 18 | KNRI11 | KNRI11 |
| 19 | PMLL11 | PMLL11 |
| 20 | HGLG11 | HGLG11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: VVRI11 6,60 → 8,88 (35%); CARE11 3,09 → 4,00 (29%); KNRE11 0,17 → 0,22 (29%); HUCG11 84,40 → 70,02 (-17%); RRES11 11,50 → 10,00 (-13%); CACR11 7,75 → 8,68 (12%); VOTS11 87,49 → 96,19 (10%); JASC11 109,27 → 100,00 (-8%)

**Liquidez diária (R$)**: RRES11 24 → 84 (245%); FAED11 61.066 → 182.345 (199%); HUCG11 783 → 1.647 (110%); ADSH11 2,3 mi → 1,1 mi (-54%); SPG211 1.366 → 1.957 (43%); LSOP11 137.811 → 80.668 (-41%); RBRI11 132 → 83 (-37%); GRWA11 7.735 → 9.613 (24%)

**Volatilidade 1 ano (%)**: RZAT11 16,7 → 17,6 (5%); HUCG11 64,4 → 67,1 (4%); RBVA11 16,4 → 16,9 (3%); FAED11 16,0 → 16,5 (3%); RZLC11 4,5 → 4,7 (3%); NEXG11 27,9 → 28,7 (3%); BTRA11 24,0 → 24,6 (2%); SEQR11 18,6 → 19,0 (2%)

**Maior queda 1 ano (%)**: RRES11 -2,0 → -13,0 (552%); RZLC11 -1,3 → -1,8 (36%); HUCG11 -23,5 → -31,4 (33%); SNME11 -9,6 → -11,9 (24%); VVMR11 -13,3 → -15,5 (17%); FLMA11 -11,2 → -12,7 (14%); DCRA11 -25,8 → -28,9 (12%); SNCI11 -14,8 → -16,3 (11%)

**DY 12 meses (%)**: LSOP11 2,27 → 3,41 (50%); RBIR11 19,23 → 14,11 (-27%); VVRI11 2,27 → 1,69 (-26%); KNRE11 0,73 → 0,56 (-23%); HUCG11 9,57 → 11,53 (20%); RRES11 8,58 → 9,87 (15%); CACR11 99,35 → 88,71 (-11%); JASC11 7,87 → 8,60 (9%)

**P/VP**: VVRI11 0,77 → 1,03 (35%); CARE11 0,09 → 0,12 (29%); KNRE11 0,50 → 0,65 (29%); HUCG11 0,66 → 0,55 (-17%); CACR11 0,09 → 0,10 (12%); VOTS11 0,99 → 1,09 (10%); JASC11 0,95 → 0,87 (-8%); NEXG11 1,20 → 1,28 (7%)

