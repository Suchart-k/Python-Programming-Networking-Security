# Calcuting the average for N numbers
Count = 1
Sum = 0.0
print("To exit this program, please type 0 or 0.0 :")
Num = float(input("Enter a number :"))
while Num != 0 or Num != 0.0:
    Sum += Num
    Avg = Sum / Count
    Count += 1
    print ("Average of number is : ", Avg)
    Num = float(input("Enter a number :"))
print("Good bye!")

