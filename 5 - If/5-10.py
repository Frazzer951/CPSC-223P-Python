current_users = ["Luke", "Carl", "Ryan", "John", "Ben"]
current_users_lower = [user.lower() for user in current_users]
new_users = ["Jeff", "Frank", "John", "Jake", "Carl"]


for user in new_users:
    if user.lower() in current_users_lower:
        print(f"The username {user} is taken, please find another")
    else:
        print(f"The username {user} is available")
