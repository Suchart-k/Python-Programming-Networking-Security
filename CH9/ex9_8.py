# Raising exception example 1 
def functionName(level):
   if level < 1:
      raise ("Invalid level!", level)
      print("The code would not be executed")
   print("Good Bye!")

functionName(5)
functionName(0)


