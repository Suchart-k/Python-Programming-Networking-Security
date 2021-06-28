# Default arguments
def printinfo(name, age = 35):
   "This prints a passed info into this function"
   print ("Name: ", name);
   print ("Age: ", age);
   return;
# Now you can call printinfo function
printinfo(age=50, name="miki");
printinfo(name="miki");


