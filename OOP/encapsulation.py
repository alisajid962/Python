class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # private variable

    def deposit(self, amount):
        self._balance += amount

    def show_balance(self):
        print("Balance:", self._balance)
    def hack(self):
        self._balance=0
        print("Hacke Balance : ",self._balance)


acc = BankAccount(1000)
acc.deposit(500)
acc.show_balance()
acc.hack()   # ✅ Output: 1500

print(acc._balance)  # ❌ AttributeError
