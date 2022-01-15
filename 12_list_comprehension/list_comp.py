numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
# taking values from numbers, doubling them and adding them to the doubled list

print(f"Doubled numbers: {doubled}")

#===========

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("S")]

# for loop style
# friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# starts_s = []
# for friend in friends:
#   if friend.startswith("S"):
#       starts_s.append(friend)
#
print(f"Friends name's that start with S: {starts_s}")