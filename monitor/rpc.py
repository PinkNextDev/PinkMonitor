"""
Pinkcoin node RPC.
"""

import json
import time
import logging
import requests

from . import config


log = logging.getLogger("rpc")

session = requests.Session()
session.auth = (config.RPC_USER, config.RPC_PASSWORD)
session.headers.update({"content-type": "application/json"})

connection_timeout = 30 # seconds


def execute_rpc(method: str, params=[]):
    """
    Executes specific Pinkcoin node RPC.

    :param method (str): Name of the RPC method.
    :param params (list): List of parameters
    :returns (int or str or Dict or None): result of RPC.
    """
    start_time = time.time()
    payload = {"method": method, "params": params, "jsonrpc": "2.0"}
    while 1:
        try:
            response = session.post(config.RPC_SERVER_URL, data=json.dumps(payload)).json()
            if response["error"]:
                log.error(response["error"])
            return response["result"]
        except requests.ConnectionError:
            log.error("Connection error!")
            if time.time() > start_time + connection_timeout:
                raise Exception(
                    f"Unable to get data after {connection_timeout} seconds of ConnectionErrors"
                )
            else:
                time.sleep(1)
        except Exception as e:
            log.error(e)
            return None

def stop_daemon():
    return execute_rpc("stop")

def set_wallet_passphrase(passphrase, timeout):
    return execute_rpc("walletpassphrase", [passphrase, timeout])

def send_many(account, addresses):
    return execute_rpc("sendmany", [account, addresses])

def get_balance(account=None):
    return execute_rpc("getbalance", [account])

def get_peer_info():
    return execute_rpc("getpeerinfo")

def get_block_count():
    """
    Fetches total number of blocks.

    :returns (int or None): Actual number of blocks in blockchain.
    """
    return execute_rpc("getblockcount")

def get_block_hash(num=1):
    """
    Fetches particular block hash.

    :param num (int): Block number.
    :returns (str or None: Block hash): BLock hash.
    """
    return execute_rpc("getblockhash", [num])

def get_raw_transaction(txid, verbose=True):
    """
    Fetches raw transaction data.

    :param txid (int): ....
    :returns (str or Dict): ...
    """
    return execute_rpc("getrawtransaction", [txid, 1 if verbose else 0])

def get_block_data(block_hash):
    """
    Fetches particular block data (by block hash).

    :param block_hash (str): Block hash.
    :returns (Dict or None): Dictionary with block data (difficulty, flags, etc.).
    """
    return execute_rpc("getblock", [block_hash])

def get_block_by_number(block_number):
    """
    Fetches particular block data (by block number).

    :param block_hash (str): Block hash.
    :returns (Dict or None): Dictionary with block data (difficulty, flags, etc.).
    """
    return execute_rpc("getblockbynumber", [block_number])
