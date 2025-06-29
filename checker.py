while True:
    n = int(input("Enter a number: "))
    if n == 0:
        print("This number is zero.")
    elif n % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")
    again = input("Continue? (yes/no): ")
    if again.lower() == "no":
        break
