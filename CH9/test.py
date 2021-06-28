try:
   raise Networkerror("Bad hostname")
except Networkerror as e:
   print(e.args)


