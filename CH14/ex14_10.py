def divide(x, y):
    return x/y

try:
    divide(5, 0)
except Exception as e:
    print("Error = "+str(e))
print("End program")

