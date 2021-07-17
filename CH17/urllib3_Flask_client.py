import urllib3

http = urllib3.PoolManager()
url = 'localhost:5000/'
headers = urllib3.make_headers(keep_alive=True, user_agent='Python program')
resp = http.request('GET', url, headers=headers)
print(resp.data.decode('utf-8'))

