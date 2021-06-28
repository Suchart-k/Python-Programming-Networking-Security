# Encapsulation/Data hinding
class Car:
   __color = 'red'
   register_count = 0
   
   def getColor(self):
      print("Color is:",self.__color)
      
   def setColor(self, color):
      self.__color = color
      print("Color is:",self.__color)

   def regCount(self):
      self.register_count += 1
      print("Register count is:",self.register_count)
      
car1 = Car()
car1.getColor()
car1.setColor("yellow")
car1.regCount()
car1.__color = 'green'
car1.getColor()
car1.register_count = 5
print(car1.register_count)
car1._Car__color = 'pink'
car1.getColor()


