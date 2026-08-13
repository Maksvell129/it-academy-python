import csv

users = [
    {'name': 'Alex', 'age': '25', 'city': 'Minsk'},
    {'name': 'Maria', 'age': '31', 'city': 'Vilnius'},
    {'name': 'John', 'age': '28', 'city': 'Moscow', "country": "Belarus"}
]

with open(    "users.csv",    "w",    encoding="utf-8",    newline="") as file:
    fieldnames = ["name", "age", "city", "country"]

    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )

    writer.writeheader()
    writer.writerows(users)
