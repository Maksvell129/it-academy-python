import re

text = "Мой номер: 123456"

result = re.sub(r"\d", "*", text)

print(result)
