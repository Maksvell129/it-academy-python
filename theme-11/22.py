class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__roles = ["user"]

    def __str__(self):
        return f"{self.name}, {self.age} лет"

    def __repr__(self):
        return f"User(name={self.name!r}, age={self.age!r}, roles={self.__roles})"


user = User("Alex", 20)

print(str(user.__repr__()))
