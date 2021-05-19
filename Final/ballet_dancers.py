
# uncomment the lists and put this code in your module
# American Ballet Theatre
#abt_dancers = ['Sylvie', 'Natalie', 'Johnathan', 'Isabella', 'Sara', 'Jerry']

#New York City Ballet
#ncb_dancers = ['Ingram','Patrick', 'Takako', 'Misty', 'Amanda']


import ballet as b

# Test #1 - Nominal case
if b.in_troupe('Sylvie','ABT'):
	print("Test 1 correct")
else:
	print("Test 1 incorrect")

# Test #2 - Nominal case using default value
if b.in_troupe('Sylvie'):
	print("Test 2 correct")
else:
	print("Test 2 incorrect")

# Test #3 - Nominal case for dancer not in troupe
if b.in_troupe('Sylvie', "NCB"):
	print("Test 3 incorrect")
else:
	print("Test 3 correct")

# Test #4 - Nominal case for dancer in NCB
if b.in_troupe('Misty', "NCB"):
	print("Test 4 correct")
else:
	print("Test 4 incorrect")

# Test #5 - Using default for dancer not in troupe
if b.in_troupe('Misty'):
	print("Test 5 incorrect")
else:
	print("Test 5 correct")

# Test #6 - Unknown ballet troupe
if b.in_troupe('Misty', 'Anaheim Ballet'):
	print("Test 6 incorrect")
else:
	print("Test 6 correct")

# Test #7 - Test conversion of dancer to title case
if b.in_troupe('isabella','ABT'):
	print("Test 7 correct")
else:
	print("Test 7 incorrect")

# Test #8 - Test conversion of troupe to upper case
if b.in_troupe('Isabella','ABt'):
	print("Test 8 correct")
else:
	print("Test 8 incorrect")

