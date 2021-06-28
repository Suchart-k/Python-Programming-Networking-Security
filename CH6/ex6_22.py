# calculating PI
n = int(input("Enter integer number(odd) :"))
flag = False    #flag = True (+), flag = False (-)
num = 1
for i in range(3, n+2, 2):
    if flag == False:
        num = num - 1 / i
        flag = True
    else:
        num = num + 1 / i
        flag = False
print ("Result of PI/4 = %.4f" %num)

