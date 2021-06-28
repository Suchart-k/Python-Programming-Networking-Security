# Computing exponent
def exp(x, n):
    if n == 0:
        return 1  #constant(minimum solution)
    else:
        return x * exp(x, n-1)
print("Exponet of 2^4 = ",exp(2, 4))


