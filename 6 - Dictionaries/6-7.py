luke = {"first_name": "Luke", "last_name": "Eltiste", "age": 19, "city": "Anaheim"}
carl = {"first_name": "Carl", "last_name": "Hansen", "age": 20, "city": "Orange"}
ryan = {"first_name": "Ryan", "last_name": "Daily", "age": 19, "city": "Hamden"}

people = [luke, carl, ryan]

for person in people:
    print(
        f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in the city of {person['city']}"
    )
