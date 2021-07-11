import socket

UDP_IP_ADDRESS  = "127.0.0.1"
UDP_PORT        = 6789
bufferSize      = 4096
serverAddress   = (UDP_IP_ADDRESS ,UDP_PORT)
UDPClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    message = input('>> ').strip()
    if message == "quit":
        break
    bytesToSend = str.encode(message)
    UDPClientSocket.sendto(bytesToSend, serverAddress)
    data,addr = UDPClientSocket.recvfrom(bufferSize)
    print("Message from Server >> ", data.decode())
    
UDPClientSocket.close()

