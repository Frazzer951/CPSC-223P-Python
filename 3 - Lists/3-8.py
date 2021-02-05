# Create a list of places to visit
places = ["Japan", "Germany", "UK", "Canada", "Hawaii"]

# Print the places list
print("The Original List:")
print(places)

# Print a sorted list
print("\nThe list using the sorted function:")
print(sorted(places))

# Print the list again to show it isn't modified
print("\nThe list again to show it hasn't been changed")
print(places)

# Print the sorted list in reverse
print("\nThe list sorted in reverse using the sorted function:")
print(sorted(places, reverse=True))

# Print the list again to show it isn't modified
print("\nThe list again to show it hasn't been changed")
print(places)

# Reverse the list
print("\nUse the reverse function to reverse the list:")
places.reverse()
print(places)

# Reestablish list
places = ["Japan", "Germany", "UK", "Canada", "Hawaii"]

# Remove the alphabetically first place
print("\nRemove the alphabetically first item from the list:")
places.remove(sorted(places)[0])
print(places)

# Sort the list
print("\nSort the list with the sort function:")
places.sort()
print(places)

# Reverse sort the list
print("\nSort the list in reverse with the sort function:")
places.sort(reverse=True)
print(places)