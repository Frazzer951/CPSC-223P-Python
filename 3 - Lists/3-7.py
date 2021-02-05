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

print(f"\nThere have been {len(guest_list)} people invited to dinner.")
print(
    "There is only room for two people at dinner, for the table wont arrive in time!\n"
)

while len(guest_list) > 2:
    person = guest_list.pop()
    print(f"Sorry {person} but you are no longer invited")

for i in range(len(guest_list)):
    print(f"{guest_list[i]} you are still invited!")

guest_list.remove(guest_list[-2])
del guest_list[-1]

print(guest_list)