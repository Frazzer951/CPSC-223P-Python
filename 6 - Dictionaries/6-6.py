favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

people_who_should_take_poll = ["jen", "carl", "ben", "phil", "alfonso"]

for name in people_who_should_take_poll:
    if name in favorite_languages:
        print(f"{name.title()}, Thank you for taking the poll")
    else:
        print(f"{name.title()}, do you want to take the Favorite Languages poll?")