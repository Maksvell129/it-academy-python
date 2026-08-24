class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __lt__(self, other: BankAccount) -> bool:
        return self.balance < other.balance

    def __gt__(self, other: BankAccount)-> bool:
        return self.balance > other.balance

    def __ge__(self, other: BankAccount)-> bool:
        return self.balance >= other.balance

    def __le__(self, other: BankAccount)-> bool:
        return self.balance <= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

b1 = BankAccount(500)
b2 = BankAccount(200)


print(1 + 100)