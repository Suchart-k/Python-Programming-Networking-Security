# Returning multiple values
import random
def rollDice():
    return (1 + random.randrange(6), 1 + random.randrange(6))
d1, d2 = rollDice()
print (d1,",",d2)
d1, d2 = rollDice()
print (d1,",",d2)
d1, d2 = rollDice()
print (d1,",",d2)



