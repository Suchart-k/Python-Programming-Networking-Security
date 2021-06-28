# Creating instance objects of Employee class
class Employee:
   'To declear super class Employee for all employee'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee =%d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

#Creating instance objects
employee1 = Employee("John", 25000)
employee2 = Employee("Lisa", 20000)
employee1.displayEmployee()
employee2.displayEmployee()
employee1.displayCount()
employee1.empCount = 5
employee1.salary = 30000
employee2.salary = 28000
employee1.displayEmployee()
employee2.displayEmployee()
employee2.displayCount()




