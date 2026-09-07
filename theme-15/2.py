import requests

response = requests.post(
    "https://example.com/users",
    json={
        "name": "Alex",
        "email": "alex@example.com",
    },
)

print(response.status_code)

response = requests.delete(
    "https://example.com/users/42"
)

print(response.status_code)


response = requests.get(
    "https://example.com/users"
)

if response.status_code == 200:
    print(response.json())

elif response.status_code == 404:
    print("User not found")

elif response.status_code >= 500:
    print("Server error")
