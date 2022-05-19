import datetime as date
import hashlib, json, os

class Block(object):
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        if not hasattr(self, 'nonce'):
            self.nonce = 'None'

        if not hasattr(self, 'hash'):
            self.hash = self.create_self_hash()

    def header_string(self):
        return str(self.index) + self.prev_hash + self.data + str(self.timestamp) + str(self.nonce)

    def create_self_hash(self):
        sha = hashlib.sha256()
        sha.update(self.header_string().encode('utf-8'))
        return sha.hexdigest()

    def self_save(self):
        chaindata_dir = r"app_blockchain/chaindata"

        index_string = str(self.index).zfill(6)
        filename = '%s/%s.json' % (chaindata_dir, index_string)
        with open(filename, 'w') as block_file:
            json.dump(self.__dict__(), block_file, indent=4)

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['timestamp'] = str(self.timestamp)
        info['prev_hash'] = str(self.prev_hash)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        info['nonce'] = str(self.nonce)
        return info

    def __str__(self):
        return "Block<prev_hash: %s,hash: %s>" % (self.prev_hash, self.hash)


def verification(chain):
    if len(chain) > 1:
        for i in range(len(chain) - 1):
            if chain[i].create_self_hash() != chain[i + 1].prev_hash:
                return chain[:i + 1]
    return chain


def create_first_block():
    block_data = {}
    block_data['index'] = 0
    block_data['timestamp'] = date.datetime.now()
    block_data['data'] = 'First block data'
    block_data['prev_hash'] = ''
    block_data['nonce'] = 0  # starting it at 0
    return Block(block_data)


def _block():
    chaindata_dir = r"app_blockchain/chaindata"

    if not os.path.exists(chaindata_dir):
        os.mkdir(chaindata_dir)
    if os.listdir(chaindata_dir) == []:
        first_block = create_first_block()
        first_block.self_save()
