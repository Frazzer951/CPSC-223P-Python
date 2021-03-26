remove_list = [1, 5, 7, 9]

list = [x for x in range(11) if x not in remove_list]

print(list)