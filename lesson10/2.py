def apply_operation(x: int, y: int, operation_func) -> int:
    return operation_func(x, y)


def multiply(a: int, b: int) -> int:
    return a * b

# Передаем функцию multiply как обычный аргумент (БЕЗ скобок!)
result = apply_operation(10, 5, multiply)
print(result)  # 50
