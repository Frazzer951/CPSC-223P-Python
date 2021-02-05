guest_list = ["Elon Musk", "Albert Einstein", "Steven Hawking"]

for i in range(len(guest_list)):
    print(
        f"Dear {guest_list[i]}, Would you like to have a nice dinner and chat about science?"
    )


print("Einstein declined the Invitation!")

guest_list[1] = "Nikola Tesla"

for i in range(len(guest_list)):
    print(
        f"Dear {guest_list[i]}, Would you like to have a nice dinner and chat about science?"
    )
