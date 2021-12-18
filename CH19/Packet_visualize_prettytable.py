from scapy.all import *
from collections import Counter
from prettytable import PrettyTable

packets = rdpcap('example.pcap')
srcIP = []
for pkt in packets:
    if IP in pkt:
        try:
            srcIP.append(pkt[IP].src)
        except:
            pass
cnt = Counter()
for ip in srcIP:
    cnt[i] += 1

table = PrettyTable(["IP", "Count"])
for ip, count in cnt.most_common():
        table.add_row([ip, count])
print(table)
