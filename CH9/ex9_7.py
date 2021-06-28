# Argument of Exception
# Define a function here.
def temp_convert(var):
   try:
      return int(var)
   except ValueError as Args:
      print ("Argument doesn’t contain numbers\n", Args.args)
# Call above function here.
temp_convert("xyz");


