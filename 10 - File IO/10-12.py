import json

try:
    with open("fav_number.json") as f:
        fav_number = json.load(f)

    print(f"I know your favorite number! It’s {fav_number}.")
except:
    fav_number = input("Please enter your favorite number: ")

    with open("fav_number.json", "w") as f:
        json.dump(fav_number, f)
