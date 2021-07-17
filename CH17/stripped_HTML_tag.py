import httplib2
import re
 
http = httplib2.Http()
content = http.request("http://www.something.com")[1]
 
stripped = re.sub('<[^<]+?>', '', content.decode())
print(stripped)

