x, y = 5, 11 #tuples do not requrie brackets

student_attendance = {"rolf": 96, "bob": 80, "anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

people = [("Bob", 42, "mechanic"), ("James", 24, "artist"), ("harry", 32, "lecturer")] # a tuple of three values

for name, age, profession, in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# a single tuple

person = ("Bob", 42, "mechanic")
name, _, profession = person

print(name, profession)

#splitting a list

head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
