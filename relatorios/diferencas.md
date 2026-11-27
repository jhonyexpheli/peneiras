# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-27 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-25 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | – | – | ('Connection aborted.', ConnectionResetError(104, 'Connection reset by peer')) |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,8% | 142 | 0 |
| Liquidez diária (R$) | 380 | 7,6% | 268 | 39 |
| Volatilidade 1 ano (%) | 394 | 0,3% | 2 | 0 |
| Maior queda 1 ano (%) | 400 | 0,0% | 2 | 0 |
| Valor de mercado (R$) | 582 | 0,8% | 142 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 261 | 9,6% | 13,1% | 159 |
| 2 meses so dias com negocio | 261 | 9,6% | 12,9% | 159 |
| 21 pregoes | 261 | -7,8% | 7,9% | 80 |
| 42 pregoes | 261 | 6,2% | 11,9% | 146 |
| 63 pregoes | 261 | -5,2% | 13,9% | 160 |

### O que muda no resultado do método

Ranqueados: 109 antes, 110 depois. Entraram 1, saíram 0, continuaram 109.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| TASA4 | Volatilidade de 49.1% a.a. entre os 20% mais voláteis (corte em 49.0%) | 78º  |

**Top 20**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | LREN3 | ALLD3 |
| 3 | ALLD3 | LREN3 |
| 4 | MDIA3 | MDIA3 |
| 5 | VLID3 | VLID3 |
| 6 | BMGB4 | EUCA4 |
| 7 | EUCA4 | DEXP3 |
| 8 | DEXP3 | BMGB4 |
| 9 | ALOS3 | GMAT3 |
| 10 | BLAU3 | ABCB4 |
| 11 | GMAT3 | BLAU3 |
| 12 | JHSF3 | JHSF3 |
| 13 | ABCB4 | ALOS3 |
| 14 | VIVA3 | VIVA3 |
| 15 | FESA4 | FESA4 |
| 16 | GOAU4 | GOAU4 |
| 17 | SYNE3 | SYNE3 |
| 18 | INTB3 | GGBR4 |
| 19 | VALE3 | VALE3 |
| 20 | GGBR4 | INTB3 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: AZTE3 0,60 → 0,72 (20%); PMAM3 0,18 → 0,21 (17%); RENT4 28,71 → 33,26 (16%); MRVE3 4,62 → 5,33 (15%); RENT3 29,32 → 33,77 (15%); SIMH3 5,97 → 6,85 (15%); AZEV3 13,10 → 15,00 (15%); LJQQ3 1,11 → 1,27 (14%)

**Liquidez diária (R$)**: MSPA4 157 → 0 (-100%); RPAD5 6.947 → 709 (-90%); FIEI3 350 → 52 (-85%); RSID3 7.989 → 14.090 (76%); FESA3 20.044 → 6.133 (-69%); HBTS5 1.751 → 621 (-65%); SOND5 7.029 → 2.667 (-62%); CBEE3 1.696 → 708 (-58%)

**Volatilidade 1 ano (%)**: BBAS3 33,4 → 35,4 (6%); RADL3 37,8 → 39,7 (5%); RENT4 48,3 → 50,6 (5%); RENT3 44,8 → 46,9 (5%); BBDC4 39,9 → 41,4 (4%); IGTI11 32,9 → 34,1 (4%); MULT3 31,8 → 32,8 (3%); LIGT3 52,4 → 54,2 (3%)

**Maior queda 1 ano (%)**: RSID3 -23,7 → -19,7 (-17%); MBRF3 -38,3 → -35,0 (-9%); OBTC3 -51,1 → -49,2 (-4%); ENGI3 -30,8 → -29,7 (-4%); DOTZ3 -61,8 → -59,6 (-3%); NEXP3 -39,9 → -38,8 (-3%); BEEF3 -63,5 → -62,0 (-2%); JFEN3 -70,3 → -68,9 (-2%)

**Valor de mercado (R$)**: AZTE3 24,0 mi → 28,8 mi (20%); PMAM3 759,2 mi → 885,7 mi (17%); RENT4 32,28 bi → 37,39 bi (16%); MRVE3 2,60 bi → 3,00 bi (15%); RENT3 32,96 bi → 37,97 bi (15%); SIMH3 3,49 bi → 4,00 bi (15%); AZEV3 1,46 bi → 1,67 bi (15%); LJQQ3 216,5 mi → 247,7 mi (14%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 19 | 1 |
| Liquidez diária (R$) | 354 | 0,8% | 38 | 6 |
| Volatilidade 1 ano (%) | 322 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 346 | 0,0% | 4 | 0 |
| DY 12 meses (%) | 382 | 0,4% | 12 | 0 |
| P/VP | 469 | 0,1% | 18 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 202 | 4,1% | 5,0% | 35 |
| 2 meses so dias com negocio | 202 | 4,6% | 5,3% | 44 |
| 21 pregoes | 202 | -0,2% | 14,8% | 128 |
| 42 pregoes | 202 | 0,3% | 0,8% | 8 |
| 63 pregoes | 202 | -7,2% | 9,4% | 98 |

### O que muda no resultado do método

Ranqueados: 61 antes, 61 depois. Entraram 0, saíram 0, continuaram 61.

**Top 14 fof**: 14 de 14 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | RBRX11 | CPTS11 |
| 3 | CPTS11 | RBRX11 |
| 4 | JSAF11 | JSAF11 |
| 5 | HFOF11 | BTHF11 |
| 6 | BTHF11 | HFOF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | GARE11 | GARE11 |
| 9 | RINV11 | RINV11 |
| 10 | HGBL11 | HGBL11 |
| 11 | RZLC11 | RZLC11 |
| 12 | SNEL11 | SNEL11 |
| 13 | SEED11 | SNME11 |
| 14 | SNME11 | SEED11 |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | RZAK11 | RZAK11 |
| 3 | VCJR11 | VCJR11 |
| 4 | VGIP11 | VGIP11 |
| 5 | VRTA11 | RECR11 |
| 6 | RECR11 | HSAF11 |
| 7 | HSAF11 | VRTA11 |
| 8 | VGIR11 | VGIR11 |
| 9 | RBRR11 | RBRR11 |
| 10 | BTCI11 | PORD11 |
| 11 | PORD11 | RBRY11 |
| 12 | RBRY11 | BTCI11 |
| 13 | XPCI11 | CLIN11 |
| 14 | CLIN11 | XPCI11 |
| 15 | ICRI11 | ICRI11 |
| 16 | HGCR11 | HGCR11 |
| 17 | KNHY11 | KNIP11 |
| 18 | KNIP11 | HREC11 |
| 19 | MXRF11 | KNHY11 |
| 20 | HREC11 | MCCI11 (novo) |

**Top 20 tijolo**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRCR11 | BRCR11 |
| 2 | GTWR11 | GTWR11 |
| 3 | JSRE11 | TVRI11 |
| 4 | TVRI11 | JSRE11 |
| 5 | RCRB11 | HGRE11 |
| 6 | HGRE11 | RCRB11 |
| 7 | RBRP11 | RBRP11 |
| 8 | VILG11 | VILG11 |
| 9 | FATN11 | FATN11 |
| 10 | TJKB11 | TJKB11 |
| 11 | CPSH11 | HGBS11 |
| 12 | BRCO11 | CPSH11 |
| 13 | HGRU11 | HGRU11 |
| 14 | HGBS11 | BRCO11 |
| 15 | LVBI11 | KNHF11 |
| 16 | KNHF11 | LVBI11 |
| 17 | XPLG11 | XPLG11 |
| 18 | PMLL11 | PMLL11 |
| 19 | HGLG11 | HGLG11 |
| 20 | KNRI11 | KNRI11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: KNRE11 0,22 → 0,27 (23%); CTXT11 3,68 → 4,27 (16%); ONDA11 6,08 → 6,90 (13%); CACR11 8,38 → 9,47 (13%); ZAGH11 7,00 → 6,30 (-10%); NCRI11 6,06 → 6,66 (10%); HOFC11 32,90 → 30,01 (-9%); ERPA11 125,49 → 115,03 (-8%)

**Liquidez diária (R$)**: GLPF11 33.344 → 77.929 (134%); RBLG11 4 → 0 (-100%); VXXV11 7,7 mi → 11,3 mi (47%); HBCR11 10,8 mi → 14,4 mi (34%); CXRI11 26.752 → 18.791 (-30%); ADSH11 1,2 mi → 1,5 mi (28%); CXTL11 3.862 → 4.502 (17%); LSOP11 23.324 → 19.525 (-16%)

**Volatilidade 1 ano (%)**: VRTM11 17,2 → 18,5 (8%); GFDL11 1,4 → 1,5 (6%); VGIA11 22,6 → 23,4 (4%); ONDA11 50,4 → 52,1 (3%); BTCI11 17,1 → 17,7 (3%); NCRI11 36,7 → 37,9 (3%); KNRE11 87,2 → 89,6 (3%); JFLL11 23,5 → 22,9 (-3%)

**Maior queda 1 ano (%)**: RSPD11 -43,5 → -37,3 (-14%); ZAGH11 -38,2 → -42,7 (12%); ERPA11 -45,4 → -50,0 (10%); SNME11 -14,4 → -15,4 (7%); HGIC11 -45,8 → -47,7 (4%); ZAVC11 -15,5 → -15,1 (-3%); RBIR11 -33,1 → -33,9 (2%); BNFS11 -60,1 → -60,9 (1%)

**DY 12 meses (%)**: KNRE11 0,56 → 0,46 (-18%); ONDA11 19,00 → 16,74 (-12%); CACR11 91,89 → 81,31 (-12%); ZAGH11 7,00 → 7,78 (11%); ERPA11 8,87 → 9,68 (9%); NCRI11 19,55 → 17,79 (-9%); CNES11 4,67 → 4,32 (-7%); VRTM11 20,65 → 19,29 (-7%)

**P/VP**: KNRE11 0,65 → 0,79 (23%); CTXT11 0,25 → 0,29 (16%); CACR11 0,09 → 0,11 (13%); ZAGH11 0,82 → 0,74 (-10%); NCRI11 0,61 → 0,67 (10%); HOFC11 0,54 → 0,49 (-9%); ERPA11 0,76 → 0,69 (-8%); CNES11 0,24 → 0,26 (8%)

