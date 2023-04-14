# pyicf

Python package for analysing the Financial Condition Indicator

## Installation (Linux/Mac OS users)

Create a new environment:

```bash
python -m venv .env
```

Activate environment:

```bash
source .env/bin/activate
```

And install requirements:

```bash
pip install -r requirements.txt
```

## Configuration

Some series are extracted from [www.tradingview.com](https://www.tradingview.com). Some of those might require user authentication. Therefore, created a TradingView account and put your credentials in a file called `.auth.toml`:

```conf
[tradingview]
username = "your_user"
email = "your@email.com"
password = "YOUR_PASSWORD"
```
## Basic Usage

Check sample IPython Notebook `icf.ipynb`. This notebook requires:

- `matplotlib==3.7.1`
- `scikit-learn==1.2.2`

which should already be installed if you ran `pip install -r requirements.txt`

## API

Before using the package, one must download the database.

### pyicf.RawComponents

```python
import pyicf

username = "your_user"
password = "YOUR_PASSWORD"

icf_raw = pyicf.RawComponents(auth_file='.auth.toml')
icf_raw.update_database()
icf_rawdata = icf_raw.build_dataframe()
```

The variable `icf_rawdata` will contain the dataframe containing the indexes tha

### Download de séries do TrandingView

```python
import pyicf

username = "your_user"
password = "YOUR_PASSWORD"

series = pyicf.TimeSeriesTradingview(username=username, password=password)
series.update_database()
```

The downloaded data in .csv format can be found in `data/series_tradingview/`

### Download de séries do BCB

```python
import pyicf
series = pyicf.TimeSeriesBCB()
series.update_database()
```

The downloaded data in .csv format can be found in `data/series_tradingview/`

## A fazer

- [ ] Add loggers.
- [ ] Build API for data collection.

### Data API collector:

| Série                                         | Status            | Fonte       |
|-----------------------------------------------|-------------------|-------------|
| Swap Pré-DI 1 ano                             | ok                | Tradingview |
| Swap Pré-DI 5 anos                            | ok                | Tradingview |
| Juros EUA 3 meses                             | ok                | Tradingview |
| Juros EUA 2 anos                              | ok                | Tradingview |
| Juros EUA 10 anos                             | ok                | Tradingview |
| Juros Reino Unido 3 meses                     | ok                | Tradingview |
| Juros Reino Unido 2 anos                      | ok                | Tradingview |
| Juros Reino Unido 10 anos                     | ok                | Tradingview |
| Juros Alemanha 3 meses                        | ok                | Tradingview |
| Juros Alemanha 2 anos                         | ok                | Tradingview |
| Juros Alemanha 10 anos                        | ok                | Tradingview |
| Juros Japão 3 meses                           | ok                | Tradingview |
| Juros Japão 2 anos                            | ok                | Tradingview |
| Juros Japão 10 anos                           | ok                | Tradingview |
| CDS Brasil (5 anos)                           | ok                | cbonds      |
| VIX                                           | ok                | Tradingview |
| US dollar indexes (desenvolvidos)             | ok                | Tradingview |
| US dollar indexes (emergentes)                | ok                | Tradingview |
| Taxa de câmbio (R\$/US\$)                     | ok                | Tradingview |
| Cotações em US$ do barril de petróleo (WTI)   | ok                | Tradingview |
| Cotações em US$ do barril de petróleo (Brent) | ok                | Tradingview |
| Índices de commodities CRB (foodstuffs)       | ok (to be checked)| Tradingview |
| Índices de commodities CRB (metals)           | ok (to be checked)| Tradingview |
| Índices de ações MSCI (desenvolvidos)         | ok (to be checked)| Tradingview |
| Índices de ações MSCI (emergentes)            | ok (to be checked)| Tradingview |
| Ibovespa                                      | ok                | Tradingview |

## References and sources

- [tvdb.brianthe.dev](https://tvdb.brianthe.dev/): consult informations about the symbol, *exchange* and *screener*, at TradingView in order to feed the input data to functions and classes. [tvDataFeed](https://github.com/StreamAlpha/tvdatafeed).