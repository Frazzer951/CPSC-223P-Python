def generic_sequence_func(p1, p2):
    """What does this function do?"""
    for i in range(p2):
        for e in p1[i]:
            print(e)


try:
    # Determine what parameters go into this function
    generic_sequence_func(XXX, YYY)             # Get Name Error
    #generic_sequence_func([10, 12], 10)         # Get Type Error
    #generic_sequence_func([[10], [12]], 10)     # Get Index Error
    #generic_sequence_func([[10], [12]], 2)      # Working
except NameError as e:
    print("Name Error has occurred.")
    print(e)
    print("Variables must be defined!")
except TypeError as e:
    print("Type Error has occurred.")
    print(e)
    print("p1 must be an iterable of iterables")
    print("i.e. A List of Lists")
except IndexError as e:
    print("Index Error has occurred.")
    print(e)
    print("p2 must be less than or equal to the length of p1")
