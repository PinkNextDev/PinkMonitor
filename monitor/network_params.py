"""
Pinkcoin network parameters.
"""


# In seconds
BLOCK_TIME = {"pow": 120, "pos": 360, "fps": 60}

# Pinkcoins in block.
BLOCK_COINS = {"pow": 50, "pos": 100, "fps": 150}

BLOCKS_PER_HOUR = {
    "pow": 3600/BLOCK_TIME["pow"],
    "pos": 3600/BLOCK_TIME["pos"],
    "fps": 3600/BLOCK_TIME["fps"],
}

BLOCKS_PER_DAY = {
    "pow": 24*BLOCKS_PER_HOUR["pow"],
    "pos": 20*BLOCKS_PER_HOUR["pos"],
    "fps":  4*BLOCKS_PER_HOUR["fps"],
}

COINS_PER_DAY = {
    "pow": BLOCKS_PER_DAY["pow"]*BLOCK_COINS["pow"],
    "pos": BLOCKS_PER_DAY["pos"]*BLOCK_COINS["pos"],
    "fps": BLOCKS_PER_DAY["fps"]*BLOCK_COINS["fps"]
}

COINS_PER_DAY = COINS_PER_DAY["pow"] + COINS_PER_DAY["pos"] + COINS_PER_DAY["fps"]

# UTC time.
FLASH_HOURS = [1, 6, 15, 20]
