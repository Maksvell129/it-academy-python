from faker import Faker

faker = Faker()


class Human:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def __add__(self, other):
        n = input("Введите имя ребенка:")
        return Human(n, other.last_name, 0)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.age}"




mama = Human("Maria", "Petrovna", 31)
papa = Human("Alex", "Ivanov", 32)

# print(mama + papa)
