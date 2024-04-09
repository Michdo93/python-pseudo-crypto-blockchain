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

# Beispielcode zur Verwendung des Smart Contracts
smart_contract = SmartContract()

# Erstellen einer Vereinbarung
party1 = "Alice"
party2 = "Bob"
terms = "Alice verkauft Bob ein digitales Kunstwerk für 50 Token."
smart_contract.create_agreement(party1, party2, terms)

# Akzeptieren der Vereinbarung
agreement_index = 0
accepting_party = "Bob"
result = smart_contract.accept_agreement(agreement_index, accepting_party)
print(result)

# Überprüfen des Status der Vereinbarung
print("Status der Vereinbarung:", smart_contract.agreements[agreement_index]['status'])
