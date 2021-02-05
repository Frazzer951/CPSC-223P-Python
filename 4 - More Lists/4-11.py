pizzas = ["Pepperoni Pizza", "Cheese Pizza", "Meat Lovers Pizza"]

for pizza in pizzas:
    print(f"I like {pizza}")

print("Pizza is alright, it is always a good backup when nothing else sounds good")

friend_pizzas = pizzas.copy()

pizzas.append("Sausage Pizza")
friend_pizzas.append("BBQ Pizza")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(f"\t{pizza}")

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"\t{pizza}")
