# Descrição dos valores em data/constants.py

O módulo `data.collector` obtém os dados de séries a partir de sites ou apis.

## TRADINGVIEW_SERIES_CODES

Para obter uma série temporal a partir do site [https://www.tradingview.com](https://www.tradingview.com) são necessários pelo menos dois parâmetros: `symbol`, que é o símbolo do indicador como consta na página, e `exchange`, que corresponde ao operador ou um classificador daquele símbolo. Por exemplo, para o barril de petróleo WTI, temos que `symbol = 'USOIL'` e `exchange = 'TVC'`.

A constante `TRADINGVIEW_SERIES_CODES` é uma tupla que contém três colunas, como no exemplo abaixo:

|chave       |                 symbol |               exchange |
|------------|------------------------|------------------------|
|oil_wti     |                  USOIL |                    TVC |

## BCB_SERIES_CODES

Source [https://dadosabertos.bcb.gov.br](https://dadosabertos.bcb.gov.br).

Esta tupla contém três columnas, e abaixo segue um exemplo:

|chave       | código da série no BCB | data de início da série|
|------------|------------------------|------------------------|
|juros_selic |                     11 |             04/06/1986 |

### Séries do BCB

#### Selic

Taxa de juros que representa a taxa média ajustada das operações compromissadas com prazo de um dia útil lastreadas com títulos públicos federais custodiados no Sistema Especial de Liquidação e de Custódia (Selic). Divulgação em % a.a.

- `juros_selic`: Taxa de juros Selic.
- `juros_selic_year_252`:  Selic anualizada base 252.
- `juros_selic_year_monthly_252`: Selic acumulada no mês anualizada base 252.

#### Juros de crédito

Conceito: Taxa média de juros das novas operações de crédito contratadas no período de referência no Sistema Financeiro Nacional. Taxa ponderada pelo valor das concessões. Inclui operações contratadas no segmento de crédito livre e no segmento de crédito direcionado.

- `juros_credito`: Taxa média de juros das operações de crédito - Total.
- `juros_credito_monthly`: Taxa média mensal de juros das operações de crédito - Total.
- `juros_credito_mei`: Taxa média de juros das operações de crédito - MEI .