import os
import platform
osx = platform.system()
print(osx)
if (osx == "Windows"):
    ping_command = "ping -n 10 127.0.0.1"
elif (osx == "Linux"):
    ping_command = "ping -c 10 127.0.0.1"
else :
    ping_command = "ping -c 10 127.0.0.1"
    
os.system(ping_command)


