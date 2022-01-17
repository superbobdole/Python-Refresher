friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(f"Friends {friends}")

#access index one

print(friends[1]["name"])
print("=====")
#access all keys
student_attendance = {"rolf": 96, "bob": 80, "anne": 100}


for student in student_attendance:#not a great way to do this??
    print(f"{student}: {student_attendance[student]}")
print("=====")
#better way
for student, attend in student_attendance.items():
    print(f"{student}: {student_attendance[student]}")
    