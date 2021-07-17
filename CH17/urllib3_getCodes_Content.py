import urllib3

http = urllib3.PoolManager()
url = 'www.google.com'
resp = http.request('GET', url)
print(resp.status)
print(resp.data.decode('utf-8'))

