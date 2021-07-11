import socket
import ssl

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s = ssl.wrap_socket(s)
    s.connect(('google.com', 443))
    request = b'GET google.com HTTP/1.1\n\n'
    s.send(request)
    print(s.recv(4096).decode())

main()

