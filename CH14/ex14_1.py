protocols = []
protocols.append("HTTP")
protocols.append("SSH")
protocols.append("FTP")
protocols.append("DNS")
protocols.append("SMTP")
print(protocols)
protocols.sort()
print(protocols)
print(type(protocols))
print("Number of members in protocols is ", len(protocols))
pos = protocols.index("HTTP")
print("HTTP position is in " + str(pos))
protocols.remove("SMTP")
print(protocols)
print("Number of members in protocols after remove is ", len(protocols))

for proto in protocols:
    print (proto)

