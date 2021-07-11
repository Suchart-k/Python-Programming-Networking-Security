import subprocess

p = subprocess.Popen("dir", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print(output.decode())


