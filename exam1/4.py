from typing import Callable


def process_numbers(numbers: list[int], operation: Callable) -> list[int]:
    return [operation(number) for number in numbers]


def square(number: int) -> int:
    return number ** 2

def cube(number: int) -> int:
    return number ** 3


def module(number: int) -> int:
    if number >= 0:
        return number
    else:
        return number * (-1)


numbers = [1, 2, 3, -4]
result = process_numbers(numbers, lambda x: x ** 2)
print(result)
result = process_numbers(numbers, lambda x: x ** 3)
print(result)
result = process_numbers(numbers, lambda x: abs(x))
print(result)
result = process_numbers(numbers, lambda x: x if x >= 0 else x * (-1))
print(result)
result = process_numbers(numbers, square)
print(result)
result = process_numbers(numbers, cube)
print(result)
result = process_numbers(numbers, module)
print(result)
