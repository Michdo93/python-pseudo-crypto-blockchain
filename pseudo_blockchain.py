import hashlib
import json
import datetime

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Genesis-Block erstellen
        self.new_block(previous_hash="1", proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
            'transactions': self.pending_transactions
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Anpassen der Schwierigkeit des Proof-of-Work-Algorithmus


# Beispielcode zur Verwendung der Blockchain
blockchain = Blockchain()
blockchain.new_transaction("Alice", "Bob", 5)
blockchain.new_transaction("Bob", "Charlie", 3)
blockchain.new_block(12345)

# Mining eines neuen Blocks
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)
blockchain.new_transaction("Dan", "Eve", 2)
previous_hash = blockchain.hash(last_block)
block = blockchain.new_block(proof, previous_hash)

print("Blockchain:", blockchain.chain)
