def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


user_profile = build_profile(
    "Luke",
    "Eltiste",
    location="Anaheim",
    field="Computer Science",
    hobby="Youtube Watching",
)
print(user_profile)

if "hobby" in user_profile:
    print("Hobby is present")