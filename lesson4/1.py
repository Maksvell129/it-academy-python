# Создайте список original = [10, 20].
# Напишите код, который создает переменную b, связанную с тем же объектом, и переменную c, являющуюся независимой копией списка original.
# Измените список b, добавив элемент 30. Выведите на экран все три списка, а также результаты проверок original is b и original is c.

# original = [10, 20]
#
# b = original
# c = original.copy()
#
# b.append(30)
#
# print(original)
# print(b)
# print(c)
#
# print(original is b)
# print(original is c)

from copy import copy, deepcopy

original = [10, 20, [1, 2, 3, 4]]

shallow_copy = copy(original)
deep_copy = deepcopy(original)

print(shallow_copy, shallow_copy is original)
print(deep_copy, deep_copy is original)

print("=" * 20)

original.append(30)
original[0] = 90

print(original)
print(shallow_copy, shallow_copy is original)
print(deep_copy, deep_copy is original)

print("=" * 20)

original[2].append(5)
print(original)
print(shallow_copy, shallow_copy is original)
print(deep_copy, deep_copy is original)

print("=" * 20)

print(original[2] is shallow_copy[2])
print(original[2] is deep_copy[2])