# Напишите функцию make_rate_limiter(max_requests: int).
# Внутри неё создайте вложенную функцию request(), которая при каждом вызове:
# Уменьшает доступное количество запросов на 1.
# Если запросы ещё остались (количество > 0), возвращает строку: «Запрос выполнен. Ослалось запросов: X».
# Если лимит исчерпан (< 0), возвращает строку: «Ошибка: Лимит запросов превышен!».
# Внешняя функция должна возвращать внутреннюю функцию request.
# Подсказка: Не забудьте использовать nonlocal, чтобы изменять внешнюю переменную max_requests.


def make_rate_limiter(max_requests: int):

    def request():
        nonlocal max_requests
        max_requests -= 1

        if max_requests >= 0:
            return f"Запрос выполнен. Ослалось запросов: {max_requests}"
        else:
            return "Ошибка: Лимит запросов превышен!"


    return request


limiter = make_rate_limiter(max_requests=3)
print(limiter())
print(limiter())
print(limiter())
print(limiter())
