people = {
    "Duke": {
        "first": "Duke",
        "last": "Ellington",
        "Bday": "April 29, 1899",
        "bplace": "Washington D.C.",
        "quote": "Gray skies are just clouds passing over.",
    },
    "Miles": {
        "first": "Miles",
        "last": "Davis",
        "Bday": "May 26, 1926",
        "bplace": "Alton, IL",
        "quote": "I always listen for what I can leave out.",
    },
    "Goro": {
        "first": "Goro",
        "last": "Masamune",
        "Bday": "May 26, 1926",
        "bplace": "Japan",
        "quote": "I made the Honjo Masamune.",
    },
}

print("Name                     Birthdate          Birthplace                Quote    ")
print("-" * 85)

for person in people:
    print(
        "{:<25}{:<19}{:<26}{}".format(
            people[person]["last"] + ", " + people[person]["first"],
            people[person]["Bday"],
            people[person]["bplace"],
            people[person]["quote"],
        )
    )
