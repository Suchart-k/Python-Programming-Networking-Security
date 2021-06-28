# Creating car class(private attributes & methods)
class Car:
    # attributes
    color = "No brand yet"
    brand = "No brand yet"
    number_of_seats = 4
    number_of_wheels = 4
    maxSpeed = 0
    registration_number = 0
    
    def __init__(self, color, brand, number_of_seats, number_of_wheels, \
                 maxSpeed):
        self.color = color
        self.brand = brand
        self.number_of_seats = number_of_seats
        self.number_of_wheels = number_of_wheels
        self.maxSpeed = maxSpeed
        self.registration_number += 1
 
    # methods
    def setColor(self,x):
        self.Color = x
        
    def setBrand(self,x):
        self.brand = x

    def setNumberOfSeats(self,x):
        self.number_of_seats = x
        
    def setNumberOfWeels(self,x):
        self.number_of_wheels = x

    def setMaxSpeed(self,x):
        self.maxSpeed = x
 
    def printData(self):
        print("The color of this car is :", self.color)
        print("The car was manufactured by :", self.brand)
        print("The number of seats is :", self.number_of_seats, "seats.")
        print("The number of wheels is :", self.number_of_wheels, "wheels.")
        print("The maximum speed is :", self.maxSpeed, "km/h.")
        print("The registration number is :", self.registration_number)

# Creating instance and use it
car1 = Car('red','Toyota',4,4,150)
car1.printData()
car1.color = 'Blue'
car1.printData()
car2 = Car('Yello','Honda',4,4,170)
car2.printData()



