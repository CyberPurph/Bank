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

class BankApp:
    def __init__(self):
        self.bank = Bank()
        self.current_account = None

    def showMainMenu(self):
        while True:
            print("\nMAIN MENU")
            print("1. Select Account")
            print("2. Open Account")
            print("3. Exit")

            Selection = input("Welcome! Please select what you would like to do today: ")

            if Selection == "1":
                account_number = input("Enter the account number: ")
                self.current_account = self.bank.searchAccount(account_number)

                if self.current_account:
                    self.showAccountMenu()
                else:
                    print("We're sorry, you're account cannot be found.")

            elif Selection == "2":
                account_type = input("Please enter your account type (Savings/Chequing): ")
                account_number = input("Enter account number: ")
                initial_balance = float(input("Enter your initial balance: "))
                parameters = float(input("Enter your minimum balance or overdraft limit: "))

                new_account = self.bank.openAccount(account_type, account_number, initial_balance, parameters)

                if new_account:
                    print(f"Your account {account_number} has successfully opened!")
                    self.current_account = new_account
                    self.showAccountMenu()
                else:
                    print("Invalid account! Please choose either Savings or Chequing.")

            elif Selection == "3":
                print("Exiting now. Have a good day!")
                break

            else:
                print("Invalid selection! Please try again.")