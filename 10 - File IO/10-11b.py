import json

with open("fav_number.json") as f:
    fav_number = json.load(f)

print(f"I know your favorite number! It’s {fav_number}.")