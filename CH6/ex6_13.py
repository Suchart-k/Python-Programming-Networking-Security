# Calcuting the average of two dices
import random
count, avg1, avg2 = 1, 0, 0
while count <= 100:
    dice1, dice2 = random.randrange(6)+1, random.randrange(6)+1
    avg1, avg2, count = avg1 + dice1, avg2 + dice2, count + 1

print("Average of dice1 = %0.2f and dice2 = %0.2f"%(avg1, avg2))
if avg1 > avg2:
    print("Average of dice1 > dice2")
else:
    print("Average of dice2 > dice1")

