all_users = ["Luke", "John", "Ben"]

print("All Users:", all_users)

all_users.append("Carl")

untrusted_users = ["Ben", "Ryan"]

print("Untrusted Users:", untrusted_users)

trusted_users = [user for user in all_users if user not in untrusted_users]

print("Trusted Users:", trusted_users)

all_users = {"Luke", "Carl", "Ryan", "John", "Ben"}
untrusted_users = {"Ben", "Frank"}
trusted_users = all_users - untrusted_users

print("\nAll Users:", all_users)
print("Untrusted Users:", untrusted_users)
print("Trusted Users:", trusted_users)
