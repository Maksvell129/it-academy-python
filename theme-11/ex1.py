# Создайте класс Money, который представляет денежную сумму. Объект должен хранить:
# amount — сумма;
# currency — валюта.
# Реализуйте:
# __str__() — красивое отображение объекта.
# __repr__() — техническое представление объекта.
# __add__() — сложение двух объектов Money.
# __sub__() — вычитание двух объектов Money.
# __eq__() — сравнение двух объектов.
#
# Правила:
# Складывать и вычитать можно только суммы в одной валюте. А попытка Money(100, "EUR") + Money(50, "USD") должна приводить к исключению.
#
# Создайте собственное исключение: DifferentCurrencyError


class DifferentCurrencyError(Exception):
    pass



class InsufficientFundsError(Exception):
    pass



class Money:
    def __init__(self, amount: int, currency: str):
        self.__amount = amount
        self.__currency = currency

    def __str__(self):
        return f'{self.__amount} {self.__currency}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__amount},{self.__currency})'

    @staticmethod
    def validate_currency_consistency(currency1: str, currency2: str) -> None:
        if currency1 != currency2:
            raise DifferentCurrencyError(f"Валюты не совпадают: {currency1} и {currency2}")

    def __add__(self, other):
        self.validate_currency_consistency(self.__currency, other.__currency)

        return Money(self.__amount + other.__amount, self.__currency)

    def __sub__(self, other):
        self.validate_currency_consistency(self.__currency, other.__currency)

        if other.__amount > self.__amount:
            raise InsufficientFundsError(f"Недостаточно средств: {other.__amount} и {self.__amount}")

        return Money(self.__amount - other.__amount, self.__currency)

    def __eq__(self, other):
        return self.__amount == other.__amount and self.__currency == other.__currency


money1 = Money(10, 'USD')
money2 = Money(20, 'USD')

print(money1 - money2)
