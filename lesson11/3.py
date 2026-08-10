# ПЛОХОЙ ПРИМЕР: Пытаемся создать список из 3 разных функций-умножителей
multipliers = []
for i in range(3):
    multipliers.append(lambda x: x * i)
# Ожидание: 0, 2, 4
# Реальность: Все функции используют ПОСЛЕДНЕЕ значение i (i = 2)!
print(multipliers[0](3))  # 4 (2 * 2)
print(multipliers[1](2))  # 4 (2 * 2)
print(multipliers[2](2))  # 4 (2 * 2)

# РЕШЕНИЕ: Фиксация i через аргумент по умолчанию (Early Binding)
multipliers_correct = []
for i in range(3):
    multipliers_correct.append(lambda x, inside_i=i: x * inside_i)

print(multipliers_correct[0](2))  # 0 (2 * 0)
print(multipliers_correct[1](2))  # 2 (2 * 1)
print(multipliers_correct[2](2))  # 2 (2 * 1)
