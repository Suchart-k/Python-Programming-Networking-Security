#Calculating discount price and VAT
name = input("Enter goods name :")
price = float(input("Enter price of %s :" %name))
if price >= 500:
    temp = price * 0.03
    price = price - temp
VAT = price * 0.07
price = price + VAT
print("The price of %s (inc VAT 7%%) is %.2f %s"%(name, price, "Baht."))

