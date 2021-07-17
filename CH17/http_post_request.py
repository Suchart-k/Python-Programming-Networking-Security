import httplib2
import urllib
 
http = httplib2.Http()
 
body = {'name': 'Suchart'}
 
content = http.request("http://localhost/target.php", 
                       method="POST", 
                       headers={'Content-type': \
                                'application/x-www-form-urlencoded'},
                       body=urllib.parse.urlencode(body) )[1]
 
print(content.decode())


