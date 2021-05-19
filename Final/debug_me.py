# Do not modify the test data
users = ["Alex", "Admin", "Weinrib", "Neil", "John"]

# Modify this code
if len(users) == 0:
    print("There are no users")
else:
    for user in users:
        if user == "Admin":
            print("Hello all powerful one.")

        else:
            print("You are a normal user.")
