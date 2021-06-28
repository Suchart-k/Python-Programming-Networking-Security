# Raising exception example 2
try:
    f = open("myfile","w")
    f.write("This is my test file for exception handling!!")
except(IOError, ValueError):
    print("An I/O error or a ValueError occurred")
    raise OSError("Permission denied")
except:
    print("An unexpected error occurred")
    raise
else:
   f.close()
   print("Myfile was closed!!")
finally:
   print("Program has finished")


