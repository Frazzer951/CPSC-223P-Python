sandwich_orders = ["Tuna", "Beef", "Jam", "Bacon", "Turkey"]
finished_sandwiches = []

while sandwich_orders:
    print("I made your {} sandwich".format(sandwich_orders[-1]))
    finished_sandwiches.append(sandwich_orders.pop())

print("All the finished_sandwiches")
for sandwich in finished_sandwiches:
    print("\t{}".format(sandwich))