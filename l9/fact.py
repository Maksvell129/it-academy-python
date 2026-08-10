def factorial(n: int) -> int:
    # print(f"Запуск для числа {n}")
    if n <= 1:
        # print(f"Базовый случай {n}")
        return 1

    r = n * factorial(n - 1)
    # print(f"Возвращаемся с {n} с числом {r}")
    return r


print(factorial(5))


def factorial_iterative(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(factorial_iterative(5))
