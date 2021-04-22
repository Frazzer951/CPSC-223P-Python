while True:
    name = input("Please enter your name or 'quit': ")

    if name.lower() == "quit":
        break

    print(f"Welcome {name}, it's nice to see you!")

    with open("guest_book.txt", "a") as f:
        f.write(name + "\n")
