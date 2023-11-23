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

class ChequingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=5000):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        pass

class Bank:
    def __init__(self):
        self.accounts = [
            ChequingAccount("C1.1", 1000),
            ChequingAccount("C1.2", 2000),
            ChequingAccount("C1.3", 3000),
            SavingsAccount("S1.1", 5000),
            SavingsAccount("S1.2", 6000),
            SavingsAccount("S1.3", 7000),
        ]

    def SearchAccount(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def openAccount(self, account_type, account_number, initial_balance, parameters):
        if account_type == "Savings":
            new_account = SavingsAccount(account_number, initial_balance, parameters)
        elif account_type == "Chequing":
            new_account = ChequingAccount(account_number, initial_balance, parameters)
        else:
            return None
    
        self.accounts.append(new_account)
        return new_account
