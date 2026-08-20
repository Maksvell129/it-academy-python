class User:
    COUNT = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        User.COUNT += 1

    @classmethod
    def show_count(cls):
        print(cls.COUNT)

    @classmethod
    def from_string(cls, data):
        name, age = data.split(";")
        return cls(name, int(age))


class Admin(User):
    pass


alena = User("Alena", 23)

kirill = User.from_string("Kirill;29")

print(alena.name, alena.age)
print(kirill.name, kirill.age)

User.show_count()

admin = Admin.from_string("Alex;30")

print(admin)