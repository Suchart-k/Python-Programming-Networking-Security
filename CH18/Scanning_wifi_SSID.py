import pywifi
from comtypes import GUID
import time

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
time.sleep(2)
result=iface.scan_results()

for i in range(len(result)):
    print(result[i].ssid, result[i].bssid)

    
