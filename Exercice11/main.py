# Écrivez votre code ici !
class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("You can't withdraw that much")

    def display_balance(self):
        print(f'account_holder : {self.account_holder}')
        print(f'balance : {self.balance}')


bank_account = BankAccount('Michel', 500)
bank_account.deposit(200)
bank_account.withdraw(1200)
bank_account.withdraw(500)
bank_account.display_balance()
