# Destroying any obects that not use 
class Car:
   def __init__(self, color='red', speed=100):
      self.color = color
      self.speed = speed
      
# Deconstructor method   
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "object has destroyed")

car1 = Car()
car2 = car1
car3 = car1
# prints the ids of the obejcts
print ("ID[car1]=",id(car1),", ID[car2]=",id(car2),", ID[car3]=",id(car3)) 
del car1
del car2
del car3


