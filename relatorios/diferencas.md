# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-11 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-09 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,58 | 2026-09-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,55 | 2026-11-09 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,3% | 39 | 2 |
| Liquidez diária (R$) | 384 | 3,3% | 107 | 21 |
| Volatilidade 1 ano (%) | 389 | 0,1% | 1 | 0 |
| Maior queda 1 ano (%) | 395 | 0,0% | 6 | 2 |
| Valor de mercado (R$) | 582 | 0,2% | 39 | 2 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 271 | 0,4% | 4,3% | 51 |
| 2 meses so dias com negocio | 271 | 0,5% | 4,4% | 51 |
| 21 pregoes | 271 | -2,8% | 3,3% | 15 |
| 42 pregoes | 271 | -15,1% | 15,8% | 209 |
| 63 pregoes | 271 | -25,2% | 26,2% | 239 |

### O que muda no resultado do método

Ranqueados: 110 antes, 110 depois. Entraram 0, saíram 0, continuaram 110.

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | ALLD3 |
| 3 | LREN3 | LREN3 |
| 4 | MDIA3 | VLID3 |
| 5 | VLID3 | MDIA3 |
| 6 | EUCA4 | EUCA4 |
| 7 | BLAU3 | BLAU3 |
| 8 | GMAT3 | GMAT3 |
| 9 | ABCB4 | ABCB4 |
| 10 | BMGB4 | BMGB4 |
| 11 | JHSF3 | ALOS3 |
| 12 | ALOS3 | JHSF3 |
| 13 | DEXP3 | DEXP3 |
| 14 | GOAU4 | GOAU4 |
| 15 | FESA4 | VIVA3 |
| 16 | GGBR4 | BBDC4 |
| 17 | BBDC4 | CSUD3 (novo) |
| 18 | VIVA3 | GGBR4 |
| 19 | SYNE3 | SYNE3 |
| 20 | INTB3 | FESA4 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: TXRX3 9,00 → 5,46 (-39%); SEQL3 9,50 → 12,30 (29%); MRSA6B 36,00 → 42,00 (17%); USIM6 6,60 → 5,51 (-17%); MRSA5B 38,00 → 43,46 (14%); TECN3 7,95 → 9,00 (13%); SBFG3 5,48 → 4,84 (-12%); MGLU3 5,84 → 6,52 (12%)

**Liquidez diária (R$)**: MRSA3B 1.200 → 4.126 (244%); MRSA5B 349 → 1.158 (232%); MRSA6B 328 → 1.061 (224%); BGIP3 1.396 → 3.236 (132%); SNSY3 47 → 0 (-100%); GPAR3 285 → 95 (-67%); CASN3 639 → 1.011 (58%); CEDO3 67 → 33 (-50%)

**Volatilidade 1 ano (%)**: BMKS3 33,9 → 30,6 (-10%); TECN3 42,1 → 43,8 (4%); AGRO3 26,3 → 27,3 (4%); SMTO3 46,0 → 47,6 (3%); SBFG3 52,4 → 53,8 (3%); CRPG5 64,2 → 62,5 (-3%); EMBJ3 39,9 → 40,7 (2%); FESA4 41,9 → 42,8 (2%)

**Maior queda 1 ano (%)**: USIM6 -35,3 → -44,8 (27%); AHEB3 -21,8 → -17,4 (-20%); BRAV3 -31,3 → -35,7 (14%); CEEB5 -17,9 → -15,6 (-13%); UNIP5 -29,8 → -31,4 (5%); MNPR3 -37,5 → -39,4 (5%); AALR3 -64,0 → -66,7 (4%); MELK3 -45,3 → -46,5 (3%)

**Valor de mercado (R$)**: TXRX3 18,3 mi → 11,1 mi (-39%); SEQL3 403,5 mi → 522,4 mi (29%); MRSA6B 14,54 bi → 16,96 bi (17%); USIM6 6,18 bi → 5,16 bi (-17%); MRSA5B 14,54 bi → 16,63 bi (14%); TECN3 478,4 mi → 541,6 mi (13%); SBFG3 1,26 bi → 1,12 bi (-12%); MGLU3 4,53 bi → 5,06 bi (12%)

## Peneira FIIs

Universo: 575 antes, 575 depois (575 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 575 | 0,0% | 18 | 1 |
| Liquidez diária (R$) | 359 | 0,6% | 27 | 4 |
| Volatilidade 1 ano (%) | 324 | 0,1% | 6 | 0 |
| Maior queda 1 ano (%) | 352 | 0,0% | 14 | 2 |
| DY 12 meses (%) | 381 | 0,2% | 23 | 4 |
| P/VP | 470 | 0,1% | 18 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 198 | 12,3% | 13,9% | 134 |
| 2 meses so dias com negocio | 198 | 13,5% | 14,3% | 139 |
| 21 pregoes | 198 | 9,9% | 14,2% | 132 |
| 42 pregoes | 198 | -0,0% | 0,7% | 5 |
| 63 pregoes | 198 | -4,3% | 8,5% | 84 |

### O que muda no resultado do método

Ranqueados: 59 antes, 58 depois. Entraram 0, saíram 1, continuaram 58.

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| SPXS11 | 3º (papel) | Liquidez média diária R$ 0,49 mi abaixo de R$ 0,5 mi |

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
| 8 | KISU11 | KISU11 |
| 9 | GARE11 | GARE11 |
| 10 | RZLC11 | RZLC11 |
| 11 | RINV11 | RINV11 |
| 12 | SNEL11 | SNEL11 |

**Top 20 papel**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | VCJR11 | VCJR11 |
| 3 | SPXS11 | VRTA11 |
| 4 | RZAK11 | RZAK11 |
| 5 | VRTA11 | VGIP11 |
| 6 | VGIP11 | RECR11 |
| 7 | RECR11 | VGIR11 |
| 8 | RBRR11 | RBRR11 |
| 9 | VGIR11 | RBRY11 |
| 10 | PORD11 | BTCI11 |
| 11 | RBRY11 | CLIN11 |
| 12 | BTCI11 | PORD11 |
| 13 | CLIN11 | XPCI11 |
| 14 | XPCI11 | ICRI11 |
| 15 | ICRI11 | HGCR11 |
| 16 | HGCR11 | KNHY11 |
| 17 | KNIP11 | KNIP11 |
| 18 | KNHY11 | KNSC11 |
| 19 | KNSC11 | KNUQ11 |
| 20 | KNUQ11 | MCCI11 (novo) |

**Top 20 tijolo**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | JSRE11 | GTWR11 |
| 3 | GTWR11 | JSRE11 |
| 4 | RBVA11 | RBVA11 |
| 5 | TVRI11 | TVRI11 |
| 6 | RBRP11 | RBRP11 |
| 7 | HGRE11 | RCRB11 |
| 8 | RCRB11 | HGRE11 |
| 9 | VILG11 | VILG11 |
| 10 | FATN11 | FATN11 |
| 11 | LVBI11 | HGBS11 |
| 12 | KNHF11 | XPML11 |
| 13 | HGBS11 | CPSH11 |
| 14 | CPSH11 | KNHF11 |
| 15 | HGRU11 | LVBI11 |
| 16 | BRCO11 | HGRU11 |
| 17 | XPLG11 | BRCO11 |
| 18 | XPML11 | XPLG11 |
| 19 | HGLG11 | PMLL11 |
| 20 | PMLL11 | HGLG11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: CTXT11 3,92 → 3,00 (-23%); EMET11 10,50 → 8,84 (-16%); HCTR11 11,01 → 9,71 (-12%); NVHO11 12,22 → 13,64 (12%); APTO11 5,54 → 5,00 (-10%); HOFC11 35,00 → 32,16 (-8%); RZTR11 66,04 → 70,70 (7%); CACR11 10,96 → 10,20 (-7%)

**Liquidez diária (R$)**: ERPA11 18.094 → 34.033 (88%); EMET11 138.683 → 216.858 (56%); SPMO11 5.637 → 2.800 (-50%); WTSP11 158.979 → 225.726 (42%); FPNG11 124 → 148 (20%); AROA11 7.004 → 5.720 (-18%); FIXX11 146.273 → 121.003 (-17%); VGII11 297.509 → 249.860 (-16%)

**Volatilidade 1 ano (%)**: RCRI11 11,1 → 12,3 (10%); APTO11 22,8 → 24,9 (9%); HCTR11 28,2 → 30,8 (9%); NEWU11 30,9 → 28,7 (-7%); RZTR11 18,8 → 20,0 (6%); XPML11 13,2 → 14,0 (6%); SNFZ11 14,0 → 13,3 (-5%); FYTO11 14,1 → 14,5 (3%)

**Maior queda 1 ano (%)**: CTXT11 -40,6 → -54,5 (34%); GFDL11 -0,1 → -0,1 (-30%); NEXG11 -11,1 → -9,2 (-17%); APTO11 -37,4 → -43,5 (16%); ARXD11 -15,3 → -17,8 (16%); XPML11 -15,9 → -18,4 (15%); DVFF11 -17,7 → -19,7 (11%); HCTR11 -52,5 → -58,1 (11%)

**DY 12 meses (%)**: GCOI11 80,13 → 133,38 (66%); VVDI11 2,90 → 4,04 (39%); TCIN11 5,61 → 7,54 (34%); HILG11 69,57 → 91,63 (32%); EMET11 12,48 → 14,37 (15%); APTO11 17,50 → 19,39 (11%); RMBS11 11,95 → 13,23 (11%); NVHO11 8,69 → 7,79 (-10%)

**P/VP**: CTXT11 0,27 → 0,20 (-23%); EMET11 1,15 → 0,96 (-16%); HCTR11 0,11 → 0,09 (-12%); NVHO11 0,74 → 0,82 (12%); APTO11 0,71 → 0,64 (-10%); HOFC11 0,57 → 0,52 (-8%); RZTR11 0,66 → 0,70 (7%); CACR11 0,12 → 0,11 (-7%)

