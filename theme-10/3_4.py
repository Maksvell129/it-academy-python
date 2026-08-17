import re


text = """
Телефоны:
+375291234567
+375441112233
+123
"""

phones = re.findall(
    r"\+\d{12}",
    text
)

print(phones)
