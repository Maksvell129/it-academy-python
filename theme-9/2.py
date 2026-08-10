try:
    number = int(input("Введите число: "))
    result = 100 / number

except ValueError:
    print("Нужно ввести число")

except ZeroDivisionError:
    print("Нельзя делить на ноль")

else:
    print("Результат:", result)

finally:
    print("Работа программы завершена")
