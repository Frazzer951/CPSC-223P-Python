def makeusername(firstname, lastname):
    username = lastname[:3]
    username += firstname[:3]
    username += "2"
    return username


firstname = input("Give me a first name: ")
lastname = input("Give me a last name: ")

print("Computer System name is:", makeusername(firstname, lastname))
