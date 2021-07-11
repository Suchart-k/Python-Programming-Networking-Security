import socket
import sys 
  
try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    print("Socket successfully created")
except socket.error as err: 
    print ("Socket creation failed with error %s" %(err))
  
# default port for HTTTP protocol
port = 80
  
try: 
    host_ip = socket.gethostbyname('www.google.com') 
except socket.gaierror: 
    # this means could not resolve the host 
    print ("There was an error resolving the host")
    sys.exit() 
print ("Host ip is ", host_ip)  
# connecting to the server 
s.connect((host_ip, port)) 
  
print ("The socket has successfully connected to google") 
