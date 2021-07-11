import socket, sys

host_name = socket.gethostbyaddr('8.8.8.8')
print(host_name)
service = socket.getservbyname('http')
print(service)
service = socket.getservbyname('smtp','tcp')
print(service)
service = socket.getservbyport(80)
print(service)
service = socket.getservbyport(23)
print(service)

