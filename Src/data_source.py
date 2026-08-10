from abc import ABC, abstractmethod


class DataSource(ABC):

    @abstractmethod
    def get_candles(self, symbol, timeframe, limit=100):
        pass


class DemoDataSource(DataSource):

    def get_candles(self, symbol, timeframe, limit=100):
        return []
