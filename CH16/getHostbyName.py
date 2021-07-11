import socket

ip_addr = socket.gethostbyname('google.com')
print(ip_addr)
ip_addr = socket.gethostbyname_ex('google.com')
print(ip_addr)
ip_addr = socket.getfqdn('google.com')
print(ip_addr)

