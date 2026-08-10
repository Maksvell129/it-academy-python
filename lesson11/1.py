def make_greeter(greeting: str):
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"

    return greet


say_hello = make_greeter("Привет")
say_bye = make_greeter("До свидания")


print(say_hello.__closure__)
print(say_bye.__closure__)
# print(say_hello("Алексей"))
# print(say_hello("Петя"))
# print(say_hello("Маша"))
# print(say_bye("Андрей"))
# print(say_bye("Саша"))
# print(say_bye("Ваня"))
