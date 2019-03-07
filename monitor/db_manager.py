
from os import path
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from datetime import datetime
import logging

from .rpc import (
    get_block_count, get_block_by_number,
    get_block_hash, get_block_data, get_raw_transaction
)
from .db_models import Base
from . import config


log = logging.getLogger("dbmanager")


class DBManager:

    columns = (
        "hash", "size", "height", "version", "merkleroot", "mint", "time", "nonce",
        "bits", "difficulty", "blocktrust", "chaintrust", "previousblockhash",
        "nextblockhash", "flags", "proofhash", "entropybit", "modifier", "tx", "signature",
    )
    chunk_size = 1000

    def __enter__(self):
        log.info(f"Connecting to database...")
        self.engine = create_engine(config.DB_CONFIG)
        self.connection = self.engine.connect()
        if not self.engine.dialect.has_table(self.engine, "blockchain"):
            Base.metadata.create_all(self.engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def update(self):
        log.info(f"Updating blockchain data...")
        data = None
        try:
            blocks_count = get_block_count()
            if not blocks_count:
                log.error("None blocks_count value: issue with RPC connection!")
                exit(1)
            with self.engine.connect() as conn, conn.begin():
                row_query = "SELECT * FROM blockchain ORDER BY height DESC LIMIT 1"
                last_row = pd.read_sql_query(row_query, conn)
                start_block = 0
                if len(last_row) == 1:
                    start_block = last_row["height"].iloc[0] + 1
                for i in range(start_block, blocks_count + 1, self.chunk_size):
                    to = np.clip(i + self.chunk_size, i, blocks_count + 1)
                    data = self.collect_data(i, to)
                    data = data.set_index("height")
                    data.to_sql("blockchain", self.engine, chunksize=1000, if_exists="append")
        except Exception as err:
            log.error(err)

    def collect_data(self, start_block, end_block):
        log.info(f"Collecting blockchain data for blocks from {start_block} to {end_block}...")
        subchain = []
        for i in range(start_block, end_block):
            if i%100 == 0:
                log.info(f"Block number {i}")
            block = get_block_by_number(i)
            block["time"] = datetime.utcfromtimestamp(block["time"])
            del block["confirmations"]
            subchain.append(block)
        return pd.DataFrame(subchain, columns=self.columns)
