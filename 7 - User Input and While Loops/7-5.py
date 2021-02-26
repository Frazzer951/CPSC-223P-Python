while True:
    age = input("Please enter your age to see your ticket price, or quit to exit:")

    if age.lower() == "quit":
        break
    age = int(age)
    if age < 3:
        print("The Ticket is free")
    elif age < 12:
        print("The Ticket is $10")
    else:
        print("The Ticket is $15")
