# Базовый синтаксис без сахара:
def my_decorator(func):
    def wrapper():
        print(f"INFO run {func.__name__}")

        try:
            func()
        except Exception as e:
            print(f"ERROR {func.__name__}: {e}")
        finally:
            print(f"INFO end {func.__name__}")

    return wrapper

def say_hi():
    print("Привет!")
    raise Exception("СУПЕР СМЕРТЕЛЬНАЯ ОШИБКА")

# Ручное обертывание:
say_hi = my_decorator(say_hi)
say_hi()
