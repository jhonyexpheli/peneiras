# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-13 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-11 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,54 | 2026-11-11 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 51 | 4 |
| Liquidez diária (R$) | 380 | 2,2% | 102 | 12 |
| Volatilidade 1 ano (%) | 390 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 396 | 0,0% | 8 | 2 |
| Valor de mercado (R$) | 582 | 0,2% | 51 | 4 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 268 | 4,5% | 6,9% | 98 |
| 2 meses so dias com negocio | 268 | 4,6% | 6,9% | 98 |
| 21 pregoes | 268 | -1,6% | 2,2% | 12 |
| 42 pregoes | 268 | -8,4% | 10,8% | 146 |
| 63 pregoes | 268 | -18,9% | 20,4% | 215 |

### O que muda no resultado do método

Ranqueados: 110 antes, 110 depois. Entraram 0, saíram 0, continuaram 110.

**Top 20**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | ALLD3 |
| 3 | LREN3 | LREN3 |
| 4 | VLID3 | VLID3 |
| 5 | MDIA3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | GMAT3 | GMAT3 |
| 8 | ABCB4 | ABCB4 |
| 9 | BMGB4 | BMGB4 |
| 10 | BLAU3 | BLAU3 |
| 11 | JHSF3 | ALOS3 |
| 12 | ALOS3 | JHSF3 |
| 13 | DEXP3 | DEXP3 |
| 14 | GOAU4 | GOAU4 |
| 15 | GGBR4 | VIVA3 |
| 16 | SYNE3 | GGBR4 |
| 17 | BBDC4 | SYNE3 |
| 18 | VIVA3 | CSUD3 |
| 19 | CSUD3 | FESA4 |
| 20 | FESA4 | BBDC4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: OSXB3 1,47 → 2,23 (52%); UCAS3 0,94 → 0,70 (-26%); CASN3 6,00 → 4,56 (-24%); AMER3 5,07 → 4,05 (-20%); HAPV3 4,63 → 5,32 (15%); CRPG6 8,97 → 8,00 (-11%); MELK3 2,29 → 2,06 (-10%); CEED3 10,00 → 9,00 (-10%)

**Liquidez diária (R$)**: UCAS3 31.095 → 77.825 (150%); CEDO3 33 → 0 (-100%); ESTR4 477 → 247 (-48%); RCSL3 230.259 → 133.546 (-42%); MNDL3 16.207 → 10.494 (-35%); SOND6 3.710 → 2.430 (-35%); FIEI3 2.507 → 1.714 (-32%); FESA3 30.180 → 21.956 (-27%)

**Volatilidade 1 ano (%)**: BRAP3 25,4 → 27,0 (7%); AMER3 67,6 → 71,2 (5%); VULC3 39,7 → 37,8 (-5%); CEBR3 28,6 → 27,5 (-4%); WHRL3 27,6 → 28,6 (4%); BBAS3 32,0 → 33,2 (4%); SLCE3 28,8 → 29,8 (3%); MELK3 41,4 → 42,6 (3%)

**Maior queda 1 ano (%)**: CASN3 -1,8 → -25,4 (1.309%); UCAS3 -40,9 → -56,0 (37%); WHRL3 -29,9 → -32,8 (10%); BNBR3 -17,1 → -18,7 (10%); MELK3 -46,5 → -50,4 (8%); BRAP3 -23,4 → -25,3 (8%); BBAS3 -41,3 → -43,9 (6%); HAGA3 -22,7 → -23,9 (6%)

**Valor de mercado (R$)**: OSXB3 4,6 mi → 7,0 mi (52%); UCAS3 62,1 mi → 46,3 mi (-26%); CASN3 6,90 bi → 5,25 bi (-24%); AMER3 1,02 bi → 811,0 mi (-20%); HAPV3 2,33 bi → 2,67 bi (15%); CRPG6 332,8 mi → 296,8 mi (-11%); MELK3 472,4 mi → 424,9 mi (-10%); CEED3 684,2 mi → 615,8 mi (-10%)

## Peneira FIIs

Universo: 575 antes, 576 depois (575 em comum; só na base nova: ).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 575 | 0,0% | 16 | 0 |
| Liquidez diária (R$) | 358 | 0,7% | 55 | 20 |
| Volatilidade 1 ano (%) | 323 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 349 | 0,0% | 16 | 2 |
| DY 12 meses (%) | 381 | 0,3% | 16 | 1 |
| P/VP | 469 | 0,2% | 15 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 199 | 9,5% | 11,8% | 115 |
| 2 meses so dias com negocio | 199 | 10,6% | 12,5% | 121 |
| 21 pregoes | 199 | 5,0% | 14,2% | 119 |
| 42 pregoes | 199 | -0,0% | 0,6% | 6 |
| 63 pregoes | 199 | -4,9% | 8,9% | 91 |

### O que muda no resultado do método

Ranqueados: 57 antes, 58 depois. Entraram 1, saíram 0, continuaram 57.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| SEED11 | Liquidez média diária R$ 0 mi abaixo de R$ 0,5 mi | 12º (fof) |

**Top 11 fof**: 11 de 11 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | JSAF11 | JSAF11 |
| 3 | RBRX11 | RBRX11 |
| 4 | CPTS11 | CPTS11 |
| 5 | BTHF11 | BTHF11 |
| 6 | HFOF11 | HFOF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | GARE11 | GARE11 |
| 9 | RINV11 | RINV11 |
| 10 | RZLC11 | RZLC11 |
| 11 | SNEL11 | SNEL11 |
| 12 |  | SEED11 (novo) |

**Top 20 papel**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | RZAK11 | RZAK11 |
| 4 | RECR11 | VGIP11 |
| 5 | VGIP11 | VRTA11 |
| 6 | VRTA11 | RECR11 |
| 7 | RBRR11 | RBRY11 |
| 8 | VGIR11 | VGIR11 |
| 9 | RBRY11 | RBRR11 |
| 10 | CLIN11 | BTCI11 |
| 11 | BTCI11 | PORD11 |
| 12 | PORD11 | CLIN11 |
| 13 | XPCI11 | XPCI11 |
| 14 | ICRI11 | ICRI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNHY11 | KNIP11 |
| 17 | KNIP11 | KNHY11 |
| 18 | KNSC11 | KNSC11 |
| 19 | KNUQ11 | KNUQ11 |
| 20 | MCCI11 | MCCI11 |

**Top 20 tijolo**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | GTWR11 | GTWR11 |
| 3 | JSRE11 | JSRE11 |
| 4 | RBVA11 | RBVA11 |
| 5 | TVRI11 | TVRI11 |
| 6 | RBRP11 | RBRP11 |
| 7 | RCRB11 | RCRB11 |
| 8 | HGRE11 | HGRE11 |
| 9 | VILG11 | FATN11 |
| 10 | FATN11 | VILG11 |
| 11 | XPML11 | XPML11 |
| 12 | HGBS11 | CPSH11 |
| 13 | CPSH11 | HGBS11 |
| 14 | LVBI11 | LVBI11 |
| 15 | KNHF11 | KNHF11 |
| 16 | HGRU11 | HGRU11 |
| 17 | BRCO11 | BRCO11 |
| 18 | XPLG11 | XPLG11 |
| 19 | HGLG11 | HGLG11 |
| 20 | KNRI11 | KNRI11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: CTXT11 3,45 → 4,01 (16%); IBCR11 37,29 → 32,00 (-14%); VVRI11 7,25 → 8,25 (14%); HUSC11 90,01 → 99,94 (11%); APTO11 4,89 → 4,40 (-10%); OCRE11 74,99 → 68,00 (-9%); FIIP11 152,96 → 140,08 (-8%); ICDI11 94,53 → 87,00 (-8%)

**Liquidez diária (R$)**: SEED11 5 → 596.910 (12,5 mi%); RZEO11 423 → 14.482 (3.326%); BLCA11 10.581 → 260.707 (2.364%); VVDI11 2.422 → 50.040 (1.966%); BMLC11 2.747 → 28.173 (926%); BLMO11 39.487 → 233.500 (491%); REME11 345.716 → 0 (-100%); NAVT11 31.359 → 0 (-100%)

**Volatilidade 1 ano (%)**: APTO11 25,0 → 27,0 (8%); IBCR11 36,9 → 39,9 (8%); FIIP11 28,2 → 29,5 (5%); PATC11 14,6 → 15,1 (3%); HAAA11 73,4 → 71,2 (-3%); CTXT11 62,2 → 64,0 (3%); HUSC11 43,2 → 44,5 (3%); TRXF11 20,9 → 21,4 (2%)

**Maior queda 1 ano (%)**: ICDI11 -5,8 → -13,3 (128%); IBCR11 -34,5 → -43,8 (27%); ARXD11 -18,2 → -21,2 (16%); APTO11 -44,8 → -50,3 (12%); RINV11 -11,5 → -12,7 (10%); HFOF11 -19,1 → -21,0 (10%); XPML11 -18,5 → -20,1 (9%); HOFC11 -15,6 → -16,9 (8%)

**DY 12 meses (%)**: RZLC11 14,50 → 11,39 (-21%); INHF11 6,07 → 4,94 (-19%); VVRI11 3,59 → 3,15 (-12%); APTO11 19,83 → 22,03 (11%); IBCR11 18,37 → 20,31 (11%); OCRE11 6,35 → 7,00 (10%); HUSC11 13,67 → 12,32 (-10%); FIIP11 11,07 → 12,09 (9%)

**P/VP**: CTXT11 0,23 → 0,27 (16%); IBCR11 0,42 → 0,36 (-14%); VVRI11 0,83 → 0,95 (14%); HUSC11 0,45 → 0,50 (11%); APTO11 0,63 → 0,56 (-10%); OCRE11 0,57 → 0,51 (-9%); FIIP11 0,76 → 0,70 (-8%); ICDI11 0,95 → 0,87 (-8%)

