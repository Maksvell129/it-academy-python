class BankAccount:
    def __init__(self, balance: int):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @property
    def is_positive(self) -> bool:
        return self._balance > 0



account = BankAccount(-1000)

print(account.balance)
print(account.is_positive)
