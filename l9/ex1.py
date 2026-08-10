# Напишите функцию analyze_scores(scores: list[int | float]), которая принимает список числовых оценок.
# Функция должна находить и возвращать 3 значения через запятую (return):
#     Минимальную оценку.
#     Максимальную оценку.
#     Среднее арифметическое (округленное до 2 знаков после запятой).

from statistics import mean

def analyze_scores(scores: list[int | float]) -> (int | float, int | float, int | float):
    summ = scores[0]
    min_score, max_score = scores[0], scores[0]

    for i in range(1, len(scores)):
        if scores[i] < min_score:
            min_score = scores[i]

        if scores[i] > max_score:
            max_score = scores[i]

        summ += scores[i]


    return min_score, max_score, summ / len(scores)


scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(scores.__len__())
print(analyze_scores(scores))

