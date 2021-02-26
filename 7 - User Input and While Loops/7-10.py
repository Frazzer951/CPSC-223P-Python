dream_vacations = {}

while True:
    name = input("\nPleas enter your name or quit to exit: ")
    if name.lower() == "quit":
        break
    vac1 = input("Please enter the country of your dream vacation: ")
    vac2 = input("Please enter the country of your second dream vacation: ")
    dream_vacations[name] = [vac1, vac2]

for name in dream_vacations:
    print(
        f"{name} would like to goto {dream_vacations[name][0]} on their first vacation and {dream_vacations[name][1]} on their second"
    )
