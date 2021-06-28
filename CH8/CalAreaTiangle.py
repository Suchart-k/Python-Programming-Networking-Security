# Calculating Triangles Area
# This module named CalAreaTriangle.py
def triangle(height, base):
   return 1/2 * height * base

def equilateral(width):
   return 3**(1/2) * width * width

def isosceles(base, sidebase):
   return base/4 * 4 * (((sidebase*sidebase) - (base*base)))**(1/2)

def pythagorean(perpendicular):
   return 0.5 * perpendicular * perpendicular



