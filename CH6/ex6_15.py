# Break for while and for loop
for letter in 'Python':  #First example for for loop
   if letter == 'h':
      break	#Break force exit for loop
   print('Current Letter :', letter)  

var = 10  #Second example while loop
while var > 0:
   print('Current variable value :', var)
   var = var - 1
   if var == 5:
      break	#Break force exit while loop
print("Good bye!")

