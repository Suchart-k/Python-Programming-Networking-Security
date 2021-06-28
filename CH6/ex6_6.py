Score = float(input("Enter your score :"))
Msg = "Your grade is ";
if Score >= 80:
    print(Msg + "A")
elif Score >= 75:
    print(Msg + "B+")
elif Score >= 70:
    print(Msg + "B")
elif Score >= 65:
    print(Msg + "C+")
elif Score >= 60:
    print(Msg + "C")
elif Score >= 55:
    print(Msg + "D+")
elif Score >= 50:
    print(Msg + "D")
else:
    print(Msg + "F")
print("Good bye!")

