import os
import platform
import subprocess 

osx = platform.system()
if (osx == "Windows"):
    command = "dir"
elif (osx == "Linux"):
    command = "ls"

subprocess.run(command, shell=True)

