numbers = [x for x in range(1, 10)]

for num in numbers:
    if num % 10 == 1:
        print(f"{num}st")
    elif num % 10 == 2:
        print(f"{num}nd")
    elif num % 10 == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")