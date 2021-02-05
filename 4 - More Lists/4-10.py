numbers = [i ** 3 for i in range(1, 11)]

for num in numbers:
    print(num)

print("The first three items in the list are:", numbers[:3])
print("Three items from the middle of the list are:", numbers[4:7])
print("The last three items in the list are:", numbers[-3:])
