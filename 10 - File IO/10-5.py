while True:
    responce = input("Please enter why you like programming or 'quit': ")

    if responce.lower() == "quit":
        break

    with open("responce.txt", "a") as f:
        f.write(responce + "\n")
