import requests
import json

url = "http://127.0.0.1:8000/foods/receive_json/"
data = {'item': 'aAsasple'}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url, data=json.dumps(data), headers=headers)