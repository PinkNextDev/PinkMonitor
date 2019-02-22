"""
Configuration module.
"""

import logging


log = logging.getLogger("config")

try:
    from .local_config import * # pylint: disable=W0401,W0614
    RPC_PORT; SERVER_IP; RPC_USER; RPC_PASSWORD
except ImportError:
    log.error("Missing local_config.py file")
    exit(1)
except NameError:
    log.error("Missing one of parameters: RPC_PORT, SERVER_IP, RPC_USER, RPC_PASSWORD")

# SERVER_IP = "18.224.37.139" # "127.0.0.1"
SERVER_URL = "http://" + SERVER_IP + ":" + str(RPC_PORT)

BITTREX_PRICE_URL = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-pink"
BITTREX_DAILY_PRICES_URL = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-PINK&tickInterval=day"

data_folder = "blockchain"
