'''Chat Client for a multi-client chat room'''
from socket import *

HOST = 'localhost'
PORT = 5000
BUFSIZE = 4096
ADDRESS = (HOST, PORT) #(127.0.0.1, 5000)

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)
messageFromServer =  bytes.decode(server.recv(BUFSIZE))
print(messageFromServer)
name = input('Enter your name: ')
userName = str.encode(name)
server.send(userName)

while True:
    receiveMessage = bytes.decode(server.recv(BUFSIZE))
    if not receiveMessage:
        print('Server disconnected')
        break
    print(receiveMessage)
    sendMessage = input('> ')
    if not sendMessage:
        print('Server disconnected')
        break
    server.send(str.encode(sendMessage))
server.close()

