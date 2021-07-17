import httplib2
 
http = httplib2.Http()
content = http.request("http://www.something.com")[1]
 
print(content.decode())

