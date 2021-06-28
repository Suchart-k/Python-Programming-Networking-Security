# Assert preconditions
def DIV(x, y):
    assert (y != 0), "Cann't divide by zero!!!"
    return x / y 
print (DIV(5, 3))
print (DIV(5, 0))


