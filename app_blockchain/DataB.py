import json
from shutil import rmtree as del_dir
from app_blockchain import python_nodes

def chain():
    with open('DB/database.json', 'r') as f:
        blocks = json.load(f)
    return blocks


def length_chain():
    with open('DB/database.json', 'r') as f:
        blocks = json.load(f)
    length = len(blocks)
    return length


def one_block(index):
    with open('DB/database.json', 'r') as f:
        blocks = json.load(f)
    return blocks[index]


def update_chain():
    global blocks
    blocks = python_nodes.nodes()
    with open('DB/database.json', 'w') as f:
        json.dump(blocks, f, indent=4)

def delete_all():
    chaindata_dir = "app_blockchain/chaindata"
    del_dir(chaindata_dir)
