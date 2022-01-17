friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Adam"])
# you cannot call a number in dictionaries, you have to call the key
friend_ages["Bob"] = 43 # add an entry
# - ["Bob"] is subscript notation

print(f"Friends Ages: {friend_ages}")

# edit an entry

friend_ages["Adam"] = 69

print(f"Friends Ages -Edited-: {friend_ages}")