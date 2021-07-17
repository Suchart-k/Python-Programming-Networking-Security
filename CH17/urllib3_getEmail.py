import urllib3
import re

url = input("Enter url: ")
http = urllib3.PoolManager()
#get content page from response
resp = http.request('GET', url)
#regular expression
pattern = re.compile("[-a-zA-Z0-9._]+@[-a-zA-Z0-9_]+.[a-zA-Z0-9_.]+")
#convert UTF-8 to text 
content = resp.data.decode('utf-8')
#get mails from regular expression
mails = re.findall(pattern, content)
print(mails)

