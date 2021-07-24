import requests

method_list = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS', 'TRACE','TEST']

for method in method_list:
    req = requests.request(method, 'http://www.googl.com')
    print (method, req.status_code, req.reason)


if method == 'TRACE' and 'TRACE / HTTP/1.1' in req.text:
   print ('Cross Site Tracing(XST) is possible')
