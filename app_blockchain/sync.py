import os
import json
from app_blockchain.block import Block, verification


def sync():
    node_blocks = []
    chaindata_dir = r"app_blockchain/chaindata"
    if os.path.exists(chaindata_dir):
        files_dir = sorted(os.listdir(chaindata_dir))
        for filename in files_dir:
            if filename.endswith('.json'):
                filepath = '%s/%s' % (chaindata_dir, filename)
                with open(filepath, 'r') as block_file:
                    block_info = json.load(block_file)
                    block_object = Block(block_info)
                    node_blocks.append(block_object)

    node_blocks = verification(node_blocks)
    return node_blocks
