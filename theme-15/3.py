import requests


headers = {
    "Accept": "application/json",
    "Authorization": "Bearer token",
}
response = requests.get(
    "https://example.com/users",
    headers=headers,
)
print(response.headers)
print(
    response.headers["Content-Type"]
)
print(response.text)