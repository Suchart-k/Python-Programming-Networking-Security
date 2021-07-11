services1 = {"ftp":21, "ssh":22, "smtp":25, "http":80}
services2 = {"ftp":21, "ssh":22, "snmp":161, "ldap":389}
services1.update(services2)
print(services1)

