class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def have_birthday(self):
        self.age += 1


user1 = User(name="Alex", age=20)
user2 = User("Maria", age=23)

# print(user1.name, user1.email)
# print(user2.name, user2.email)

print(user1.age)
user1.have_birthday()
print(user1.age)
print(user2.age)


