"""
Project configuration.
"""

import logging
from configparser import ConfigParser, Error


logging.basicConfig(level=logging.INFO)
log = logging.getLogger("config")
config = ConfigParser()

try:
    config.read("config.ini")
    if config.sections() == []:
        log.error("Missing proper config.ini file")
        exit(1)

    RPC_PORT = config.get("NODE", "RPC_PORT")
    SERVER_IP = config.get("NODE", "SERVER_IP")
    RPC_USER = config.get("NODE", "RPC_USER")
    RPC_PASSWORD = config.get("NODE", "RPC_PASSWORD")

    DB_USER = config.get("DATABASE", "DB_USER")
    DB_PASSWORD = config.get("DATABASE", "DB_PASSWORD")
    DB_NAME = config.get("DATABASE", "DB_NAME")
    DB_PORT = config.get("DATABASE", "DB_PORT")

except Error as err:
    log.error(err)
    exit(1)

RPC_SERVER_URL = f"http://{SERVER_IP}:{RPC_PORT}"
DB_CONFIG = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:{DB_PORT}/{DB_NAME}"

BITTREX_PRICE_URL = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-pink"
BITTREX_DAILY_PRICES_URL = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-PINK&tickInterval=day"
