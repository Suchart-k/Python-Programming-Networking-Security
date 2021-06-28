# Try...except with keyboard
while True:
    try:
        n = int(input("Please enter an integer: "))
        break
    except ValueError:
        print("No valid integer! Please try again ...")
print("Great, you successfully entered an integer!")


