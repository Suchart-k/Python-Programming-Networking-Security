# Mini-calculator program
def menu():
#print what options you have
    print ("Welcome to calculator program")
    print ("your options are:")
    print (" ")
    print ("1) Addition")
    print ("2) Subtraction")
    print ("3) Multiplication")
    print ("4) Division")
    print ("5) Quit calculator program")
    print (" ")
    return int(input("Choose your option: "))
    
# this adds two numbers given
def add(a, b):
    print("You chose the Addition")
    print ("Result of ",a, "+", b, "=", a + b)
    return a + b
    
# this subtracts two numbers given
def sub(a, b):
    print("You chose the Subtraction")
    print ("Result of ",a, "-", b, "=", a - b)
    return a - b
    
# this multiplies two numbers given
def mul(a, b):
    print("You chose the Multiplication")
    print ("Result of ",a, "*", b, "=", a * b)
    return a * b
    
# this divides two numbers given
def div(a, b):
    print("You chose the Division")
    if b != 0:
        print ("Result of ",a, "/", b, "=", a / b)
        return a / b
    else:
        print("Can't divide by zero")
        return False
        
# this is main program for control all def
def main():
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
        if choice == 1:
            add(int(input("Number 1:")),int(input("Number 2:")))
        elif choice == 2:
            sub(int(input("Number 1:")),int(input("Number 2:")))
        elif choice == 3:
            mul(int(input("Number 1:")),int(input("Number 2:")))
        elif choice == 4:
            div(int(input("Number 1:")),int(input("Number 2:")))
        elif choice == 5:
            loop = 0
    else:
            print("Good bye! ")

if __name__ == "__main__":
    main()



