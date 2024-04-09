import hashlib
import json
import datetime

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.smart_contract = SmartContract()  # Verbindung zur Smart-Contract-Klasse herstellen

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


class SmartContract:
    def __init__(self):
        self.agreements = []

    def create_agreement(self, party1, party2, terms):
        agreement = {
            'party1': party1,
            'party2': party2,
            'terms': terms,
            'status': 'pending'  # 'pending', 'accepted', 'rejected'
        }
        self.agreements.append(agreement)
        return "Vereinbarung erstellt"

    def accept_agreement(self, agreement_index, accepting_party):
        if agreement_index < 0 or agreement_index >= len(self.agreements):
            return "Ungültiger Vereinbarungsindex"
        
        agreement = self.agreements[agreement_index]
        if accepting_party == agreement['party1'] or accepting_party == agreement['party2']:
            agreement['status'] = 'accepted'
            return "Vereinbarung akzeptiert"
        else:
            return "Die Partei ist nicht an der Vereinbarung beteiligt"


# Beispielcode zur Verwendung der Blockchain und des Smart Contracts
blockchain = Blockchain()

# Erstellen einer Vereinbarungstransaktion in der Blockchain
sender = "Alice"
recipient = "Bob"
amount = 0  # keine Token-Übertragung erforderlich
agreement_terms = "Alice verkauft Bob ein digitales Kunstwerk für 50 Token."
blockchain.new_transaction(sender, recipient, amount)

# Mining eines neuen Blocks
last_block = blockchain.last_block
last_proof = last_block['proof']
proof = blockchain.proof_of_work(last_proof)
blockchain.new_block(proof)

# Aufrufen des Smart Contracts, um die Vereinbarung zu erstellen
smart_contract = blockchain.smart_contract
agreement_result = smart_contract.create_agreement(sender, recipient, agreement_terms)
print(agreement_result)

# Überprüfen des Status der Vereinbarung im Smart Contract
print("Status der Vereinbarung:", smart_contract.agreements[-1]['status'])

# Überprüfen der gesamten Blockchain
print("Blockchain:", blockchain.chain)
