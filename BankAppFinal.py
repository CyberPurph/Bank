class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, minimum_balance=5000):
        super().__init__(account_number, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        pass
             