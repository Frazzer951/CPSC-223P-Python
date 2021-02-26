genders = ["Male", "Female"]
counties = ["Orange County", "LA County", "Riverside county"]

students = [[gender, county] for gender in genders for county in counties]

print(students)