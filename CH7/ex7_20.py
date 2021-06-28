# Factorial & Fibonacci
#Factorial function
def factorial(n):
    if n == 1:
        return 1  #constant(minimum solution)
    else:
        res = n * factorial(n-1)
        return res

#Fibonacci function
def fib(n):
    if n == 0:
        return 0  #constant(minimum solution)
    elif n == 1:
        return 1  #constant(minimum solution)
    else:
        return fib(n-1) + fib(n-2)
#call both functions
print("Factorial (5) = ",factorial(5))
print("Fibonacci (5) = ",fib(5))

