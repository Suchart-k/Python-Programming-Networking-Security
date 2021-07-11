import socket

localIP     = "127.0.0.1"
localPort   = 6789
bufferSize  = 4096
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

UDPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

while(True):
    data,addr = UDPServerSocket.recvfrom(bufferSize)
    print ("received from: ",addr)
    print ("message: ", data)
    UDPServerSocket.sendto(bytesToSend, addr)

UDPServerSocket.close()

