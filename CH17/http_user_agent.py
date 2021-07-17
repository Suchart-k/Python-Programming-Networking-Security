import httplib2
 
http = httplib2.Http()
content = http.request("http://localhost/agent.php", method="GET", 
                  headers={'user-agent': 'Python script'})[1]
 
print(content.decode())
