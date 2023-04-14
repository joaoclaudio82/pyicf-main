"""Data collector classes"""
from datetime import date
from datetime import datetime
from pathlib import Path

import tqdm

import toml

import requests

import pandas as pd

from tvDatafeed import TvDatafeed, Interval

from .constants import BCB_SERIES_BASE_URL
from .constants import BCB_SERIES_CODES
from .constants import BCB_SELIC_SERIES_CODES
from .constants import DATE_FORMAT
from .constants import DATE_FORMAT_BCB
from .constants import DATE_FORMAT_WITH_TIME

from .constants import TRADINGVIEW_SERIES_CODES
from .constants import WORLD_GOVERNMENT_BONDS_URL
from .constants import WORLD_GOVERNMENT_BONDS_URL_SUFFIX
from .constants import WORLD_GOVERNMENT_BONDS_CDS
from .constants import WORLD_GOVERNMENT_BONDS_HEADERS

from .tools import int_to_datetime

BCB_SERIES_CODES_DICT = {a[0]: a[1] for a in BCB_SERIES_CODES}
BCB_SERIES_CODES_LIST = [a[1] for a in BCB_SERIES_CODES]
BCB_SELIC_SERIES_CODES_DICT = {a[0]: a[1] for a in BCB_SELIC_SERIES_CODES}


TRADINGVIEW_SERIES_CODES_DICT = {
    a[0]: (a[1], a[2], a[3]) for a in TRADINGVIEW_SERIES_CODES
}

WORLD_GOVERNMENT_BONDS_CDS_DICT = {
    a[0]: a[1:] for a in WORLD_GOVERNMENT_BONDS_CDS
}
WORLD_GOVERNMENT_BONDS_HEADERS_DICT = {
    a[0]: a[1] for a in WORLD_GOVERNMENT_BONDS_HEADERS
}

ICF_COMPONENTS_KEYS = tuple(TRADINGVIEW_SERIES_CODES_DICT.keys()) \
                    + tuple(WORLD_GOVERNMENT_BONDS_CDS_DICT.keys())

SERIES_DATA_LOCATION = (
    'series_worldgovernmentbonds',
    'series_tradignview',
    'series_cbonds',
    'series_bcb'
)

class TimeSeriesWorldGovernmentBonds:
    """
     Download series from http://www.worldgovernmentbonds.com/
    """
    def __init__(self,
                 data_location: str='database'):
        self.__data_location = Path(data_location)
        self.__series_location = Path(data_location) / SERIES_DATA_LOCATION[0]
        if isinstance(data_location, str):
            data_location = Path(data_location)
        self.__data_location = data_location
        if not self.__data_location.is_dir():
            self.__data_location.mkdir()
        if not self.__series_location.is_dir():
            self.__series_location.mkdir()

    def __get_series(self, name: str, store_data=True):
        """
        __get_series

        Resquest json data from http://www.worldgovernmentbonds.com/ and
        save them as csv file.

        Parameters
        ----------
        name : str
            name of the series. Check pyicf.constants.WORLD_GOVERNMENT_BONDS_CDS
        store_data : bool, optional
            Whether store data, by default True

        Returns
        -------
        pd.DataFrame
            DataFrame object
        """
        headers = WORLD_GOVERNMENT_BONDS_HEADERS_DICT
        headers['Referer'] += WORLD_GOVERNMENT_BONDS_CDS_DICT[name][-1]
        url = WORLD_GOVERNMENT_BONDS_URL
        url+= str(WORLD_GOVERNMENT_BONDS_CDS_DICT[name][0])
        url+= WORLD_GOVERNMENT_BONDS_URL_SUFFIX
        url+= WORLD_GOVERNMENT_BONDS_CDS_DICT[name][1]
        with requests.Session() as session:
            session.headers['User-Agent'] = headers['User-Agent']
            response = session.get(url, headers=headers, timeout=150)
            if response.ok:
                data = response.json()
                df = pd.DataFrame([
                    [
                        int_to_datetime(data['quote'][key][0], strformat=DATE_FORMAT_WITH_TIME),
                        data['quote'][key][1]
                    ] for key in data['quote']
                ], columns=['datetime', 'close'])
                if store_data:
                    filename = self.__series_location / f'{name}.csv'
                    df.to_csv(filename, index=False)
                return df

    def update_database(self,):
        print("Getting data from WorldGovernmentBonds")
        for name in tqdm.tqdm(WORLD_GOVERNMENT_BONDS_CDS_DICT, desc='CDS'):
            self.__get_series(name, store_data=True)

    def load_series(self, name):
        if name not in WORLD_GOVERNMENT_BONDS_CDS_DICT:
            keys = tuple(k for k in WORLD_GOVERNMENT_BONDS_CDS_DICT)
            message = f"Invalid key '{name}'. Valid keys are: {keys}"
            raise KeyError(message)
        filename = self.__series_location / f'{name}.csv'
        return pd.read_csv(filename)


class TimeSeriesTradingview(TvDatafeed):
    def __init__(self,
                 data_location: str='database',
                 username: str=None,
                 password: str=None):
        super().__init__(username, password)
        self.__data_location = Path(data_location)
        self.__series_location = Path(data_location) / SERIES_DATA_LOCATION [1]
        if isinstance(data_location, str):
            data_location = Path(data_location)
        self.__data_location = data_location
        if not self.__data_location.is_dir():
            self.__data_location.mkdir()
        if not self.__series_location.is_dir():
            self.__series_location.mkdir()

    def __get_series(self,
                     name: str,
                     interval: Interval=Interval.in_monthly,
                     n_bars=10*12,
                     store_data=False):
        data = self.get_hist(
            symbol=TRADINGVIEW_SERIES_CODES_DICT[name][0],
            exchange=TRADINGVIEW_SERIES_CODES_DICT[name][1],
            interval=interval,
            n_bars=n_bars,
            fut_contract=TRADINGVIEW_SERIES_CODES_DICT[name][2]
        )
        if store_data:
            filename = self.__series_location / f'{name}.csv'
            data.to_csv(filename)
        return data

    def update_database(self,):
        print("Getting data from TradingView")
        for name in tqdm.tqdm(TRADINGVIEW_SERIES_CODES_DICT, desc='TradingView series'):
            self.__get_series(name, store_data=True)

    def load_series(self, name):
        if name not in TRADINGVIEW_SERIES_CODES_DICT:
            keys = tuple(k for k in TRADINGVIEW_SERIES_CODES_DICT)
            message = f"Invalid key '{name}'. Valid keys are: {keys}"
            raise KeyError(message)
        filename = self.__series_location / f'{name}.csv'
        return pd.read_csv(filename)


class TimeSeriesCbonds:
    def __init__(self,
                 data_location: str='database'):
        super().__init__(username, password)
        self.__data_location = Path(data_location)
        self.__series_location = Path(data_location) / SERIES_DATA_LOCATION [2]
        if isinstance(data_location, str):
            data_location = Path(data_location)
        self.__data_location = data_location
        if not self.__data_location.is_dir():
            self.__data_location.mkdir()
        if not self.__series_location.is_dir():
            self.__series_location.mkdir()


class TimeSeriesBCB:
    def __init__(self,
                 data_location: str='database'):
        self.__data_location = Path(data_location)
        self.__series_location = Path(data_location) / SERIES_DATA_LOCATION [3]
        if isinstance(data_location, str):
            data_location = Path(data_location)
        self.__data_location = data_location
        if not self.__data_location.is_dir():
            self.__data_location.mkdir()
        if not self.__series_location.is_dir():
            self.__series_location.mkdir()

    def __get_data(self, ):
        pass

    def __check_series_key(self, series: str):
        try:
            BCB_SERIES_CODES_DICT[series]
            return True
        except KeyError:
            keys = tuple(a[0] for a in BCB_SERIES_CODES)
            message =f"`series` must be a valid key: {keys}"
            print(message)
            return False
        except TypeError:
            keys = tuple(a[0] for a in BCB_SERIES_CODES)
            message =f"`series` must be str and a valid key: {keys}"
            print(message)
            return False

    def open_series(self, series: str='juros_selic'):
        series_file = self.__series_location / f'{series}.csv'
        return pd.read_csv(series_file)

    def __download_bcb_series(self,
                            data_inicial: str,
                            data_final: str,
                            series: str='juros_selic'):
        selic_file = self.__series_location / f'{series}.csv'
        if self.__check_series_key(series):
            code_series = BCB_SERIES_CODES_DICT[series]
            url = BCB_SERIES_BASE_URL + self.__selic_params(
                data_inicial, data_final, code_series
            )
            # print(url)
            data = pd.read_csv(url, sep=";")
            data.to_csv(selic_file, index=False)
            return data
        else:
            return None

    def update_database(self,):
        for key, _, start_date in BCB_SERIES_CODES:
            end_date = date.today().strftime(DATE_FORMAT_BCB)
            self.__download_bcb_series(start_date, end_date, key)
            

    def __selic_params(self, data_inicial: str, data_final: str, code_series: int):
        """
        __selic_params

        Parâmetros de requerimento de dados de taxa selic na
        API do Banco Central do Brasil:
            <code_series>/dados?formato=csv&dataInicial=<data_inicial>&dataFinal=<data_final>

        Parameters
        ----------
        data_inicial : str
            Data inicial no formato %d/%m/%Y
        data_final : str
            Data final no formato %d/%m/%Y

        Returns
        -------
        dict
            Dicionário de parametros da requisição.
        """
        dict_params = {
            'formato': 'csv',
            'dataInicial': data_inicial,
            'dataFinal': data_final
        }

        params = f"{code_series}/dados?"
        params += "&".join([f"{key}={value}" for key, value in dict_params.items()])
        return params


class RawComponents:
    def __init__(self,
                 data_location: str='database',
                 auth_file: str='.auth.toml',
                 update_database: bool=False):
        tradingview_username = None
        tradingview_password = None
        try:
            auth = toml.load(auth_file)
            tradingview_username = auth['tradingview']['username']
            tradingview_password = auth['tradingview']['password']
        except FileNotFoundError:
            pass
        self.__data_location = Path(data_location)

        self.__tradingview = TimeSeriesTradingview(
            data_location=data_location,
            username=tradingview_username,
            password=tradingview_password
        )
        self.__worldgovbonds = TimeSeriesWorldGovernmentBonds(
            data_location=data_location,
        )
        if update_database:
            self.__tradingview.update_database()
            self.__worldgovbonds.update_database()

    def load_series(self, name):
        if name in TRADINGVIEW_SERIES_CODES_DICT:
            return self.__tradingview.load_series(name)
        elif name in WORLD_GOVERNMENT_BONDS_CDS_DICT:
            return self.__worldgovbonds.load_series(name)

    def update_database(self,):
        self.__tradingview.update_database()
        self.__worldgovbonds.update_database()    

    def build_dataframe(self, store_data=True):
        series = []
        for name in TRADINGVIEW_SERIES_CODES_DICT:
            df = self.__tradingview.load_series(name)
            df = df[['datetime','close']]
            df['datetime'] = df['datetime'].apply(
                lambda x:
                    datetime.strptime(x.split(' ')[0], DATE_FORMAT)
            )
            df = df.rename(columns={'close': name}).set_index('datetime')
            series.append(df)
        for name in WORLD_GOVERNMENT_BONDS_CDS_DICT:
            df = self.__worldgovbonds.load_series(name)
            df['datetime'] = df['datetime'].apply(
                lambda x: datetime.strptime(x.split(' ')[0], DATE_FORMAT)
            )
            df_monthly = pd.DataFrame([])
            for index in df.index:
                if index < df.shape[0] - 2:
                    current_date = df.loc[index, 'datetime']
                    next_date = df.loc[index + 1, 'datetime']
                    if next_date.month > current_date.month or\
                        (next_date.month == 1 and current_date.month == 12):
                        df_monthly = pd.concat([df_monthly, df.iloc[[index]]], axis=0)
            df_monthly = df_monthly.rename(columns={'close': name}).set_index('datetime')
            # df = df.rename(columns={'close': name}).set_index('datetime')
            series.append(df_monthly)
            # series.append(df)
        joined = pd.concat(series, axis=1)
        if store_data:
            joined.to_csv(self.__data_location / 'icf_raw_components.csv')
        return joined

