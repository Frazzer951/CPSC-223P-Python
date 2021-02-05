# Find all prime numbers from 2 to 1000, using just lists, for, if, in, and remove

numbers = [x for x in range(2, 1000)]

for num in numbers:
    for x in range(2, 1000):
        if num * x in numbers:
            numbers.remove(num * x)

print(numbers)