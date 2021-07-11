import socket
import sys
from datetime import datetime
import errno

remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)
print ("Please enter the port range for scanning")
startPort = int(input("Enter a start port: "))
endPort = int(input("Enter a end port: "))
print ("Please wait, scanning remote host", remoteServerIP)
t1 = datetime.now()

try:
    for port in range(startPort , endPort):
        print ("Checking port {} ...".format(port))
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: Open".format(port))
        else:
            print ("Port {}: Closed".format(port))    
            print ("Reason:", errno.errorcode[result])
        sock.close()
except KeyboardInterrupt:
    print ("You pressed Ctrl+C")
    sys.exit()
except socket.gaierror:
    print ('Hostname could not be resolved. Exiting')
    sys.exit()
except socket.error:
    print ("Couldn't connect to server")
    sys.exit()

t2 = datetime.now()
total = t2 - t1
print ('Port Scanning Completed in: ', total)
