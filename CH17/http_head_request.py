import httplib2
 
http = httplib2.Http() 
resp = http.request("http://www.something.com", "HEAD")[0]
print("Server: " + resp['server'])
print("Last modified: " + resp['last-modified'])
print("Content type: " + resp['content-type'])



