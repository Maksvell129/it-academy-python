try:
    age = int(input("Введите возраст: "))

    if age < 0:
        print("Возраст не может быть отрицательным")

except ValueError:
    print("Возраст должен быть числом")
