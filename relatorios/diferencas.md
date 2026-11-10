# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-10 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-09 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,58 | 2026-09-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,55 | 2026-11-09 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,0% | 0 | 0 |
| Liquidez diária (R$) | 407 | 11,8% | 305 | 138 |
| Volatilidade 1 ano (%) | 239 | 0,3% | 21 | 0 |
| Maior queda 1 ano (%) | 239 | 0,0% | 63 | 17 |
| Valor de mercado (R$) | 582 | 0,0% | 0 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. A peneira usa a primeira linha (2 meses, pregões sem negócio contam zero).

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 270 | 6,0% | 7,8% | 111 |
| 2 meses so dias com negocio | 270 | 6,0% | 7,7% | 110 |
| 21 pregoes | 270 | 3,5% | 4,2% | 35 |
| 42 pregoes | 270 | -11,5% | 13,7% | 183 |
| 63 pregoes | 270 | -22,6% | 24,1% | 224 |

### O que muda no resultado do método

Ranqueados: 111 antes, 111 depois. Entraram 2, saíram 2, continuaram 109.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| CURY3 | Volatilidade de 47.5% a.a. entre os 20% mais voláteis (corte em 47.3%) | 37º  |
| CAML3 | Volatilidade de 48.4% a.a. entre os 20% mais voláteis (corte em 47.3%) | 88º  |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| EZTC3 | 32º  | Volatilidade de 51.4% a.a. entre os 20% mais voláteis (corte em 48.6%) |
| CYRE3 | 54º  | Volatilidade de 52.3% a.a. entre os 20% mais voláteis (corte em 48.6%) |

**Top 20**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | ALLD3 |
| 3 | LREN3 | LREN3 |
| 4 | MDIA3 | MDIA3 |
| 5 | VLID3 | VLID3 |
| 6 | EUCA4 | EUCA4 |
| 7 | BLAU3 | BLAU3 |
| 8 | GMAT3 | GMAT3 |
| 9 | ABCB4 | ABCB4 |
| 10 | BMGB4 | BMGB4 |
| 11 | ALOS3 | JHSF3 |
| 12 | JHSF3 | ALOS3 |
| 13 | DEXP3 | DEXP3 |
| 14 | GOAU4 | GOAU4 |
| 15 | FESA4 | FESA4 |
| 16 | GGBR4 | GGBR4 |
| 17 | BBDC4 | BBDC4 |
| 18 | SYNE3 | VIVA3 |
| 19 | VIVA3 | SYNE3 |
| 20 | INTB3 | INTB3 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: ZAMP3 3,50 → 3,50 (0%); YDUQ3 9,65 → 9,65 (0%); WLMM4 15,00 → 15,00 (0%); WLMM3 16,80 → 16,80 (0%); WIZC3 6,05 → 6,05 (0%); WHRL4 3,04 → 3,04 (0%); WHRL3 3,16 → 3,16 (0%); WEST3 3,49 → 3,49 (0%)

**Liquidez diária (R$)**: AMBP3 183.880 → 791.865 (331%); MAPT3 125 → 449 (258%); CEDO3 175 → 562 (221%); ESPA3 643.422 → 1,7 mi (167%); CTAX3 13.432 → 29.343 (118%); FASA3 20.151 → 42.115 (109%); AGXY3 7.744 → 15.515 (100%); ZAMP3 247.849 → 0 (-100%)

**Volatilidade 1 ano (%)**: GRND3 37,4 → 43,8 (17%); BBSE3 22,3 → 25,4 (14%); EZTC3 45,3 → 51,4 (13%); DEXP3 32,0 → 36,2 (13%); CYRE4 60,7 → 53,2 (-12%); CYRE3 47,3 → 52,3 (11%); LOGG3 34,9 → 38,1 (9%); POMO3 38,4 → 41,9 (9%)

**Maior queda 1 ano (%)**: TASA3 -60,2 → -23,6 (-61%); DEXP3 -16,9 → -25,9 (54%); TASA4 -58,8 → -32,1 (-45%); GOAU3 -23,2 → -33,0 (42%); EGIE3 -29,7 → -41,1 (39%); RAPT4 -58,3 → -36,4 (-38%); GOAU4 -25,3 → -34,8 (37%); ENJU3 -37,8 → -50,3 (33%)

**Valor de mercado (R$)**: ZAMP3 1,42 bi → 1,42 bi (0%); YDUQ3 2,64 bi → 2,64 bi (0%); WLMM4 576,0 mi → 576,0 mi (0%); WLMM3 576,0 mi → 576,0 mi (0%); WIZC3 967,4 mi → 967,4 mi (0%); WHRL4 4,69 bi → 4,69 bi (0%); WHRL3 4,69 bi → 4,69 bi (0%); WEST3 38,8 mi → 38,8 mi (0%)

## Peneira FIIs

Universo: 575 antes, 575 depois (575 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 575 | 0,0% | 0 | 0 |
| Liquidez diária (R$) | 380 | 17,1% | 316 | 167 |
| Volatilidade 1 ano (%) | 223 | 0,2% | 16 | 7 |
| Maior queda 1 ano (%) | 234 | 0,0% | 19 | 11 |
| DY 12 meses (%) | 381 | 0,0% | 2 | 1 |
| P/VP | 470 | 0,0% | 0 | 0 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. A peneira usa a primeira linha (2 meses, pregões sem negócio contam zero).

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 212 | 7,7% | 14,1% | 145 |
| 2 meses so dias com negocio | 212 | 8,9% | 14,6% | 148 |
| 21 pregoes | 212 | 6,2% | 15,9% | 144 |
| 42 pregoes | 212 | -0,0% | 0,0% | 50 |
| 63 pregoes | 212 | -7,0% | 11,1% | 114 |

### O que muda no resultado do método

Ranqueados: 60 antes, 59 depois. Entraram 1, saíram 2, continuaram 58.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| HSAF11 | Liquidez média diária R$ 0,41 mi abaixo de R$ 0,5 mi | 7º (papel) |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| SPXS11 | 3º (papel) | Liquidez média diária R$ 0,48 mi abaixo de R$ 0,5 mi |
| HBCR11 | 21º (tijolo) | Volatilidade de 27.1% a.a., entre os 20% mais voláteis do grupo tijolo (corte em 23.1%) |

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
| 3 | SPXS11 | RZAK11 |
| 4 | RZAK11 | VRTA11 |
| 5 | VRTA11 | VGIP11 |
| 6 | VGIP11 | RECR11 |
| 7 | RECR11 | HSAF11 (novo) |
| 8 | RBRR11 | RBRR11 |
| 9 | VGIR11 | VGIR11 |
| 10 | PORD11 | RBRY11 |
| 11 | RBRY11 | BTCI11 |
| 12 | BTCI11 | PORD11 |
| 13 | CLIN11 | CLIN11 |
| 14 | XPCI11 | XPCI11 |
| 15 | ICRI11 | ICRI11 |
| 16 | HGCR11 | HGCR11 |
| 17 | KNIP11 | KNIP11 |
| 18 | KNHY11 | KNHY11 |
| 19 | KNSC11 | KNSC11 |
| 20 | KNUQ11 | KNUQ11 |

**Top 20 tijolo**: 20 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | LIFE11 | LIFE11 |
| 2 | JSRE11 | JSRE11 |
| 3 | GTWR11 | GTWR11 |
| 4 | RBVA11 | RBVA11 |
| 5 | TVRI11 | TVRI11 |
| 6 | RBRP11 | RBRP11 |
| 7 | HGRE11 | HGRE11 |
| 8 | RCRB11 | RCRB11 |
| 9 | VILG11 | VILG11 |
| 10 | FATN11 | FATN11 |
| 11 | LVBI11 | LVBI11 |
| 12 | KNHF11 | KNHF11 |
| 13 | HGBS11 | HGBS11 |
| 14 | CPSH11 | CPSH11 |
| 15 | HGRU11 | HGRU11 |
| 16 | BRCO11 | BRCO11 |
| 17 | XPLG11 | XPLG11 |
| 18 | XPML11 | XPML11 |
| 19 | HGLG11 | HGLG11 |
| 20 | PMLL11 | PMLL11 |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: JPPA11 77,39 → 77,65 (0%); ZIFI11 749,99 → 749,99 (0%); ZAVI11 9,32 → 9,32 (0%); ZAVC11 8,88 → 8,88 (0%); ZAGH11 7,89 → 7,89 (0%); YUFI11 15,00 → 15,00 (0%); YCHY11 1.000,00 → 1.000,00 (0%); XTED11 8,82 → 8,82 (0%)

**Liquidez diária (R$)**: RVBI11 931.734 → 0 (-100%); RRES11 24 → 0 (-100%); RRCI11 218.182 → 0 (-100%); ROOF11 47 → 0 (-100%); RMAI11 30.797 → 0 (-100%); RDLI11 1.091 → 0 (-100%); RBCO11 144.616 → 0 (-100%); QAGR11 149.034 → 0 (-100%)

**Volatilidade 1 ano (%)**: JASC11 30,8 → 64,6 (110%); VXXV11 3,9 → 7,1 (81%); CJCT11 20,3 → 31,3 (54%); HBCR11 18,3 → 27,1 (48%); VVRI11 77,2 → 102,9 (33%); EIRA11 16,0 → 20,2 (27%); FTCA11 29,9 → 23,4 (-22%); WTSP11 81,7 → 97,3 (19%)

**Maior queda 1 ano (%)**: BTRU11 -4,4 → -12,1 (173%); OXRL11 -19,3 → -0,1 (-100%); XPML11 -99,0 → -15,9 (-84%); MIDW11 -10,3 → -3,4 (-67%); VGII11 -39,7 → -17,0 (-57%); FIXX11 -7,9 → -11,9 (50%); APXM11 -40,5 → -56,1 (39%); INHF11 -76,3 → -48,1 (-37%)

**DY 12 meses (%)**: HIRE11 6,49 → 9,10 (40%); EIRA11 12,06 → 13,94 (16%); EQIR11 15,17 → 14,99 (-1%); JPPA11 18,56 → 18,49 (-0%); IVBP11 1,27 → 1,27 (0%); VVMR11 0,50 → 0,50 (0%); ADSH11 2,21 → 2,21 (0%); GSFI11 1,95 → 1,95 (-0%)

**P/VP**: JPPA11 0,78 → 0,78 (0%); RFOF11 181,87 → 181,87 (-0%); AROA11 1,23 → 1,23 (0%); SRVD11 18,35 → 18,35 (0%); KNRE11 0,32 → 0,32 (0%); IDFI11 1,25 → 1,25 (0%); PATL11 201,64 → 201,64 (-0%); HYPI11 38,69 → 38,69 (0%)

