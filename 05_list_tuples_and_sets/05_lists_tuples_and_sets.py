l = ["Bob", "Rolf", "Anne"] # lists and tuples keep the order
t = ("Bob", "Rolf", "Anne") # tuples cannot be modified
s = {"Bob", "Rolf", "Anne"} # sets cannot have duplicate entries

# accessing individual elements of a list or tuple
print(l[0])
print(l[1])
print(l[2])
# sets cannot use subscript notation to select individual element

l.append("Smith")
print(l[3])

l.remove("Bob")
print(l)

s.add("dick")
print(s)

# single value tuple
# my_tuple = (15,)
# or
# my_tuple = 15,