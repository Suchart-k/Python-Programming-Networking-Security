import os
# you can adjust the "/" to a directory which your choice
for file in os.walk("./"):
    print(file)


