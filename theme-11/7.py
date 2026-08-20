from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def move(self):
        print("Автомобиль едет по дороге")


class Ship(Transport):
    def move(self):
        print("Корабль плывет")


class Plane(Transport):
    def move(self):
        print("Самолет летит")

# transport = Transport(brand="Lada", model="Kalina")

# print(transport.brand)
# print(transport.model)
# transport.move()

car = Car(brand="Tesla", model="X", doors=5)

# print(car.brand)
# print(car.model)
# print(car.doors)
# car.move()

plane = Plane(brand="Boeng", model="1")

ship = Ship(brand="Ship", model="1")


transports = [car, plane, ship]
for transport in transports:
    transport.move()
