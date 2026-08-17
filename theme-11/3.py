

class User:
    def __init__(self, age):
        self.__age = age

    @property
    def age(self):
        return self.__age



user = User(25)
print(user.age)

