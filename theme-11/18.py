from dataclasses import dataclass, field

@dataclass
class User:
    name: str
    age: int
    email: str
    roles: list[str] = field(default_factory=list)
    dict_attr: dict[str, int] = field(default_factory=dict)

user = User(name="Alex", age=25, email="alex@example.com")

print(user.email)
print(user.age)
print(user.name)
print(user.roles)

user.roles.append("admin")

print(user.roles)

user2 = User(name="Maria", age=25,email="maria@example.com")

print(user2.roles)


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0

    def total_cost(self):
        return self.price * self.quantity


product = Product(name="Milk", price=5.00, quantity=5)

print(product.name)
print(product.price)
print(product.quantity)
print("Total:", product.total_cost())


product = Product(name="Bread", price=4.00)

print(product.name)
print(product.price)
print(product.quantity)