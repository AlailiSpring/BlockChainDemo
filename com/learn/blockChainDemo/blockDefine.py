import hashlib as hasher
'''定义区块链中的块'''
class Block:
    def __init__(self,index,timestamp,data,previous_hash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previous_hash=previous_hash
        self.hash=self.hash_block()

    def hash_block(self):
        sha=hasher.sha256()
        sha.update(str(self.index).encode("utf8")
                   +str(self.timestamp).encode("utf8")
                   +str(self.data).encode("utf8")
                   +str(self.previous_hash).encode("utf8")
                   )

        return sha.hexdigest()


