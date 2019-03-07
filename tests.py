
import time

from monitor.rpc import (
    get_block_count, get_block_by_number, get_block_hash, get_block_data, get_raw_transaction
)


start_time = time.time()

try:
    blocks_num  = get_block_count()
except:
    # TODO: Gracefully shut down.
    exit(1)
print(blocks_num)

chain = []

def main():
    for i in range(100):
        try:
            block = get_block_by_number(i)
        except:
            # TODO: Gracefully shut down.
            exit(1)
        chain.append(block)

print(get_block_by_number(100000))

if __name__ == "__main__":
    main()
    print(f"Elapsed time: {(time.time() - start_time)} seconds")
