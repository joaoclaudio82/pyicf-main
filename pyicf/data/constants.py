""" Pacote pyicf - análise de indicador de condições financeiras (ICF)
    Module data.constants
"""

DATE_FORMAT = r'%Y-%m-%d'
DATE_FORMAT_BCB = r'%d/%m/%Y'
DATE_FORMAT_WITH_TIME = r'%Y-%m-%d %H:%M:%S'

TRADINGVIEW_SERIES_CODES = (
    ('juros_br01y', 'BR01Y', 'TVC', None),
    ('juros_br05y', 'BR05Y', 'TVC', None),
    ('juros_us03m', 'US03MY', 'TVC', None),
    ('juros_us02y', 'US02Y', 'TVC', None),
    ('juros_us10y', 'US10Y', 'TVC', None),
    ('juros_uk03m', 'GB03MY', 'TVC', None),
    ('juros_uk02Y', 'GB02Y', 'TVC', None),
    ('juros_uk10Y', 'GB10Y', 'TVC', None),
    ('juros_de03m', 'DE03MY', 'TVC', None),
    ('juros_de02Y', 'DE02Y', 'TVC', None),
    ('juros_de10Y', 'DE10Y', 'TVC', None),
    ('juros_jp03m', 'JP03MY', 'TVC', None),
    ('juros_jp02Y', 'JP02Y', 'TVC', None),
    ('juros_jp10Y', 'JP10Y', 'TVC', None),
    ('vix', 'VIX', 'TVC', None),
    ('dollar_index_advanced', 'DTWEXAFEGS', 'FRED', None),
    ('dollar_index_emerging', 'DTWEXEMEGS', 'FRED', None),
    ('brl_usd', 'BRLUSD', 'FX_IDC', None),
    ('oil_wti', 'USOIL', 'TVC', None),
    ('oil_brent', 'UKOIL', 'TVC', None),
    # ('metals', 'WPU10', 'FRED', None),
    ('metals', 'IRON', 'NASDAQ', None),
    # ('foods', 'WPSFD4131', 'FRED', None),
    ('foods', 'SOYBEAN', 'GLOBALPRIME', None),
    ('msci_emerging', 'MME', 'ICEUS', 2),
    ('msci_world', 'MML', 'ICEUS', 2),
    ('ibov', 'IBOV', 'BMFBOVESPA', None),
)

WORLD_GOVERNMENT_BONDS_URL = "http://www.worldgovernmentbonds.com/wp-admin"
WORLD_GOVERNMENT_BONDS_URL+="/admin-ajax.php?action=jsonStoricoCds&area="
WORLD_GOVERNMENT_BONDS_URL_SUFFIX = "&dateRif=2099-12-31&durata="

WORLD_GOVERNMENT_BONDS_CDS = (
    ('cds_brazil5y', 7, '5Y', '/brazil/5-years/'),
)

WORLD_GOVERNMENT_BONDS_USERAGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64;"\
    " rv:109.0) Gecko/20100101 Firefox/111.0"
WORLD_GOVERNMENT_BONDS_HEADERS = (
    ("Accept", "application/json, text/javascript, */*; q=0.01"),
    ("Accept-Encoding", "gzip, deflate"),
    ("Accept-Language", "en-US,en;q=0.5"),
    ("Connection", "keep-alive"),
    ("Host", "www.worldgovernmentbonds.com"),
    ("Referer", "http://www.worldgovernmentbonds.com/cds-historical-data"),
    ("User-Agent", WORLD_GOVERNMENT_BONDS_USERAGENT),
    ("X-Requested-With", "XMLHttpRequest"),
)

GROUPS = (
    (TRADINGVIEW_SERIES_CODES[0][0], 1),
    (TRADINGVIEW_SERIES_CODES[1][0], 1),
    (TRADINGVIEW_SERIES_CODES[2][0], 2),
    (TRADINGVIEW_SERIES_CODES[3][0], 2),
    (TRADINGVIEW_SERIES_CODES[4][0], 2),
    (TRADINGVIEW_SERIES_CODES[5][0], 2),
    (TRADINGVIEW_SERIES_CODES[6][0], 2),
    (TRADINGVIEW_SERIES_CODES[7][0], 2),
    (TRADINGVIEW_SERIES_CODES[8][0], 2),
    (TRADINGVIEW_SERIES_CODES[9][0], 2),
    (TRADINGVIEW_SERIES_CODES[10][0], 2),
    (TRADINGVIEW_SERIES_CODES[11][0], 2),
    (TRADINGVIEW_SERIES_CODES[12][0], 2),
    (TRADINGVIEW_SERIES_CODES[13][0], 2),
    (TRADINGVIEW_SERIES_CODES[14][0], 3),
    (WORLD_GOVERNMENT_BONDS_CDS[0][0], 3),
    (TRADINGVIEW_SERIES_CODES[15][0], 4),
    (TRADINGVIEW_SERIES_CODES[16][0], 4),
    (TRADINGVIEW_SERIES_CODES[17][0], 4),
    (TRADINGVIEW_SERIES_CODES[18][0], 5),
    (TRADINGVIEW_SERIES_CODES[19][0], 5),
    (TRADINGVIEW_SERIES_CODES[20][0],  6),
    (TRADINGVIEW_SERIES_CODES[21][0],  6),
    (TRADINGVIEW_SERIES_CODES[22][0],  7),
    (TRADINGVIEW_SERIES_CODES[23][0],  7),
    (TRADINGVIEW_SERIES_CODES[24][0],  7),
)

WEIGHTS = (
    (1, 0.34),
    (2, 0.33),
    (3, 0.18),
    (4, 0.20),
    (5, 0.23),
    (6, -0.13),
    (7, -0.15),
)

BCB_SERIES_BASE_URL = "https://api.bcb.gov.br/dados/serie/bcdata.sgs."

BCB_SELIC_SERIES_CODES  = (
    ('juros_selic', 11, '04/06/1986'),
    ('juros_selic_year_252', 1178, '04/06/1986'),
    ('juros_selic_year_monthly_252', 4189, '01/06/1986'),
)

BCB_CREDITO_SERIES_CODES = (
    ('juros_credito', 20714, '01/03/2011'),
    ('juros_credito_monthly', 25433, '01/03/2011'),
    ('juros_credito_mei', 26838, '01/01/2016'),
)

BCB_SERIES_CODES = BCB_SELIC_SERIES_CODES + BCB_CREDITO_SERIES_CODES

CBONDS_SERIES_URL = "https://cbonds.com/api/"
CBONDS_SERIES_URL_SUFFIX = "/getGraphicData/"

CBONDS_SERIES_REQUEST_CODES = (
    ('cds_brazil', 'indexes', '13889'),
)

CBONDS_SERIES_REQUEST_PAYLOAD = (
    (
        'cds_brazil',
        ('beginDate', '2018-04-06'),
        ('endDate', '2023-04-05'),
        ('periodId', 1),
    ),
    (
        'cds_brazil',
        ('beginDate', '2018-04-06'),
        ('endDate', '2023-04-06'),
        ('periodId', 1),
    )
)