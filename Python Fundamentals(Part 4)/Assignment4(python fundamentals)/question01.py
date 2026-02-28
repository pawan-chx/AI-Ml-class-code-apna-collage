class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def check_balance(self):
        print(f"Total balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, available balance = {self.balance}")
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, available balance = {self.balance}")

    def get_info(self):
        print(
            f"Account holder: {self.owner_name}, "
            f"Account no: {self.account_number}, "
            f"Balance: {self.balance}"
        )


a1 = BankAccount(5665362, "pawan", 67200)       

a1.check_balance()
a1.withdraw(100)
a1.check_balance()
a1.get_info()
a1.deposit(300)
a1.get_info()