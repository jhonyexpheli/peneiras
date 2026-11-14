# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-14 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-12 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,55 | 2026-11-12 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,2% | 40 | 0 |
| Liquidez diária (R$) | 381 | 2,2% | 70 | 5 |
| Volatilidade 1 ano (%) | 391 | 0,1% | 3 | 0 |
| Maior queda 1 ano (%) | 397 | 0,0% | 6 | 0 |
| Valor de mercado (R$) | 582 | 0,2% | 40 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 268 | 5,8% | 8,2% | 112 |
| 2 meses so dias com negocio | 268 | 5,8% | 8,2% | 111 |
| 21 pregoes | 268 | -1,6% | 2,2% | 8 |
| 42 pregoes | 268 | -5,9% | 9,7% | 130 |
| 63 pregoes | 268 | -16,8% | 19,0% | 208 |

### O que muda no resultado do método

Ranqueados: 110 antes, 110 depois. Entraram 1, saíram 1, continuaram 109.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| BEEF3 | Volatilidade de 49.5% a.a. entre os 20% mais voláteis (corte em 48.6%) | 81º  |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| ALPK3 | 96º  | Liquidez média diária R$ 1 mi abaixo de R$ 1 mi |

**Top 20**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | LREN3 |
| 3 | LREN3 | ALLD3 |
| 4 | VLID3 | VLID3 |
| 5 | MDIA3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | GMAT3 | GMAT3 |
| 8 | ABCB4 | BMGB4 |
| 9 | BMGB4 | BLAU3 |
| 10 | BLAU3 | ALOS3 |
| 11 | ALOS3 | JHSF3 |
| 12 | JHSF3 | ABCB4 |
| 13 | DEXP3 | DEXP3 |
| 14 | GOAU4 | VIVA3 |
| 15 | VIVA3 | GOAU4 |
| 16 | GGBR4 | FESA4 |
| 17 | SYNE3 | SYNE3 |
| 18 | CSUD3 | GGBR4 |
| 19 | FESA4 | BBDC4 |
| 20 | BBDC4 | CSUD3 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: ALLD3 5,95 → 7,13 (20%); MAPT4 2,50 → 2,01 (-20%); AALR3 1,61 → 1,31 (-19%); JALL3 2,18 → 2,49 (14%); PDTC3 1,59 → 1,80 (13%); AGXY3 0,23 → 0,20 (-13%); UCAS3 0,70 → 0,79 (13%); EVEN3 3,23 → 3,63 (12%)

**Liquidez diária (R$)**: FIGE3 157 → 0 (-100%); BALM3 3.771 → 1.152 (-69%); WLMM3 620 → 998 (61%); VIVR3 415.036 → 313.270 (-25%); CGAS3 8.695 → 6.920 (-20%); RCSL3 133.546 → 106.961 (-20%); NEXP3 933 → 1.115 (20%); BRSR5 880 → 708 (-19%)

**Volatilidade 1 ano (%)**: ALLD3 39,5 → 43,4 (10%); PASS3 34,8 → 37,1 (6%); MNPR3 46,2 → 43,8 (-5%); AALR3 63,6 → 66,7 (5%); FHER3 41,3 → 43,2 (5%); FESA4 42,6 → 40,9 (-4%); UCAS3 44,2 → 45,9 (4%); AGXY3 47,9 → 49,7 (4%)

**Maior queda 1 ano (%)**: MNPR3 -39,4 → -33,6 (-15%); UNIP3 -24,6 → -26,3 (7%); AALR3 -71,2 → -75,7 (6%); CGRA4 -34,9 → -36,8 (5%); ENMT4 -49,9 → -52,5 (5%); CASH3 -33,3 → -35,0 (5%); UNIP5 -31,4 → -32,7 (4%); WHRL3 -32,8 → -33,9 (3%)

**Valor de mercado (R$)**: ALLD3 571,0 mi → 684,2 mi (20%); MAPT4 2,3 mi → 1,9 mi (-20%); AALR3 245,3 mi → 199,6 mi (-19%); JALL3 661,7 mi → 755,8 mi (14%); PDTC3 126,4 mi → 143,0 mi (13%); AGXY3 4,6 mi → 4,0 mi (-13%); UCAS3 46,3 mi → 52,2 mi (13%); EVEN3 646,0 mi → 726,0 mi (12%)

## Peneira FIIs

Universo: 576 antes, 576 depois (575 em comum; só na base nova: STRY11; só na base antiga: ).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 575 | 0,0% | 20 | 0 |
| Liquidez diária (R$) | 357 | 0,8% | 27 | 6 |
| Volatilidade 1 ano (%) | 323 | 0,1% | 4 | 0 |
| Maior queda 1 ano (%) | 349 | 0,0% | 10 | 0 |
| DY 12 meses (%) | 381 | 0,3% | 20 | 4 |
| P/VP | 469 | 0,1% | 19 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 202 | 9,2% | 11,0% | 112 |
| 2 meses so dias com negocio | 202 | 10,7% | 11,9% | 118 |
| 21 pregoes | 202 | 5,2% | 12,9% | 124 |
| 42 pregoes | 202 | -0,0% | 0,9% | 5 |
| 63 pregoes | 202 | -4,4% | 9,2% | 94 |

### O que muda no resultado do método

Ranqueados: 58 antes, 58 depois. Entraram 0, saíram 0, continuaram 58.

**Top 12 fof**: 12 de 12 continuam.

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
| 12 | SEED11 | SEED11 |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | RZAK11 | VGIP11 |
| 4 | VGIP11 | RECR11 |
| 5 | VRTA11 | RZAK11 |
| 6 | RECR11 | VRTA11 |
| 7 | RBRY11 | VGIR11 |
| 8 | VGIR11 | RBRR11 |
| 9 | RBRR11 | RBRY11 |
| 10 | BTCI11 | BTCI11 |
| 11 | PORD11 | PORD11 |
| 12 | CLIN11 | CLIN11 |
| 13 | XPCI11 | ICRI11 |
| 14 | ICRI11 | XPCI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNIP11 | KNIP11 |
| 17 | KNHY11 | KNHY11 |
| 18 | KNSC11 | MCCI11 |
| 19 | KNUQ11 | KNSC11 |
| 20 | MCCI11 | MXRF11 (novo) |

**Top 20 tijolo**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | GTWR11 | GTWR11 |
| 3 | JSRE11 | TVRI11 |
| 4 | RBVA11 | JSRE11 |
| 5 | TVRI11 | RBVA11 |
| 6 | RBRP11 | RBRP11 |
| 7 | RCRB11 | HGRE11 |
| 8 | HGRE11 | RCRB11 |
| 9 | FATN11 | VILG11 |
| 10 | VILG11 | FATN11 |
| 11 | XPML11 | XPML11 |
| 12 | CPSH11 | HGBS11 |
| 13 | HGBS11 | KNHF11 |
| 14 | LVBI11 | CPSH11 |
| 15 | KNHF11 | HGRU11 |
| 16 | HGRU11 | LVBI11 |
| 17 | BRCO11 | BRCO11 |
| 18 | XPLG11 | HGLG11 |
| 19 | HGLG11 | XPLG11 |
| 20 | KNRI11 | PMLL11 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: RRES11 9,99 → 11,50 (15%); DAMA11 4,76 → 4,12 (-13%); MGHT11 11,01 → 12,24 (11%); DPRO11 5,09 → 4,63 (-9%); FZDA11 106,50 → 115,42 (8%); GZIT11 31,50 → 34,00 (8%); ZAGH11 7,60 → 7,00 (-8%); FPAB11 205,00 → 219,87 (7%)

**Liquidez diária (R$)**: BTSI11 14.287 → 0 (-100%); EDGE11 475 → 78 (-84%); LSOI11 294 → 65 (-78%); ZAGH11 314.263 → 433.342 (38%); KNRE11 919 → 1.255 (36%); ICDI11 46.858 → 59.202 (26%); NEWU11 94.779 → 77.758 (-18%); CPUR11 1,6 mi → 1,8 mi (18%)

**Volatilidade 1 ano (%)**: EIRA11 20,6 → 22,8 (10%); NEWU11 28,7 → 26,1 (-9%); RCRI11 13,1 → 14,1 (7%); NEXG11 31,8 → 29,8 (-6%); GZIT11 27,4 → 28,5 (4%); GLPF11 4,8 → 5,0 (4%); CXTL11 62,7 → 60,6 (-3%); FLRP11 21,4 → 21,9 (3%)

**Maior queda 1 ano (%)**: VVMR11 -11,3 → -13,3 (17%); HOFC11 -16,9 → -19,4 (15%); CXRI11 -20,9 → -18,2 (-13%); BLMG11 -19,1 → -21,2 (11%); DPRO11 -29,7 → -32,2 (8%); RBOP11 -26,6 → -28,5 (7%); AGRX11 -19,4 → -20,7 (7%); ARRI11 -50,1 → -53,3 (6%)

**DY 12 meses (%)**: ICDI11 1,27 → 5,74 (352%); SNME11 8,19 → 2,91 (-64%); VVRI11 3,15 → 1,80 (-43%); HCRI11 17,38 → 10,87 (-37%); RRES11 10,23 → 8,58 (-16%); DAMA11 13,34 → 15,41 (16%); KNCR11 12,89 → 11,19 (-13%); DPRO11 14,01 → 15,41 (10%)

**P/VP**: DAMA11 0,68 → 0,58 (-13%); MGHT11 0,56 → 0,63 (11%); DPRO11 0,54 → 0,49 (-9%); FZDA11 1,13 → 1,22 (8%); GZIT11 0,36 → 0,39 (8%); ZAGH11 0,88 → 0,81 (-8%); FPAB11 0,57 → 0,61 (7%); BLCA11 0,81 → 0,75 (-7%)

