import requests


response = requests.get(
    "https://example.com/users",
    params={
        "name": "Alex",
        "age": 30,
    },
)

user_id = 42

response = requests.get(
    f"https://example.com/users/{user_id}"
)
