# Showing inheritance, constructor and deconstructor 
# Define parent class
class ClassicCar:
   register_number = 0
   color = 'white'
   #Constructor method
   def __init__(self):
      ClassicCar.register_number += 1
      print ("ClassicCar: Constructor")
      
   def ClassicCarGetReg(self):
      print ("ClassicCar: Register number is ",self.register_number)
      
   def ClassicCarSetColor(self, color):
      self.color = color
      print ("ClassicCar: Set color")

   def ClassicCarGetColor(self):
      print ("ClassicCar: Get color is ",ClassicCar.color)
   
   #Deconstructor method   
   def __del__(self):
      class_name = self.__class__.__name__
      print ("ClassicCar: ",class_name, "object has destroyed")

# Define Toyota child class
class ToyotaCar(ClassicCar):
   def __init__(self):
      self.color = 'gold blond'
      print ("Toyota Car: Constructor")

   def ToyotaCarGetColor(self):
      print ('Toyota Car: Get color is ',self.color)

# Define Honda child class
class HondaCar(ClassicCar):
   def __init__(self):
      self.color = 'black'
      print ("Honda Car: Constructor")

   def HondaCarGetColor(self):
      print ('Honda Car: Get color is ',self.color)

# Define Dummy child class
class DummyCar(ClassicCar):
   color = 'No color'
   def DummyCarGetColor(self):
      print ('Dymmy Car: Get color is ',self.color)
      
#Creating Toyota car instance      
car1 = ToyotaCar()
car1.ClassicCarGetReg()
car1.ClassicCarGetColor()
car1.ClassicCarSetColor('green')
car1.ClassicCarGetColor()
car1.ToyotaCarGetColor()
#Creating Honda car instance      
car2 = HondaCar()
car2.ClassicCarGetReg()
car2.ClassicCarGetColor()
car2.ClassicCarSetColor('yello')
car2.ClassicCarGetColor()
car2.HondaCarGetColor()
#Creating Dummay car instance      
car3 = DummyCar()
car3.ClassicCarGetReg()
car3.ClassicCarGetColor()
car3.ClassicCarSetColor('pink')
car3.ClassicCarGetColor()
car3.DummyCarGetColor()
#Destroying all instances
del car1
del car2
del car3



