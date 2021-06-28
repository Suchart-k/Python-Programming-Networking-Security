# Try...except first program
try:
   fh = open("myfile", "w")
   fh.write("This is my file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()

