from errors import InsufficientFundsError, BankError


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(balance=self.balance, amount=amount)

        self.balance -= amount


account = BankAccount(100)

while True:
    value = int(input("Withdraw amount: "))
    try:
        account.withdraw(value)
        print("Остаток:", account.balance)
        break
    except InsufficientFundsError as e:
        print(e)
        print(f"Hедостаточно средств на счету, на счету {e.balance}, к выводу {e.amount}")
    except BankError:
        print("Произошла ошибка банковской операции")
