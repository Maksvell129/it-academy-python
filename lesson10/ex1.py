# raw_prices = ["100$ ", " 250$", "FREE", " -50$", "500$", "0$"]
# С помощью List Comprehension в одну строчку очистите список:
#     Удалите пробелы по краям и символ $.
#     Исключите бесплатные ("FREE") и отрицательные стоимости.
#     Преобразуйте оставшиеся корректные значения в тип int.


raw_prices = ["100$ ", " 250$", "FREE", " -50$", "500$", "0$"]


result = [
    int(price) for price in [p.strip().replace("$", "") for p in raw_prices]
    if price != "FREE" and int(price) > 0
]


# print(result)



