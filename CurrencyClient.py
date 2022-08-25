import requests
import time
import threading


cache = dict()
ACCESS_KEY = 'insert your access key from exchangeratesapi.io'
URL = 'https://api.apilayer.com/exchangerates_data/latest'


class GetDataFromCache:
    def __init__(self):
        pass

    def get_data_from_cache(self, symbol: str):
        print("-- Get data from cache --")
        print(cache[symbol])
        return cache[symbol]


class GetDataFromResponse:
    def __init__(self):
        pass

    def get_data_from_server(self, symbol: str):
        payload = {"access_key": ACCESS_KEY,
                   "symbols": symbol.upper()}
        headers = {"apikey": ACCESS_KEY}
        r = requests.request("GET", URL, headers=headers, params=payload)
        print(f" -- Get data from server, status code: {r.status_code} --")
        print(r.json()["rates"])
        cache[symbol] = r.json()["rates"]
        return r


class CurrencyClient:
    def __init__(self):
        self.getDataFromCache = GetDataFromCache()
        self.getDataFromResponse = GetDataFromResponse()

    def get_currency(self, symbol: str):
        if not cache:
            self.getDataFromResponse.get_data_from_server(symbol)
        else:
            if symbol in cache.keys():
                self.getDataFromCache.get_data_from_cache(symbol)
            else:
                cache[symbol] = self.getDataFromResponse.get_data_from_server(symbol).json()["rates"]



    def set_interval(self, secs: int):
        print("-- Interval started -- ")
        interval = threading.Thread(target=self.clear_cache, args=(secs,))
        interval.start()

    def clear_cache(self, secs: int):
        time.sleep(secs)
        cache.clear()
        print("-- Cache cleaned --")
        print("-- Interval ended --")





