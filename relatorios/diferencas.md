# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-17 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-13 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,60 | 2026-11-13 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,3% | 45 | 3 |
| Liquidez diária (R$) | 381 | 1,7% | 77 | 14 |
| Volatilidade 1 ano (%) | 391 | 0,1% | 3 | 0 |
| Maior queda 1 ano (%) | 397 | 0,0% | 4 | 0 |
| Valor de mercado (R$) | 582 | 0,2% | 45 | 3 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 267 | 6,7% | 8,5% | 117 |
| 2 meses so dias com negocio | 267 | 6,7% | 8,5% | 116 |
| 21 pregoes | 267 | -1,0% | 1,7% | 10 |
| 42 pregoes | 267 | -4,1% | 9,1% | 125 |
| 63 pregoes | 267 | -15,6% | 18,1% | 205 |

### O que muda no resultado do método

Ranqueados: 110 antes, 109 depois. Entraram 0, saíram 1, continuaram 109.

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| CURY3 | 39º  | Volatilidade de 48.8% a.a. entre os 20% mais voláteis (corte em 48.7%) |

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | LREN3 | LREN3 |
| 3 | ALLD3 | ALLD3 |
| 4 | VLID3 | VLID3 |
| 5 | MDIA3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | GMAT3 | BLAU3 |
| 8 | BMGB4 | DEXP3 |
| 9 | BLAU3 | GMAT3 |
| 10 | ALOS3 | BMGB4 |
| 11 | JHSF3 | ALOS3 |
| 12 | ABCB4 | JHSF3 |
| 13 | DEXP3 | VIVA3 |
| 14 | VIVA3 | ABCB4 |
| 15 | GOAU4 | GOAU4 |
| 16 | FESA4 | GGBR4 |
| 17 | SYNE3 | BBDC4 |
| 18 | GGBR4 | FESA4 |
| 19 | BBDC4 | SYNE3 |
| 20 | CSUD3 | BRBI11 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: INEP3 0,99 → 1,34 (35%); AALR3 1,31 → 0,95 (-27%); INEP4 0,97 → 1,22 (26%); JFEN3 2,95 → 2,43 (-18%); SEQL3 9,98 → 8,26 (-17%); CTAX3 0,84 → 0,96 (14%); HBOR3 1,16 → 1,02 (-12%); LJQQ3 1,10 → 0,97 (-12%)

**Liquidez diária (R$)**: MWET4 118 → 525 (345%); BAUH4 453 → 1.359 (200%); SOND6 2.430 → 4.334 (78%); RSID3 2.594 → 4.507 (74%); CTKA3 649 → 326 (-50%); BRSR3 304.911 → 173.517 (-43%); AVLL3 2.660 → 1.607 (-40%); SOND5 5.124 → 7.029 (37%)

**Volatilidade 1 ano (%)**: INEP4 54,7 → 59,3 (8%); MNPR3 43,8 → 41,5 (-5%); CGAS5 19,5 → 18,5 (-5%); DEXP4 37,4 → 39,0 (4%); GRND3 43,8 → 42,2 (-4%); CLSC4 23,8 → 24,6 (4%); DEXP3 36,4 → 37,7 (4%); LOGG3 38,4 → 39,6 (3%)

**Maior queda 1 ano (%)**: MDIA3 -47,5 → -42,4 (-11%); AALR3 -75,7 → -82,4 (9%); BRAP4 -30,2 → -32,8 (9%); BRAP3 -25,5 → -27,5 (8%); CASH3 -35,0 → -36,5 (4%); LOGN3 -43,1 → -45,0 (4%); UNIP5 -32,7 → -34,0 (4%); HBRE3 -69,2 → -71,9 (4%)

**Valor de mercado (R$)**: INEP3 54,6 mi → 73,9 mi (35%); AALR3 199,6 mi → 144,7 mi (-27%); INEP4 50,5 mi → 63,5 mi (26%); JFEN3 7,6 mi → 6,2 mi (-18%); SEQL3 423,8 mi → 350,8 mi (-17%); CTAX3 6,7 mi → 7,7 mi (14%); HBOR3 155,3 mi → 136,5 mi (-12%); LJQQ3 214,6 mi → 189,2 mi (-12%)

## Peneira FIIs

Universo: 576 antes, 576 depois (576 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 576 | 0,0% | 19 | 0 |
| Liquidez diária (R$) | 358 | 0,8% | 41 | 11 |
| Volatilidade 1 ano (%) | 321 | 0,1% | 7 | 0 |
| Maior queda 1 ano (%) | 346 | 0,0% | 19 | 4 |
| DY 12 meses (%) | 382 | 0,6% | 31 | 3 |
| P/VP | 464 | 0,9% | 50 | 13 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 203 | 9,5% | 10,9% | 114 |
| 2 meses so dias com negocio | 203 | 10,3% | 11,6% | 120 |
| 21 pregoes | 203 | 7,2% | 14,5% | 128 |
| 42 pregoes | 203 | 0,4% | 1,0% | 8 |
| 63 pregoes | 203 | -4,2% | 8,3% | 90 |

### O que muda no resultado do método

Ranqueados: 58 antes, 56 depois. Entraram 1, saíram 3, continuaram 55.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| BRCR11 | Vacância física de 40,2% (2026-06-30), acima de 25% | 2º (tijolo) |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| JSRE11 | 4º (tijolo) | Volatilidade de 23.2% a.a., entre os 20% mais voláteis do grupo tijolo (corte em 22.7%) |
| RBVA11 | 5º (tijolo) | Inadimplência de 13.321,5% da receita (2026-09-30), acima de 10% |
| XPML11 | 11º (tijolo) | Vacância física de 91,8% (2026-09-30), acima de 25% |

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
| 8 | GARE11 | RINV11 |
| 9 | RINV11 | GARE11 |
| 10 | RZLC11 | SNEL11 |
| 11 | SNEL11 | RZLC11 |
| 12 | SEED11 | SEED11 |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | VGIP11 | VGIP11 |
| 4 | RECR11 | RZAK11 |
| 5 | RZAK11 | RECR11 |
| 6 | VRTA11 | VGIR11 |
| 7 | VGIR11 | VRTA11 |
| 8 | RBRR11 | RBRY11 |
| 9 | RBRY11 | RBRR11 |
| 10 | BTCI11 | BTCI11 |
| 11 | PORD11 | PORD11 |
| 12 | CLIN11 | CLIN11 |
| 13 | ICRI11 | ICRI11 |
| 14 | XPCI11 | XPCI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNIP11 | KNIP11 |
| 17 | KNHY11 | KNHY11 |
| 18 | MCCI11 | MCCI11 |
| 19 | KNSC11 | KNUQ11 (novo) |
| 20 | MXRF11 | MXRF11 |

**Top 20 tijolo**: 17 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | GTWR11 | BRCR11 (novo) |
| 3 | TVRI11 | GTWR11 |
| 4 | JSRE11 | TVRI11 |
| 5 | RBVA11 | RCRB11 |
| 6 | RBRP11 | HGRE11 |
| 7 | HGRE11 | RBRP11 |
| 8 | RCRB11 | VILG11 |
| 9 | VILG11 | FATN11 |
| 10 | FATN11 | CPSH11 |
| 11 | XPML11 | LVBI11 |
| 12 | HGBS11 | HGRU11 |
| 13 | KNHF11 | KNHF11 |
| 14 | CPSH11 | BRCO11 |
| 15 | HGRU11 | HGBS11 |
| 16 | LVBI11 | XPLG11 |
| 17 | BRCO11 | PMLL11 |
| 18 | HGLG11 | HGLG11 |
| 19 | XPLG11 | KNRI11 (novo) |
| 20 | PMLL11 | ALZR11 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: KNRE11 0,18 → 0,20 (11%); HUCG11 78,07 → 86,59 (11%); ZAVI11 9,49 → 8,61 (-9%); IBCR11 31,74 → 34,47 (9%); MGHT11 12,24 → 11,26 (-8%); PLRI11 5,00 → 5,40 (8%); DPRO11 4,63 → 4,99 (8%); OCRE11 65,00 → 70,00 (8%)

**Liquidez diária (R$)**: BGRB11 4.347 → 12.204 (181%); HGBL11 220.537 → 462.223 (110%); SPMO11 2.800 → 0 (-100%); SNFF11 172.123 → 0 (-100%); KISU11 465.133 → 0 (-100%); HJCT11 75 → 0 (-100%); BTWR11 2 → 4 (100%); INHF11 459.468 → 233.351 (-49%)

**Volatilidade 1 ano (%)**: MCCI11 12,3 → 13,7 (11%); SNEL11 11,2 → 12,3 (10%); CXRI11 38,3 → 34,6 (-10%); ZAVI11 24,7 → 26,5 (8%); LIFE11 21,4 → 22,7 (6%); RCRI11 14,1 → 14,9 (6%); VGIR11 12,9 → 13,6 (5%); HSAF11 14,9 → 15,7 (5%)

**Maior queda 1 ano (%)**: MCCI11 -8,8 → -11,4 (30%); ZAVI11 -17,1 → -21,6 (26%); VGIR11 -14,6 → -18,2 (25%); HSAF11 -14,8 → -18,2 (24%); LIFE11 -28,6 → -33,9 (19%); LAFI11 -10,4 → -8,5 (-18%); SNEL11 -18,0 → -20,7 (15%); BLMG11 -21,2 → -24,3 (15%)

**DY 12 meses (%)**: LSOP11 4,69 → 2,35 (-50%); IBBP11 11,26 → 6,73 (-40%); RBIR11 18,76 → 13,88 (-26%); TRXB11 16,78 → 14,10 (-16%); RZZI11 5,51 → 6,26 (14%); ZAVI11 14,46 → 15,94 (10%); KNRE11 0,69 → 0,62 (-10%); HUCG11 10,35 → 9,33 (-10%)

**P/VP**: LSOP11 0,97 → 194,63 (19.889%); HIRE11 1,01 → 201,13 (19.725%); SNLG11 0,60 → 116,15 (19.195%); TRXF11 0,58 → 73,42 (12.622%); RDLI11 0,93 → 38,86 (4.095%); INRD11 0,61 → 10,55 (1.631%); KNRE11 0,30 → 0,59 (95%); CFII11 1,74 → 2,91 (67%)

