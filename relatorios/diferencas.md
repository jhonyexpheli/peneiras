# Quadro de diferenças: fontes oficiais × base atual

Gerado pelo robô do GitHub Actions a cada execução do coletor. Não é recomendação de investimento.

## Indicadores de referência

| Indicador | Valor | Data | Fonte |
|---|---|---|---|
| Selic meta (% a.a.) | 13,75 | 2026-11-28 | Banco Central, SGS série 432 |
| CDI (% a.a.) | 13,65 | 2026-11-26 | Banco Central, SGS série 4389 |
| IPCA 12 meses (%) | 4,63 | 2026-10-01 | Banco Central, SGS série 13522 |
| NTN-B, juro real (% a.a.) | 7,52 | 2026-11-26 | Tesouro Transparente, preços e taxas do Tesouro Direto |

## Peneira de Valor (ações)

Universo: 617 antes, 617 depois (617 em comum).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 579 | 0,4% | 63 | 1 |
| Liquidez diária (R$) | 379 | 3,6% | 146 | 17 |
| Volatilidade 1 ano (%) | 394 | 0,1% | 0 | 0 |
| Maior queda 1 ano (%) | 400 | 0,0% | 2 | 0 |
| Valor de mercado (R$) | 582 | 0,4% | 63 | 1 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 21 pregões nas ações.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 259 | 19,4% | 19,9% | 211 |
| 2 meses so dias com negocio | 259 | 19,4% | 19,9% | 211 |
| 21 pregoes | 259 | -3,5% | 4,0% | 26 |
| 42 pregoes | 259 | 16,8% | 18,6% | 192 |
| 63 pregoes | 259 | 5,1% | 13,7% | 161 |

### O que muda no resultado do método

Ranqueados: 110 antes, 109 depois. Entraram 0, saíram 1, continuaram 109.

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| TASA4 | 78º  | Volatilidade de 49.2% a.a. entre os 20% mais voláteis (corte em 48.3%) |

**Top 20**: 19 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRSR6 | BRSR6 |
| 2 | ALLD3 | ALLD3 |
| 3 | LREN3 | LREN3 |
| 4 | MDIA3 | MDIA3 |
| 5 | VLID3 | VLID3 |
| 6 | EUCA4 | EUCA4 |
| 7 | DEXP3 | BMGB4 |
| 8 | BMGB4 | DEXP3 |
| 9 | GMAT3 | BLAU3 |
| 10 | ABCB4 | ABCB4 |
| 11 | BLAU3 | GMAT3 |
| 12 | JHSF3 | JHSF3 |
| 13 | ALOS3 | ALOS3 |
| 14 | VIVA3 | GOAU4 |
| 15 | FESA4 | FESA4 |
| 16 | GOAU4 | GGBR4 |
| 17 | SYNE3 | VIVA3 |
| 18 | GGBR4 | SYNE3 |
| 19 | VALE3 | VALE3 |
| 20 | INTB3 | PFRM3 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: ESTR4 1,22 → 1,50 (23%); LJQQ3 1,27 → 1,48 (17%); SIMH3 6,85 → 7,97 (16%); PTBL3 1,44 → 1,66 (15%); WEST3 3,25 → 3,69 (14%); TEND3 16,51 → 18,66 (13%); HETA4 4,81 → 5,40 (12%); MOVI3 6,76 → 7,57 (12%)

**Liquidez diária (R$)**: HETA4 46 → 147 (221%); IGTI4 2.009 → 4.649 (131%); CGAS3 6.790 → 13.780 (103%); SHUL3 143 → 0 (-100%); EQPA6 31 → 0 (-100%); ISAE4 108,7 mi → 214,7 mi (98%); FIEI3 52 → 26 (-50%); TELB3 39.477 → 20.541 (-48%)

**Volatilidade 1 ano (%)**: EALT4 29,3 → 30,8 (5%); ALPA3 53,8 → 51,2 (-5%); CRPG5 59,3 → 57,4 (-3%); PTBL3 60,6 → 62,3 (3%); BRSR3 30,3 → 31,1 (3%); LOGN3 35,4 → 36,3 (3%); SIMH3 67,5 → 69,1 (2%); CAMB3 32,9 → 32,1 (-2%)

**Maior queda 1 ano (%)**: MSPA4 -19,5 → -21,9 (12%); FASA3 -44,7 → -49,4 (10%); CGAS3 -16,1 → -16,6 (3%); ENMT3 -55,6 → -54,1 (-3%); VSTE3 -54,3 → -53,1 (-2%); EPAR3 -74,6 → -75,8 (2%); BEEF3 -62,0 → -61,0 (-2%); CTAX3 -64,1 → -63,2 (-1%)

**Valor de mercado (R$)**: ESTR4 10,8 mi → 13,3 mi (23%); LJQQ3 247,7 mi → 288,7 mi (17%); SIMH3 4,00 bi → 4,65 bi (16%); PTBL3 203,0 mi → 234,0 mi (15%); WEST3 36,1 mi → 41,0 mi (14%); TEND3 2,02 bi → 2,29 bi (13%); HETA4 18,1 mi → 20,3 mi (12%); MOVI3 2,87 bi → 3,22 bi (12%)

## Peneira FIIs

Universo: 576 antes, 650 depois (377 em comum; só na base nova: AAGR11, ABTC11, ACWI11, AGGX11, AGRI11, ALUG11, APXR11, APXU11, ARGE11, AUMT11, AURO11, AUVP11, AZIN11, BBOI11, BBOV11; só na base antiga: AEFI11, AERO11, AFCR11, AFOF11, AGCX11, ALZM11, ALZT11, AQPA11, ARCT11, ASMT11, BARI11, BBFI11, BBPO11, BBVJ11, BCFF11).

### Campos que vieram da fonte nova

Variação relativa entre a base atual e a nova, nos ativos com o campo preenchido nas duas.

| Campo | Comparados | Diferença mediana | Acima de 5% | Acima de 20% |
|---|---|---|---|---|
| Preço (R$) | 377 | 1,3% | 43 | 3 |
| Liquidez diária (R$) | 353 | 0,7% | 35 | 9 |
| Volatilidade 1 ano (%) | 321 | 0,3% | 7 | 0 |
| Maior queda 1 ano (%) | 346 | 0,0% | 3 | 0 |
| DY 12 meses (%) | 282 | 11,0% | 199 | 109 |
| P/VP | 344 | 1,3% | 39 | 3 |

### Qual medida de liquidez da B3 bate com a fonte antiga

Ativos com liquidez antiga acima de R$ 100 mil. Em todas as janelas, pregão sem negócio conta zero. A peneira usa a janela do arquivo de critérios: 42 pregões nos FIIs.

| Janela | Ativos | Diferença mediana | Diferença mediana (absoluta) | Acima de 10% |
|---|---|---|---|---|
| 2 meses | 202 | 3,6% | 4,3% | 18 |
| 2 meses so dias com negocio | 202 | 3,9% | 4,6% | 40 |
| 21 pregoes | 202 | -1,5% | 16,8% | 133 |
| 42 pregoes | 202 | 0,5% | 0,8% | 2 |
| 63 pregoes | 202 | -6,8% | 8,7% | 91 |

### O que muda no resultado do método

Ranqueados: 61 antes, 60 depois. Entraram 3, saíram 4, continuaram 57.

**Entraram no ranking**

| Ativo | Antes saía por | Posição agora |
|---|---|---|
| LIFE11 | Volatilidade de 23.3% a.a., entre os 20% mais voláteis do grupo tijolo (corte em 23.2%) | 2º (tijolo) |
| BCIA11 | Liquidez média diária R$ 0,5 mi abaixo de R$ 0,5 mi | 3º (fof) |
| CYCR11 | não estava na base | 8º (papel) |

**Saíram do ranking**

| Ativo | Posição antes | Motivo agora |
|---|---|---|
| PSEC11 | 1º (fof) | Sem informe mensal de FII na CVM: Fiagro, FI-Infra ou fundo sem cadastro como FII |
| TVRI11 | 3º (tijolo) | Sem informe mensal de FII na CVM: Fiagro, FI-Infra ou fundo sem cadastro como FII |
| VGIP11 | 4º (papel) | Volatilidade de 20.6% a.a., entre os 20% mais voláteis do grupo papel (corte em 19.7%) |
| PMLL11 | 18º (tijolo) | Sem informe mensal de FII na CVM: Fiagro, FI-Infra ou fundo sem cadastro como FII |

**Top 14 fof**: 13 de 14 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | PSEC11 | JSAF11 |
| 2 | CPTS11 | CPTS11 |
| 3 | RBRX11 | BCIA11 (novo) |
| 4 | JSAF11 | HFOF11 |
| 5 | BTHF11 | KFOF11 |
| 6 | HFOF11 | RBRX11 |
| 7 | KFOF11 | BTHF11 |
| 8 | GARE11 | GARE11 |
| 9 | RINV11 | HGBL11 |
| 10 | HGBL11 | SEED11 |
| 11 | RZLC11 | SNEL11 |
| 12 | SNEL11 | RINV11 |
| 13 | SNME11 | SNME11 |
| 14 | SEED11 | RZLC11 |

**Top 20 papel**: 18 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | HABT11 | HABT11 |
| 2 | RZAK11 | VCJR11 |
| 3 | VCJR11 | HSAF11 |
| 4 | VGIP11 | RECR11 |
| 5 | RECR11 | VRTA11 |
| 6 | HSAF11 | RZAK11 |
| 7 | VRTA11 | PORD11 |
| 8 | VGIR11 | CYCR11 (novo) |
| 9 | RBRR11 | XPCI11 |
| 10 | PORD11 | RBRY11 |
| 11 | RBRY11 | RBRR11 |
| 12 | BTCI11 | ICRI11 |
| 13 | CLIN11 | BTCI11 |
| 14 | XPCI11 | VGIR11 |
| 15 | ICRI11 | CLIN11 |
| 16 | HGCR11 | HGCR11 |
| 17 | KNIP11 | KNIP11 |
| 18 | HREC11 | KNHY11 |
| 19 | KNHY11 | HREC11 |
| 20 | MCCI11 | KNSC11 (novo) |

**Top 20 tijolo**: 18 de 20 continuam.

| # | Antes | Depois |
|---|---|---|
| 1 | BRCR11 | BRCR11 |
| 2 | GTWR11 | LIFE11 (novo) |
| 3 | TVRI11 | GTWR11 |
| 4 | JSRE11 | JSRE11 |
| 5 | HGRE11 | HGRE11 |
| 6 | RCRB11 | RCRB11 |
| 7 | RBRP11 | VILG11 |
| 8 | VILG11 | FATN11 |
| 9 | FATN11 | RBRP11 |
| 10 | TJKB11 | TJKB11 |
| 11 | HGBS11 | CPSH11 |
| 12 | CPSH11 | HGRU11 |
| 13 | HGRU11 | BRCO11 |
| 14 | BRCO11 | KNHF11 |
| 15 | KNHF11 | LVBI11 |
| 16 | LVBI11 | HGBS11 |
| 17 | XPLG11 | XPLG11 |
| 18 | PMLL11 | HGLG11 |
| 19 | HGLG11 | KNRI11 |
| 20 | KNRI11 | ALZR11 (novo) |

### Maiores diferenças por campo

Para conferir na fonte: o valor antigo, o novo e a variação.

**Preço (R$)**: KNRE11 0,27 → 0,19 (-30%); HGAG11 13,00 → 16,50 (27%); RBDS11 1,90 → 1,50 (-21%); VVRI11 8,68 → 7,60 (-12%); MFII11 26,88 → 29,58 (10%); LIFE11 5,81 → 6,39 (10%); CNES11 1,62 → 1,78 (10%); ERPA11 115,03 → 125,48 (9%)

**Liquidez diária (R$)**: LSOI11 69 → 1.181 (1.625%); PLTB11 2 → 0 (-100%); FZDB11 189 → 0 (-100%); GFDL11 15.082 → 3.183 (-79%); BFCC11 5 → 8 (50%); RBRI11 96 → 124 (30%); RBDS11 66 → 85 (28%); CNES11 364.215 → 464.099 (27%)

**Volatilidade 1 ano (%)**: HGBS11 13,2 → 14,4 (9%); LIFE11 23,3 → 25,2 (8%); VRTM11 18,5 → 19,8 (7%); XPML11 16,2 → 17,1 (6%); VISC11 16,3 → 17,2 (5%); BNFS11 26,8 → 28,1 (5%); FIXX11 15,0 → 15,7 (5%); WHGR11 18,9 → 19,7 (4%)

**Maior queda 1 ano (%)**: SHPP11 -24,3 → -26,0 (7%); ZAGH11 -42,7 → -45,5 (6%); ZAVC11 -15,1 → -14,3 (-6%); IAGR11 -23,1 → -24,0 (4%); TORD11 -60,4 → -59,7 (-1%); HGIC11 -47,7 → -47,9 (0%); KOPA11 -72,6 → -72,7 (0%); ZAVI11 -21,7 → -21,7 (0%)

**DY 12 meses (%)**: BTAL11 3,80 → 33,83 (789%); IAAG11 3,95 → 20,64 (423%); BTRA11 2,43 → 8,78 (262%); HAAA11 1,12 → 3,65 (226%); CPOF11 4,82 → 13,15 (173%); RMBS11 13,71 → 35,01 (155%); PDBM11 5,49 → 12,70 (131%); RZZI11 6,26 → -0,01 (-100%)

**P/VP**: KNRE11 0,79 → 0,56 (-30%); HGAG11 0,55 → 0,70 (27%); RBDS11 0,08 → 0,06 (-21%); VVRI11 1,01 → 0,88 (-12%); MFII11 0,28 → 0,30 (10%); LIFE11 0,61 → 0,67 (10%); CNES11 0,26 → 0,28 (10%); ERPA11 0,69 → 0,76 (9%)

