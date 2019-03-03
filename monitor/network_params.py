"""
Pinkcoin network parameters.
"""


# In seconds
BLOCK_TIME = {"pow": 120, "pos": 360, "fps": 60}

# Reward in a block.
BLOCK_REWARD = {"pow": 50, "pos": 100, "fps": 150}

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

TOTAL_REWARD_PER_DAY = {
    "pow": BLOCKS_PER_DAY["pow"]*BLOCK_REWARD["pow"],
    "pos": BLOCKS_PER_DAY["pos"]*BLOCK_REWARD["pos"],
    "fps": BLOCKS_PER_DAY["fps"]*BLOCK_REWARD["fps"]
}

COINS_MINTERD_PER_DAY = TOTAL_REWARD_PER_DAY["pow"] + \
                        TOTAL_REWARD_PER_DAY["pos"] + TOTAL_REWARD_PER_DAY["fps"]

# UTC time.
FLASH_HOURS = [1, 6, 15, 20]


POW_LIMIT = 0x00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
POS_LIMIT = 0x003fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
FPOS_LIMIT = 0x003fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

POW_TARGET_TIMESPAN = 60*60 # 1 hour in seconds
POW_TARGET_SPACING = 120 # 2 minutes in seconds

POS_TARGET_TIMESPAN = 2*60*60 # 2 minutes in seconds
POS_TARGET_SPACING = 360 # 6 minutes in seconds

FPOS_TARGET_TIMESPAN = 10*60 # 10 minutes in seconds
FPOS_TARGET_SPACING = 60 # 1 minute in seconds
