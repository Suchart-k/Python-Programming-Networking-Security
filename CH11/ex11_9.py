# Overloading methods 
class Car:
   #Constructor overloading
   def __init__(self, *args):
      if(len(args)==0):
            print("No overloading")
      else:
            print("There are %d arguments overloading" %(len(args)))
            lists = []
            for i in args:
               lists.append(i)
            print("Constructor overloading arguments:",lists)

   #Method overloading   
   def printX(*args):
      if(len(args)==0):
            print("No overloading")
      else:
            print("There are %d arguments overloading" %(len(args)-1))
            lists = []
            for i in args:
               lists.append(i)
            print("Method overloading arguments:",lists[1:])
#Creating instance
car1 = Car()
car2 = Car("Toyota")
Car3 = Car("Toyota", "Honda", "BMW", "Audi", "Ford")
car1.printX()
car1.printX(5)
car1.printX(5, 6.5, -5, "Overloading")


