import json

user = {
    "name": "Alex",
    "age": 25,
    "skills": ["Python", "SQL"]
}

with open(    "user2.json",    "w",    encoding="utf-8") as file:
    json.dump(user, file, indent=4)
