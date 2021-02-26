toppings = []

while True:
    topping = input("Please enter a topping, or type quit to exit: ")
    if topping.lower() == "quit":
        break
    print("Adding {} to your pizza".format(topping))
    toppings.append(topping)

print("Your pizza will have the following toppings:")
for topping in toppings:
    print(f"\t{topping}")