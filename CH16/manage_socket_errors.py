import socket,sys

host = "127.0.0.1"
port = 9999
try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except socket.error as e:
    print ("socket create error: %s" %e)
    sys.exit(1)
try:
    s.connect((host,port))
except socket.timeout as e :
    print ("Timeout %s" %e)
    sys.exit(1)
except socket.gaierror as e:
    print ("connection error to the server:%s" %e)
    sys.exit(1)
except socket.error as e:
    print ("Connection error: %s" %e)
    sys.exit(1)

