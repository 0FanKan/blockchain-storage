from app_blockchain import sync

node_blocks = sync.sync()


def nodes():

    node_blocks = sync.sync()
    python_blocks = []

    for block in node_blocks:
        block_index = str(block.index)
        block_timestamp = str(block.timestamp)
        block_data = str(block.data)
        block_hash = block.hash
        block_prev_hash = block.prev_hash
        block_nonce = block.nonce
        block = {
            "index": block_index,
            "timestamp": block_timestamp,
            "data": block_data,
            "prev_hash": block_prev_hash,
            "hash": block_hash,
            "Nonce": block_nonce
        }

        python_blocks.append(block)
    return python_blocks
