# Showing overriding methods 
# Define Classic car parent class
class ClassicCar:
   #ClassicCar method  
   def brake(self):
      print ("ClassicCar: Normal brake!")
       
# Define Toyota car child class
class ToyotaCar(ClassicCar):
   #ToyotaCar method  
   def brake(self):
      print ("ToyotaCar: Disk brake pad!")

# Define Honda car child class
class HondaCar(ClassicCar):
   #HondaCar method  
   def brake(self):
      print ("HondaCar: Drum brake pad!")

# Define Dummy car child class
class DummyCar(ClassicCar):
   pass

#Creating Toyota car instance      
car1 = ToyotaCar()
car1.brake()
#Creating Honda car instance      
car2 = HondaCar()
car2.brake()
#Creating Dummay car instance      
car3 = DummyCar()
car3.brake()


