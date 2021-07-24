import requests
urls = open("URLs.txt", "r")

for url in urls:
   url = url.strip()
   req = requests.get(url)
   print (url, 'report:')
   
   try:
      protection_xss = req.headers['X-XSS-Protection']
      if protection_xss != '1; mode = block':
          print ('X-XSS-Protection not set properly, it may be possible:', protection_xss)
   except:
       print ('X-XSS-Protection not set, it may be possible')
      
   try:
       options_content_type = req.headers['X-Content-Type-Options']
       if options_content_type != 'nosniff':
           print ('X-Content-Type-Options not set properly:', options_content_type)
   except:
       print ('X-Content-Type-Options not set')
       
   try:
       transport_security = req.headers['Strict-Transport-Security']
   except:
       print ('HSTS header not set properly, Man in the middle attacks is possible')
      
   try:
       content_security = req.headers['Content-Security-Policy']
       print ('Content-Security-Policy set:', content_security)
   except:
       print ('Content-Security-Policy missing')
