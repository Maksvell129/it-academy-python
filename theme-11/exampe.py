# Создадим класс товара.
# У товара есть:
# название;
# цена;
# количество.
# Цена не должна быть отрицательной.
# Поэтому мы хотим контролировать изменение price.



class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self._name = name
        self._price = price
        self._quantity = quantity


    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value:
            raise ValueError("Name cannot be empty")

        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price must be positive")

        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be 0")

        self._quantity = value


    def make_purchase(self, wanted_quantity: int) -> float:
        """:return float: purchase price"""
        if wanted_quantity < 1:
            raise ValueError("Quantity cannot less than 1")

        if wanted_quantity > self._quantity:
            raise ValueError("You cannot by more product than we have")

        self._quantity -= wanted_quantity

        return self._price * wanted_quantity


    def __str__(self):
        return f"Name: {self._name}, Price: {self._price}, Quantity: {self._quantity}"


milk = Product("Milk", 3.00, 10)

print(milk)

print(milk.make_purchase(5))

print(milk)