temps = [30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 50]

print(temps)

for _ in range(100):
    # Copy temps into new_temps
    new_temps = temps.copy()

    # Average of left and right temps
    for i in range(1, len(temps) - 1):
        new_temps[i] = (temps[i - 1] + temps[i + 1]) / 2

    # If the new_temps equals the old temps, break out of loop
    if new_temps == temps:
        print(temps)
        break

    # Copy the new_temps into temps and print them out
    temps = new_temps.copy()
    print(temps)
