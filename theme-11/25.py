

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)



cart = ShoppingCart()

cart.add("молоко")
cart.add("хлеб")
cart.add("морковка")
cart.add("арбуз")

print(len(cart))