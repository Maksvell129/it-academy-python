while True:
    try:
        age = int(input("Введите возраст: "))

        if age < 0 or age > 150:
            raise ValueError("Возраст должен быть от 0 до 150")

        break

    except ValueError as error:
        print("Ошибка:", error)

print("Возраст:", age)
