import socket
import sys

def scanPorts(ip, lstPort):
    try:
        for port in lstPort:
            sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print ("Port {}: \t Open".format(port))
            else:
                print ("Port {}: \t Closed".format(port))
            sock.close()
    except socket.error as error:
        print (str(error))
        print ("Connection error")
        sys.exit()

list_port = [20, 22, 23, 25, 52, 53, 80, 443, 1205, 1206, 1207]
scanPorts('localhost', list_port)


