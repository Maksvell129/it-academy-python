# Напишите декоратор retry(func).
# Внутри создайте функцию-обертку wrapper(*args, **kwargs).
# Обертка должна пытаться выполнить целевую функцию func.
# Если функция выполнилась успешно — вернуть её результат.
# Если при выполнении возникла ошибка Exception, перехватить её (try-except),
# вывести в консоль сообщение: «Произошла ошибка [название ошибки]. Пробуем еще раз...» и сделать вторую (повторную) попытку вызова.
# Не забудьте обернуть wrapper с помощью @functools.wraps(func).


from functools import wraps
from random import randint

def retry(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"«Произошла ошибка [{e}]. Пробуем еще раз...» и сделать вторую попытку вызова.")
            return func(*args, **kwargs)

    return wrapper

@retry(num=5)
def random_bool():
    result = randint(0, 1)

    if result:
        return "Успех"
    else:
        raise ValueError("не повезло")



print(random_bool())
