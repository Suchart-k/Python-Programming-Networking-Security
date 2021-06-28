# Try...except, else and finally
try:
   fh = open("myfile", "w")
   fh.write("This is my file for exception handling!!")
except:     
   print("IO Error with File")
else:
   print("Written content in the file successfully")
finally:
   print("This file is closed completely")
   fh.close()


