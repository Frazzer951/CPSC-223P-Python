def sandwich_orders(**items):
    print("The Sandwich is")
    for item in items:
        print(f"\t{item}: ")
        print(f"\t\t{items[item]}")

sandwich_orders(bread='Wheat', topping='Cheese')
sandwich_orders(bread='White', topping='Chicken and BBQ Sauce', condiment='ketchup')
sandwich_orders(bread='Grain')