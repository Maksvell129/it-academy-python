# Создайте функцию:
# validate_age(age)
#
# Требования:
#
# если возраст меньше 0 — вызвать ValueError;
# если возраст больше 150 — вызвать ValueError;
# если значение корректное — функция ничего не возвращает.


def validate_age(age: int) -> None:
    min_age, max_age = 0, 150

    if age < min_age:
        raise ValueError(f"Возраст не может быть меньше {min_age}")

    if age > max_age:
        raise ValueError(f"Возраст не может быть больше {max_age}")


