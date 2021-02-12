fav_nums = {"Luke": [7,42,2], "Carl": [4,5], "Ryan": 15, "Ben": 1, "John": [0,0]}

for name in fav_nums:
    print(f"{name}'s Favorite number(s) is/are {str(fav_nums[name]).strip('[]')}")