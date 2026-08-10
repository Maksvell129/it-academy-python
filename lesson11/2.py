def make_counter():
    count = 0
    a = "2dasdsadsa2"
    def counter():
        nonlocal count
        nonlocal a
        count += 1
        return count
    return counter


c = make_counter()
print(c())  # 1
print(c())  # 2

# Посмотрим во внутренности функции c:
print(c.__closure__[0].cell_contents)  # Выведет текущее значение count: 2
print(c.__closure__[1].cell_contents)  # Выведет текущее значение count: 2
