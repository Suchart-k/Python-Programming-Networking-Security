import os
import platform
import subprocess 

osx = platform.system()
if (osx == "Windows"):
    command = "dir"
elif (osx == "Linux"):
    command = "ls"

result = subprocess.run(command, shell=True, capture_output=True, text=True)
print(result.stdout)



