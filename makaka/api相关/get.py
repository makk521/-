'''

'''
import requests
import json

URL = 'http://43.153.21.199:5000/'

res = requests.post(URL, json={"question": "写一个冒泡排序 python"})

print(json.loads(res.text)['answer'])