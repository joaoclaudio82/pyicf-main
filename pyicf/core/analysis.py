from pathlib import Path

import toml

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from pyicf import RawComponents

AUTH = toml.load('.auth.toml')
username = AUTH['tradingview']['username']
password = AUTH['tradingview']['password']

scaler = StandardScaler()
pca_one_component = PCA(n_components=1)

class Index(RawComponents):
    def __init__(self,
                 data_location: str='database',
                 tradingview_username: str=None,
                 tradingview_password: str=None,
                 update_database=False):
        super().__init__(
            data_location=data_location,
            tradingview_username=tradingview_username,
            tradingview_password=tradingview_password,
            update_database=update_database
        )

        try:
            self.__raw_data = self.build_dataframe(store_data=True)
        except FileNotFoundError:
            self.update_database()
            self.__raw_data = self.build_dataframe(store_data=True)


        data_standardized = scaler.fit_transform(self.__raw_data)
        pca_one_component.fit(data_standardized)

        # self.__data_

    @property
    def raw_data(self):
        return self.__raw_data
