import re


pattern = r"\+\d{12}"

text = input("Введите текст: ")

print(re.findall(pattern, text))
