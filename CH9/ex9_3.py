# Try...except with no any exceptions
try:
   fh = open("myfile", "w")
   fh.write("This is my file for exception handling!!")
except:
   print ("IO Error with File")
else:
   print ("Written content in the file successfully")
   fh.close()


