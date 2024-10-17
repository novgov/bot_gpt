# import requests
# from config import API_KEY
#
#
# url = "https://api.air.fail/public/text/chatgpt"
# data = {"model": "gpt-4", "content": text, "info": {"temperature": 0.5}}
# headers = {"Authorization": API_KEY}
# response = requests.post(url, json=data, headers=headers)
# return response.json()[0]["content"]
from enum import Enum

class Test(Enum):
    a = 1
print(dir(Test.a))