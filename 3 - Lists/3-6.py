guest_list = ["Elon Musk", "Albert Einstein", "Steven Hawking"]

for i in range(len(guest_list)):
    print(
        f"Dear {guest_list[i]}, Would you like to have a nice dinner and chat about science?"
    )


print("\nEinstein declined the Invitation!\n")

guest_list[1] = "Nikola Tesla"

for i in range(len(guest_list)):
    print(
        f"Dear {guest_list[i]}, Would you like to have a nice dinner and chat about science?"
    )

print("\nA larger table has been found!\n")

guest_list.insert(0, "Alan Turing")
guest_list.insert(int(len(guest_list) / 2), "Ada Lovelace")
guest_list.append("Linus Torvalds")

for i in range(len(guest_list)):
    print(
        f"Dear {guest_list[i]}, Would you like to have a nice dinner and chat about science?"
    )
