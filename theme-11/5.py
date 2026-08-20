class User:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Возраст не может быть отрицательным")

        self._age = value



user = User(25)
print(user.age)
user.age = 30
print(user.age)
