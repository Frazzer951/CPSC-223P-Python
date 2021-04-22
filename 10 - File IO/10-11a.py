import json

fav_number = input("Please enter your favorite number: ")

with open("fav_number.json", "w") as f:
    json.dump(fav_number, f)