# Scope of variables
total = 0; # This is global variable.
def sum(arg1, arg2):
   # Add both the parameters and return them.
   total = arg1 + arg2; # Here total is local variable.
   print ("Total of local variable inside function : ", total)
   return total;
# calling sum function
sum(5, 10);
print ("Total of global variable outside function : ", total)


