import random
from unittest import TestCase

from chainlink.contract_address import SEPOLIA_DATAFEED
from chainlink.feed.main import get_price


class DataFeedTest(TestCase):
    def test_data_feed_for_sepolia(self):
        res = get_price("https://rpc.ankr.com/eth_sepolia", SEPOLIA_DATAFEED)
        random_key = random.choice(list(res.keys()))
        assert res[random_key] != ""
