class BankError(Exception):
    pass


class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount

        super().__init__(f"Недостаточно средств: баланс {balance}, "  f"запрошено {amount}")



class InvalidAmountError(BankError):
    pass
