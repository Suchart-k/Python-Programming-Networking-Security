# Variable-length arguments 
def printinfo(arg1, *vartuple):
   "This prints a variable passed arguments"
   print ("Output of formal arg is : ",arg1)
   for var in vartuple:
      print ("Output of virtuple arg is : ",var)
   return;
# Now you can call printinfo function
printinfo(10);
printinfo(70, 60, 50);



