# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-12 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-10 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,58 | 2026-09-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,53 | 2026-11-10 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,3% | 51 | 3 |
| Liquidez diária (R$) | 384 | 3,9% | 145 | 19 |
| Volatilidade 1 ano (%) | 390 | 0,1% | 1 | 0 |
| Maior queda 1 ano (%) | 397 | 0,0% | 3 | 0 |
| Valor de mercado (R$) | 582 | 0,3% | 51 | 3 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 269 | 2,3% | 5,0% | 61 |
| 2 meses so dias com negocio | 269 | 2,5% | 5,1% | 62 |
| 21 pregoes | 269 | -3,8% | 4,0% | 24 |
| 42 pregoes | 269 | -12,2% | 13,3% | 179 |
| 63 pregoes | 269 | -22,8% | 23,7% | 229 |

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
| 7 | BLAU3 | GMAT3 |
| 8 | GMAT3 | ABCB4 |
| 9 | ABCB4 | BMGB4 |
| 10 | BMGB4 | BLAU3 |
| 11 | ALOS3 | JHSF3 |
| 12 | JHSF3 | ALOS3 |
| 13 | DEXP3 | DEXP3 |
| 14 | GOAU4 | GOAU4 |
| 15 | VIVA3 | GGBR4 |
| 16 | BBDC4 | SYNE3 |
| 17 | CSUD3 | BBDC4 |
| 18 | GGBR4 | VIVA3 |
| 19 | SYNE3 | CSUD3 |
| 20 | FESA4 | FESA4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: SEQL3 12,30 → 9,42 (-23%); ARML3 3,18 → 3,91 (23%); CSED3 4,94 → 3,81 (-23%); MGLU3 6,52 → 7,66 (17%); AMER3 4,40 → 5,07 (15%); CSAN3 2,68 → 3,03 (13%); LUPA3 3,84 → 4,30 (12%); BIOM3 5,22 → 5,84 (12%)

**Liquidez diária (R$)**: RPAD3 71 → 0 (-100%); JOPA3 95 → 0 (-100%); GPAR3 95 → 0 (-100%); AHEB3 219 → 0 (-100%); ESPA3 1,5 mi → 604.449 (-60%); WLMM3 1.498 → 620 (-59%); TXRX4 1.827 → 805 (-56%); CTKA3 1.411 → 649 (-54%)

**Volatilidade 1 ano (%)**: CGAS5 21,7 → 19,7 (-9%); ARML3 66,9 → 70,0 (5%); MGLU3 71,4 → 73,2 (2%); CSAN3 54,9 → 56,2 (2%); AMER3 66,2 → 67,6 (2%); PASS3 34,0 → 34,6 (2%); RAIL3 41,0 → 41,7 (2%); MRVE3 54,3 → 55,1 (2%)

**Maior queda 1 ano (%)**: CGAS3 -12,4 → -13,9 (12%); VULC3 -51,0 → -45,7 (-11%); PETR4 -24,7 → -27,0 (10%); AALR3 -66,7 → -69,2 (4%); PETR3 -24,4 → -25,1 (3%); WDCN3 -34,9 → -34,1 (-2%); TCSA3 -68,5 → -70,1 (2%); AMAR3 -61,0 → -59,6 (-2%)

**Valor de mercado (R$)**: SEQL3 522,4 mi → 400,1 mi (-23%); ARML3 1,10 bi → 1,35 bi (23%); CSED3 1,80 bi → 1,39 bi (-23%); MGLU3 5,06 bi → 5,94 bi (17%); AMER3 881,1 mi → 1,02 bi (15%); CSAN3 10,63 bi → 12,02 bi (13%); LUPA3 18,2 mi → 20,3 mi (12%); BIOM3 714,4 mi → 799,2 mi (12%)

## Peneira FIIs

Universo: 575 antes, 575 depois (575 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 575 | 0,0% | 15 | 0 |
| Liquidez diária (R$) | 359 | 0,7% | 40 | 8 |
| Volatilidade 1 ano (%) | 324 | 0,1% | 2 | 0 |
| Maior queda 1 ano (%) | 350 | 0,0% | 5 | 2 |
| DY 12 meses (%) | 381 | 0,2% | 10 | 0 |
| P/VP | 469 | 0,1% | 13 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 199 | 11,2% | 12,3% | 131 |
| 2 meses so dias com negocio | 199 | 12,1% | 13,0% | 135 |
| 21 pregoes | 199 | 7,8% | 14,0% | 123 |
| 42 pregoes | 199 | 0,0% | 0,8% | 13 |
| 63 pregoes | 199 | -3,9% | 8,1% | 83 |

### O que muda no resultado do método

Ranqueados: 58 antes, 57 depois. Entraram 0, saíram 1, continuaram 57.

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| KISU11 | 8º (fof) | Liquidez média diária R$ 0,5 mi abaixo de R$ 0,5 mi |

**Top 12 fof**: 11 de 12 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | PSEC11 |
| 2 | JSAF11 | JSAF11 |
| 3 | RBRX11 | RBRX11 |
| 4 | CPTS11 | CPTS11 |
| 5 | BTHF11 | BTHF11 |
| 6 | HFOF11 | HFOF11 |
| 7 | KFOF11 | KFOF11 |
| 8 | KISU11 | GARE11 |
| 9 | GARE11 | RINV11 |
| 10 | RZLC11 | RZLC11 |
| 11 | RINV11 | SNEL11 |
| 12 | SNEL11 |  |

**Top 20 papel**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | VRTA11 | RZAK11 |
| 4 | RZAK11 | RECR11 |
| 5 | VGIP11 | VGIP11 |
| 6 | RECR11 | VRTA11 |
| 7 | VGIR11 | RBRR11 |
| 8 | RBRR11 | VGIR11 |
| 9 | RBRY11 | RBRY11 |
| 10 | BTCI11 | CLIN11 |
| 11 | CLIN11 | BTCI11 |
| 12 | PORD11 | PORD11 |
| 13 | XPCI11 | XPCI11 |
| 14 | ICRI11 | ICRI11 |
| 15 | HGCR11 | HGCR11 |
| 16 | KNHY11 | KNHY11 |
| 17 | KNIP11 | KNIP11 |
| 18 | KNSC11 | KNSC11 |
| 19 | KNUQ11 | KNUQ11 |
| 20 | MCCI11 | MCCI11 |

**Top 20 tijolo**: 19 de 20 continuam.

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
| 9 | VILG11 | VILG11 |
| 10 | FATN11 | FATN11 |
| 11 | HGBS11 | XPML11 |
| 12 | XPML11 | HGBS11 |
| 13 | CPSH11 | CPSH11 |
| 14 | KNHF11 | LVBI11 |
| 15 | LVBI11 | KNHF11 |
| 16 | HGRU11 | HGRU11 |
| 17 | BRCO11 | BRCO11 |
| 18 | XPLG11 | XPLG11 |
| 19 | PMLL11 | HGLG11 |
| 20 | HGLG11 | KNRI11 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: CTXT11 3,00 → 3,45 (15%); DAMA11 4,17 → 4,75 (14%); RZEO11 110,00 → 95,92 (-13%); FIIP11 136,13 → 152,96 (12%); EURO11 295,00 → 327,41 (11%); RBDS11 1,67 → 1,80 (8%); HUSC11 97,50 → 90,01 (-8%); BGRB11 129,71 → 120,00 (-7%)

**Liquidez diária (R$)**: HDEL11 1 → 4 (294%); VJFD11 32 → 0 (-100%); NAUI11 1.124 → 0 (-100%); VGRH11 7.505 → 4.679 (-38%); PQDP11 420.515 → 559.514 (33%); GFDL11 25.598 → 18.581 (-27%); RECD11 4.688 → 3.468 (-26%); AZPL11 378.251 → 461.848 (22%)

**Volatilidade 1 ano (%)**: FIIP11 25,7 → 28,2 (10%); RCRI11 12,3 → 13,1 (7%); RURA11 12,9 → 13,5 (5%); CXTL11 65,5 → 62,7 (-4%); EURO11 35,7 → 37,2 (4%); VRTA11 16,6 → 17,1 (3%); VGIR11 12,3 → 12,6 (3%); CTXT11 60,5 → 62,2 (3%)

**Maior queda 1 ano (%)**: ICDI11 -0,4 → -5,8 (1.362%); RZEO11 -23,1 → -33,0 (43%); RURA11 -18,5 → -21,7 (17%); LSAG11 -23,4 → -25,2 (8%); SNEL11 -16,9 → -17,8 (5%); IAGR11 -20,6 → -21,5 (4%); TEPP11 -28,6 → -29,6 (4%); APTO11 -43,5 → -44,8 (3%)

**DY 12 meses (%)**: DAMA11 15,22 → 13,37 (-12%); FIIP11 12,44 → 11,07 (-11%); EURO11 8,67 → 7,82 (-10%); HUSC11 12,62 → 13,67 (8%); BGRB11 4,48 → 4,84 (8%); ARTE11 19,97 → 21,38 (7%); IBCR11 17,18 → 18,37 (7%); MCLO11 9,64 → 10,25 (6%)

**P/VP**: CTXT11 0,20 → 0,23 (15%); DAMA11 0,59 → 0,67 (14%); FIIP11 0,68 → 0,76 (12%); EURO11 0,74 → 0,83 (11%); RBDS11 0,07 → 0,07 (8%); HUSC11 0,49 → 0,45 (-8%); IBCR11 0,45 → 0,42 (-6%); MCLO11 0,76 → 0,71 (-6%)

