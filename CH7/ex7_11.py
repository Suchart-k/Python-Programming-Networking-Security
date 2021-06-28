# Lambda vs normal function in same name
def f(x, y, z): return x + y + z
f = lambda x, y, z: x - y - z
#Calling normal function
print("Calling lambda function :", f(2, 2, 2))
#calling lambda function
print("Calling normal function :", f(2, 3, 4))



