import requests
from config import API_KEY


def gpt(text):
    url = "https://api.air.fail/public/text/chatgpt"
    data = {"model": "gpt-4", "content": text, "info": {"temperature": 0.5}}
    headers = {"Authorization": API_KEY}
    response = requests.post(url, json=data, headers=headers)
    return response.json()[0]["content"]

def gpt(text):
    url = "https://api.air.fail/public/text/chatgpt"
    data = {"model": "gpt-4", "content": text, "info": {"temperature": 0.5}}
    headers = {"Authorization": API_KEY}
    response = requests.post(url, json=data, headers=headers)
    return response.json()[0]["content"]
