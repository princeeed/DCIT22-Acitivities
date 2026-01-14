class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display_balance(self):
        print(f"Your balance is: {self.balance}")

my_bank_account = BankAccount(1000)
my_bank_account.deposit(2000)
my_bank_account.display_balance()