import requests
# from config import API_KEY
#
#
# url = "https://api.air.fail/public/text/chatgpt"
# data = {"model": "gpt-4", "content": text, "info": {"temperature": 0.5}}
# headers = {"Authorization": API_KEY}
# response = requests.post(url, json=data, headers=headers)
# return response.json()[0]["content"]
# url = "https://api.air.fail/public/image/stablediffusion"
# headers = {"Authorization": "sk-lyCjtL5n3wUrXav9Ra1LiqcP2uIYG"}
# data = {"content": "Нарисуй Егора в машине с куклой"}
# response = requests.post(url, headers=headers, json=data)
# print(response.json())

import shelve
pandora = shelve.open("pandora")
p = pandora["5159118953"]
assert p