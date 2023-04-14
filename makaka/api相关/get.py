'''

'''
import requests
import json

URL = 'http://43.153.21.199:5000/'

res = requests.post(URL, json={"question": "沙尘暴是怎么形成的"})

print(json.loads(res.text)['answer'])