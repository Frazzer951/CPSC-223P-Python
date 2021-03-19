rivers = {"Nile": "Egypt", "Amazon": "Peru", "Red Rock": "Unite States Of America"}

for river in rivers:
    print(f"The {river} river runs through {rivers[river]}")

print("The Rivers:")
for river in rivers:
    print("\t" + river)

print("The Countries:")
for river in rivers:
    print("\t" + rivers[river])
