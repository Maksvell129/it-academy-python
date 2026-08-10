# data = [1, 2, 3, 4, 5, 6]

# ИМПЕРАТИВНЫЙ СТИЛЬ: Пошагово управляем индексами и состоянием
# result_imp = []
# for x in data:
#     if x % 2 == 0:
#         result_imp.append(x)

# ДЕКЛАРАТИВНЫЙ СТИЛЬ: Описываем суть трансформации
#          [выражение for элемент in последовательность if условие]
# result_decl = [x for x in data if x % 2 == 0]


# print(result_imp)
# print(result_decl)


#
# print(even_squares)


# labels = [x if x % 2 == 0 else -1 for x in range(1, 6)]
# Вывод: [-1, 2, -1, 4, -1]
# print(labels)


# matrix = [
#     [1, 2],
#     [3, 4]
# ]
# Вытягиваем вложенный список в плоский [1, 2, 3, 4]
# flat = [num for row in matrix for num in row]
#
# print(flat)


# unique_lengths = {len(word) for word in ["python", "java", "python", "go"]}
# print(unique_lengths)

# users = ["alex", "maria", "john"]
# user_ids = {i + 1: user  for i, user in enumerate(users) }
#
# print(user_ids)

# sum_large = (x ** 2 for x in range(1_00))
#
# for i in sum_large:
#     print(i)

# print(sum_large.__next__())
# print(sum_large.__next__())
# print(sum_large.__next__())
# print(sum_large.__next__())
# print(sum_large.__next__())

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
even_squares_2 = []

for i in range(1, 11):
    if i % 2 == 0:
        even_squares_2.append(i ** 2)

print(even_squares)
print(even_squares_2)

