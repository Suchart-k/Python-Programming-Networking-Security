import socket
import struct
from datetime import datetime

s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
dict = {}
file_txt = open("attack_DDoS.txt",'a')
t1 = str(datetime.now())
file_txt.writelines(t1)
file_txt.writelines("\n")

No_of_IPs = 15
R_No_of_IPs = No_of_IPs + 10
while True:
    pkt = s.recvfrom(2048)
    ipheader = pkt[0][14:34]
    ip_hdr = struct.unpack("!8sB3s4s4s", ipheader)
    IP = socket.inet_ntoa(ip_hdr[3])
    print ("The Source of the IP is:", IP)

    if dict.has_key(IP):
        dict[IP] = dict[IP] + 1
        print (dict[IP])

    if(dict[IP] > No_of_IPs) and (dict[IP] < R_No_of_IPs):
        line = "DDOS attack is Detected: "
        file_txt.writelines(line)
        file_txt.writelines(IP)
        file_txt.writelines("\n")
    else:
        dict[IP] = 1
       
