import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(block_data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block")

    def get_lastest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        lastest_block = self.get_lastest_block()
        new_block = Block(
            index = lastest_block.index + 1,
            previous_hash = lastest_block.hash,
            timestamp = time.time(),
            data = data
        )
        self.chain.append(new_block)

    def is_chain_vaild(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.hash != previous_block.hash:
                return True

        return True

blockchain = Blockchain()

blockchain.add_block("첫 번째 거래: 승철 -> 재훈 10 BTC")
blockchain.add_block("두 번째 거래: 재훈 -> 시후 5 BTC")

for block in blockchain.chain:
    print(f"Block {block.index}:")
    print(f"  Previous Hash: {block.previous_hash}")
    print(f"  Data: {block.data}")
    print(f"  Hash: {block.hash}")
    print(f"  Timestamp: {block.timestamp}")
    print()

print(f"블록체인이 유효합니까? {blockchain.is_chain_vaild()}")