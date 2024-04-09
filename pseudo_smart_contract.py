class SmartContract:
    def __init__(self):
        self.balances = {}

    def transfer(self, sender, recipient, amount):
        if sender not in self.balances:
            self.balances[sender] = 0
        if recipient not in self.balances:
            self.balances[recipient] = 0
        
        if self.balances[sender] < amount:
            return "Nicht genügend Guthaben"
        
        self.balances[sender] -= amount
        self.balances[recipient] += amount
        return "Transaktion erfolgreich"

# Beispielcode zur Verwendung des Smart Contracts
smart_contract = SmartContract()
smart_contract.balances["Adresse1"] = 100  # Beispiel-Guthaben für Adresse1
smart_contract.balances["Adresse2"] = 50   # Beispiel-Guthaben für Adresse2

# Transaktion ausführen
sender = "Adresse1"
recipient = "Adresse2"
amount = 30
result = smart_contract.transfer(sender, recipient, amount)
print(result)
print("Aktuelles Guthaben von Adresse1:", smart_contract.balances[sender])
print("Aktuelles Guthaben von Adresse2:", smart_contract.balances[recipient])
