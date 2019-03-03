"""
Utility functions.
"""
from . import network_params as params


def calc_net_power(diff, blocks_num: int, algo: str="pow"):
    """
    Calulcates average network hash power (for one hour period).

    :param diff: Difficlty dictionary in candlestic format.
    :param blocks_num (int): Number of blocks in one hour.
    :param algo (str): Algorithm ("pow", "pos", "fpos")
    """
    net_power_mod = blocks_num[algo]/params.BLOCKS_PER_HOUR[algo]
    net_power_mod *= 2**32/params.BLOCK_TIME[algo]

    return {
        "open": diff[algo]["open"]*net_power_mod,
        "high": diff[algo]["high"]*net_power_mod,
        "low": diff[algo]["low"]*net_power_mod,
        "close": diff[algo]["close"]*net_power_mod,
        "average": diff[algo]["average"]*net_power_mod
    }

def calc_stats(diff, blocks_sum, time, algo="pow"):
    """
    """
    diff[algo]["average"] = diff[algo]["average"]/blocks_sum[algo] if blocks_sum[algo] else 0
    power = calc_net_power(diff, blocks_sum, algo)

    blocks_num_diff = blocks_sum[algo]
    if time in params.FLASH_HOURS:
        if algo != "pos":
            blocks_num_diff -= params.BLOCKS_PER_HOUR[algo]
    elif algo != "fps":
            blocks_num_diff -= params.BLOCKS_PER_HOUR[algo]

    return {
        "difficulty": diff[algo],
        "power": power,
        "blocks_num_diff": blocks_num_diff
    }

def fill_data(diff_block, diff, blocks_sum, algo="pow"):
    """
    """
    if not diff[algo]["open"]:
        diff[algo]["open"] = diff_block
    diff[algo]["high"] = diff_block if diff_block > diff[algo]["high"] else diff[algo]["high"]
    diff[algo]["low"] = diff_block if not diff[algo]["low"] or diff_block < diff[algo]["low"] else diff[algo]["low"]
    diff[algo]["close"] = diff_block
    diff[algo]["average"] += diff_block
    blocks_sum[algo] += 1
