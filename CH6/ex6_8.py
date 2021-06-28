# Comparing the minimum of 3 numbers
num1 = float(input("Enter 1'st number :"));
num2 = float(input("Enter 2'nd number :"));
num3 = float(input("Enter 3'rd number :"));
if num1 < num2:
    if num1 < num3:
        min_num = num1
    else:
        min_num = num3
elif num2 < num3:
    min_num = num2
else:
    min_num = num3
print("Minimum number is ",min_num)

