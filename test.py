import requests
url = "https://api.air.fail/public/image"
headers = {"Authorization": "sk-lyCjtL5n3wUrXav9Ra1LiqcP2uIYG"}
response = requests.get(url, headers=headers)
print(response.json())
