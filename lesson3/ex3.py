# Задан исходный список почтовых адресов сотрудников, содержащий дубликаты из-за
# системного сбоя: emails = ["original@ya.ru", "b@ya.ru", "original@ya.ru", "c@ya.ru", "b@ya.ru"].
# Напишите код, который автоматически оставляет в структуре только уникальные адреса,
# превращает результат обратно в список и выводит количество оставшихся элементов.

emails = ["original@ya.ru", "b@ya.ru", "original@ya.ru", "c@ya.ru", "b@ya.ru"]
emails = list(set(emails))

print(len(emails))
print(emails[0])

print()
