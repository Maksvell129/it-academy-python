import time
from functools import wraps

def timer_decorator(func):
    """Декоратор для замера времени выполнения функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        # Вызываем оригинальную функцию и сохраняем её результат
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"[TIMER] Функция '{func.__name__}' выполнилась за {end_time - start_time:.5f} сек.")
        return result  # Обязательно возвращаем результат оригинальной функции!

    return wrapper


@timer_decorator
def heavy_computation(n: int, a: int, b: int) -> int:
    """Some important docs
    """
    return sum(i ** 2 for i in range(n))


@timer_decorator
def heavy_computation2(n: int) -> int:
    return sum(i ** 3 for i in range(n))


print(heavy_computation(10000, 1, 2))
# print(heavy_computation(10000))
# print(heavy_computation.__name__)
# print(heavy_computation.__doc__)
print(heavy_computation2(10000))
# print(heavy_computation2.__name__)



