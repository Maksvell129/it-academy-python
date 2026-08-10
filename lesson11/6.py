from functools import wraps


def repeat(num_times: int):

    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            for _ in range(num_times):
                result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator_repeat



@repeat(num_times=2)
def greet(name: str):
    """Приветствует пользователя."""
    print(f"Привет, {name}!")

# @repeat(num_times=3)
# def bye(name: str):
#     """Приветствует пользователя."""
#     print(f"Пока, {name}!")

#
# decorator_repeat = repeat(num_times=5)
# print(decorator_repeat)
# decorated_greet = decorator_repeat(greet)
# print(decorated_greet)
greet("Алекс")
# bye("Алекс")
