# def add(a, b):
#     print("a", a)
#     print("b", b)
#     return a+b
#
# numbers = [10, 20]
#
# print(add(numbers[0], numbers[1]))
#
# a, b = numbers
#
# print(add(a, b))
#
#
# print(add(*numbers))


# def info(name, age, city, **kwargs):
#     print("Основная информация:")
#     print(f"{name=}")
#     print(f"{age=}")
#     print(f"{city=}")
#     print(kwargs)
#
#     for key, value in kwargs.items():
#         print(f"Лишние ключ {key}: {value}")
#
# person = {
#     "name": "Иван",
#     "age": 25,
#     "city": "Barcelona",
#     "money": 12.3
# }
#
# info(**person)
# info(name="Иван", age=25, city="Barcelona")


def retrieve_by_city(city, **filters):
    query(city=city)

    if filters:
        query.filters(filters=filters)

    print(f"{user_id=}")
    print(f"{filters=}")
    pass


retrieve_by_city(city="minsk", street="Popedy", index=123123)



def first_func(a, **kwargs):
    print("Я делаю подготовку перед важной функцией")
    second_func(**kwargs)


def second_func(b ,total):
    print("Я делаю что-то супер важное")
    print("b: ", b)
    print("результат: ", total)


first_func(a=12, b=33, total=200)


