friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
#takes friends set, and finds difference between abroad set
#empty set notation = set()
print(local_friends)