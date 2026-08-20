from mixins import LogMixin, JsonMixin, FileUploadMixin


class User(LogMixin, JsonMixin):
    def __init__(self, name):
        self.name = name

    def create(self):
        self.log("Пользователь создан")


class Product(LogMixin, FileUploadMixin):
    def sell(self):
        print("товар был продан")
        self.log("Со склада был продан товар")


user = User("Alex")

user.log("Пользователь создан")

print(user.to_json())

#
# product = Product()
# product.sell()