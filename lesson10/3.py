from collections.abc import Iterable

numbers = [1, 2, 3, 4, 5, 6]


squares = map(lambda x: str(x) * 3, numbers)
# [1, 4, 9, 16, 25, 36]
# print(list(squares))



evens = filter(lambda x: x % 2 == 0, numbers)
# [2, 4, 6]
# print(list(evens))

# print(list(map(lambda x: x**2, numbers)))
# print([x**2 for x in numbers])
#
#
# print(list(filter(lambda x: x%2==0, numbers)))
# print([x for x in numbers if x%2==0])

# from functools import reduce
# numbers = ["python", "c", "javascript", "go"]
# Вычисление произведения: ((1 * 2) * 3) * 4
# product = reduce(lambda x, y: x + y, numbers)  # 24
#
# print(product)


words = ["python", 123.1, "c", "333",[1,2],"javascript", "go", "c++", "c#", "1000", 1]
words_2 = ["python", "c", "javascript", "go"]
# Сортировка по длине слова, а не по алфавиту
# sorted_words = sorted(words, key=lambda word: word.isnumeric() if isinstance(word, str) else True if isinstance(word, int) else True if isinstance(word, float) else all(isinstance(el, int) for el in word) if isinstance(word, Iterable) else False)

# print(sorted_words)
# print("333".isnumeric())

