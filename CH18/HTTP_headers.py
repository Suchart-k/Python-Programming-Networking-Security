import requests

request = requests.get('http://www.google.com')

header_list = ['Server', 'Date', 'Via', 'X-Powered-By', 'X-Country-Code', 'Connection', 'Content-Length']

for header in header_list:
   try:
      result = request.header_list[header]
      print ('%s: %s' % (header, result))
   except Exception as err:
      print ('%s: No Details Found' % header)

