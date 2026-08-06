# Создайте словарь patient с ключами name и age. Запросите у пользователя через консоль
# изменение возраста на текущий год и добавьте новый ключ allergies, значением которого
# должен стать список из двух медицинских препаратов.

patient = {
    "name": "Alex",
    "age": 20,
}

# age_diff = int(input("Input difference: "))
#
# patient["age"] = patient["age"] + age_diff

allergies_str = input("Input allergies(separated by space): ")

allergies = allergies_str.split(" ")

print(allergies)

print(f"Allergies: {" | ".join(allergies)}")

marks = [3, 4, 6]

print(f"Marks: {" | ".join(marks)}")
