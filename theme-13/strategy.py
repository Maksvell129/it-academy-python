class StandardDelivery:
    def calculate(self, price):
        return price


class ExpressDelivery:
    def calculate(self, price):
        return price * 1.3


class Order:
    def __init__(self, delivery_strategy):
        self.delivery_strategy = delivery_strategy

    def delivery_cost(self, price):
        return self.delivery_strategy.calculate(price)


order1 = Order(delivery_strategy=StandardDelivery())

print(order1.delivery_cost(100))

order2 = Order(delivery_strategy=ExpressDelivery())

print(order2.delivery_cost(100))
