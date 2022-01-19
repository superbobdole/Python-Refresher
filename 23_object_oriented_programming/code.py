class Student:
    def __init__(self): # when a function is inside of a class, it's called a method
        self.name = "Rolf"
        self.grades = (90, 90, 93, 78, 90)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()
print(student.name)
print(student.average_grade())