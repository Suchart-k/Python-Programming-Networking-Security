# Testing built-in attributes
class Employee:
   'To declear super class Employee for all employee'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee = %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

   def setEmpCount(self, x):
      Employee.empCount = x

#To access built-in attributes
print("Employee.__name__: ",Employee.__name__)
print("Employee.__doc__: ",Employee.__doc__)
print("Employee.__module__: ",Employee.__module__)
print("Employee.__dict__: ",Employee.__dict__)


