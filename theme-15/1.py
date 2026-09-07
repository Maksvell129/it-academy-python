import requests


response = requests.get(
    "https://example.com/users/42"
)


print(response.status_code)
print(response.text)

