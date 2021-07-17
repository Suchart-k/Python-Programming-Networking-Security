import httplib2
 
http = httplib2.Http()
resp = http.request("http://www.something.com")[0]
print(resp.status)
 
resp = http.request("http://www.something.com/news/")[0]
print(resp.status)

