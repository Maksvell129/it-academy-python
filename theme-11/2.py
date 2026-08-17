from threading import activeCount


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Invalid amount for deposit")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid amount for withdraw")


account_1 = BankAccount(balance=1000)
print(account_1.balance)

account_1.deposit(200)
print(account_1.balance)

account_1.withdraw(300)
print(account_1.balance)