# Raising exception example 3
def f(x):
    return g(x) + 1 
def g(x):
    if x < 0: raise (ValueError, ("I can't settle with a negative number."))
    else: return 5 
try:
    print (f(3))
    print (f(-5))
except ValueError:
    print ("That value was invalid.")


