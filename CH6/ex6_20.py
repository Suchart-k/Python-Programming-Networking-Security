# explain function range
import sys, random
sys.stdout.write("Show range (6) = ")
for i in range(6):
    sys.stdout.write(str(i) + " ")
print("\n" + "-" *70)
sys.stdout.write("Show range (1, 7) = ")
for j in range(1, 7):
    sys.stdout.write(str(j) + " ")
print("\n" + "-" *70)
sys.stdout.write("Show range (1, 36, 2) = ")
for o in range(1, 36, 2):    
    sys.stdout.write(str(o) + " ")
print("\n" + "-" *70)

sys.stdout.write("Show range [1, 3,..., 36] =")
for r in [1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36]:
    sys.stdout.write(str(r) + " ")
print("\n" + "-" *70)
sys.stdout.write("Show multiple range = ")
for d1 in range(2):
    for d2 in range(2):
        print (d1 + 1, "+", d2+1, '=', d1+d2+2)
print("\n" + "-" *70)
sys.stdout.write("Show range + random = ")
for i in range(5):
    d1= random.randrange(6)+1
    d2= random.randrange(6)+1
    print (d1+d2)
print("Show range backward")
for i in range(5, 0, -1):
    print(i)

