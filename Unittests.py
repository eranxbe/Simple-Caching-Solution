import unittest
from CurrencyClient import CurrencyClient, cache
import time

class TestCurrencyClient(unittest.TestCase):
    client = CurrencyClient()

    def tearDown(self):
        self.client.clear_cache(0)

    def test_get_one_symbol(self):
        print(f"Test started: test_get_one_symbol")
        self.client.get_currency("gbp")
        time.sleep(3)
        self.client.get_currency("gbp")
        self.client.set_interval(1)
        time.sleep(3)
        self.assertTrue(not cache, "Failed, Cache is not empty")
        self.client.get_currency("gbp")
        print(f"Test ended: test_get_one_symbol")


    def test_get_two_symbols(self):
        print(f"Test started: test_get_two_symbols")
        self.client.get_currency("usd")
        self.client.get_currency("gbp")
        time.sleep(3)
        self.client.get_currency("usd")
        self.client.get_currency("gbp")
        self.client.set_interval(1)
        time.sleep(3)
        self.assertTrue(not cache, "Failed, Cache is not empty")
        self.client.get_currency("usd")
        self.client.get_currency("gbp")
        print(f"Test ended: test_get_two_symbols")