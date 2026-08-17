import re

result = re.search(
    r"(\d{2})-(\d{2})-(\d{4})",
    "Дата: 25-12-2026"
)

print(result.group(0))
print(result.group(1))
print(result.group(2))
print(result.group(3))
