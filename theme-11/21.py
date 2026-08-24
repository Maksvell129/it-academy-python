class User:
    def save(self):
        print("Сохраняем пользователя")


class Product:
    def save(self):
        print("Сохраняем товар")


class Order:
    def save(self):
        print("Сохраняем заказ")


def save_object(obj):
    obj.save()


save_object(User())
save_object(Product())
save_object(Order())


objects = [User(), Product(), Order()]

for obj in objects:
    obj.save()
