import urllib3
import certifi

http = urllib3.PoolManager(ca_certs=certifi.where())
url = 'https://httpbin.org/post'
req = http.request('POST', url, fields={'name': 'Suchart K'})
print(req.data.decode('utf-8'))

