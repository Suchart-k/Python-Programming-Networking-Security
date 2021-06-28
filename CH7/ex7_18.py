# Define variables
def modifyVar1():
    var1, var2 = 10, 20 #These are local variables
    print("Local variables are var1 = %d, var2 = %d"%(var1, var2))
def modifyVar2(var1, var2):
    var1 = 30 #var1 is local, and var2 is global
    print("Local variable var1 = %d, and global var2 = %d"%(var1, var2))
def modifyVar3(var1):
    global var2
    var2 = 3
    return var1**var2
def modifyVar4():
    global var1
    var1 = var1**2
    return
var1, var2 = 5, 5
modifyVar1()
modifyVar2(5, 10)
print("Var1 and Var2 in main program = %d, %d"%(var1, var2))
print(modifyVar3(var1))
print("Var1 and Var2 in main program = %d, %d"%(var1, var2))
modifyVar4()
print("Var1 and Var2 in main program = %d, %d"%(var1, var2))


