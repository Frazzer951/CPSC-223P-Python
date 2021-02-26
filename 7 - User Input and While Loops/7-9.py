sandwich_orders = [
    "Tuna",
    "Pastrami",
    "Beef",
    "Jam",
    "Pastrami",
    "Bacon",
    "Turkey",
    "Pastrami",
]
finished_sandwiches = []

print("The Deli has run out of Pastrami\n")

while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    print("I made your {} sandwich".format(sandwich_orders[-1]))
    finished_sandwiches.append(sandwich_orders.pop())

print("\nAll the finished_sandwiches")
for sandwich in finished_sandwiches:
    print("\t{}".format(sandwich))