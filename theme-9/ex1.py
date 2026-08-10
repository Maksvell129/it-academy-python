"""Напишите программу, которая запрашивает у пользователя два числа и выполняет деление. Программа должна:
использовать try/except;
корректно обрабатывать ввод нечисловых значений;
обрабатывать деление на ноль;
выводить результат через else;
в finally выводить: Операция завершена
"""

while True:
    try:
        num_one = int(input(f"Введите первое число: "))
        num_two = int(input(f"Введите второе число: "))
        result = num_one / num_two

    except ValueError:
        print("Нужно ввести число")

    except ZeroDivisionError:
        print("Делить на ноль нельзя")


    else:
        print(result)
        break

    finally:
        print("Операция завершена")