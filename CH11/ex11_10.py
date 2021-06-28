# Overloading overators
import math
class Vector:
   x = y = z = 0
   def __init__(self, x, y, z):
      self.x = x
      self.y = y
      self.z = z

   # Overloading function print()
   def __str__(self):
      return '-->(' + str(self.x) + ',' + str(self.y) + ',' + str(self.z) + ')'

   # Overloading operator +
   def __add__(self, obj):
      return Vector(self.x + obj.x, self.y + obj.y , self.z + obj.z)
   
   # Overloading operator -
   def __sub__(self, obj):
      return Vector(self.x - obj.x, self.y - obj.y , self.z - obj.z)

   # Overloading operator **
   def __pow__(self, obj):
      return Vector(self.x ** obj.x, self.y ** obj.y , self.z ** obj.z)

   def squreRoot(self):
      return math.sqrt(self.x + self.y + self.z)

A = Vector(2, 3, 4)
B = Vector(4, 3, 0)
C = B - A
print (C)
D = Vector(2, 2, 2)
E = C ** D
print (E)
Y = E.squreRoot()
print (Y)


