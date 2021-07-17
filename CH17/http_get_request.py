import httplib2
 
http = httplib2.Http()
content = http.request("http://localhost/hello.php?name=Suchart", 
                       method="GET")[1]
 
print(content.decode())

