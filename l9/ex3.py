
# Напишите рекурсивную функцию recursive_sum(data: list) -> int, которая посчитает сумму всех чисел в такой «матрешке».
#
# Подсказка по логике:
#     Проходите по элементам списка циклом for item in data.
#     Если isinstance(item, list) равен True (элемент сам является списком) — вызывайте recursive_sum(item) для него.
#     В противном случае — просто прибавляйте число к общей сумме.
#
# (Ожидаемый результат для nested_data: 28)

def recursive_sum(data: list) -> int:
    summ = 0

    for item in data:
        if isinstance(item, list):
            summ += recursive_sum(item)
        else:
            summ += item

    return summ


nested_data = [1, [2, 3], [4, [5, 6]], 7]

print(recursive_sum(nested_data))
