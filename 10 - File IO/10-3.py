name = input("Please enter your name: ")

with open("guest.txt", "w") as f:
    f.write(name)