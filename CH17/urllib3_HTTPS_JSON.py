import urllib3
import certifi
import json

http = urllib3.PoolManager(ca_certs=certifi.where())
payload = {'name': 'Suchart K'}
encoded_data = json.dumps(payload).encode('utf-8')

resp = http.request(
     'POST',
     'https://httpbin.org/post',
     body=encoded_data,
     headers={'Content-Type': 'application/json'})

data = json.loads(resp.data.decode('utf-8'))['json']
print(data)

