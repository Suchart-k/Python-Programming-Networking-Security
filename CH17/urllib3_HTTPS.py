import urllib3
import certifi

url = 'https://www.python.org/'
http = urllib3.PoolManager(ca_certs=certifi.where())
resp = http.request('GET', url)
print(resp.status)
print(resp.data.decode('utf-8'))

