student_attendance = {"rolf": 96, "bob": 80, "anne": 100}

if "bob" in student_attendance:
    print(f"Bob: {student_attendance['bob']}")
else:
    print("Bob is not a student in this class.")

#calculate an average

for student, attedance in student_attendance.items():
    print(f"{student}: {attedance}")