class BankAccount:
    def __init__(self, account_name, starting_balance):
        self.account_name = account_name
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.balance = format(self.balance, ".2f")
        else:
            print("Insufficient funds. T-T")

    def get_balance(self):
        return f"{self.account_name} has a balance of ${self.balance}"

account_instance = BankAccount(account_name="Wally", starting_balance=1000)

# Deposit and withdraw hardcoded
account_instance.deposit(500.50)
account_instance.withdraw(200)

balance_result = account_instance.get_balance()
print(balance_result)
