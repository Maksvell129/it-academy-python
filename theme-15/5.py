import requests

response = requests.get(
    "https://dog.ceo/api/breeds/image/random"
)

print(response.status_code)

response_json = response.json()


print(response_json["message"])
