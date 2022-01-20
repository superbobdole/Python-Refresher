class Student:
    def __init__(self, name, grades): # when a function is inside of a class, it's called a method
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Bob", (100, 100, 93, 78, 90))
student = Student("Rolf", (100, 100, 93, 78, 90))
print(student.name)
print(student.average_grade())
student = Student("Rolf", (100, 100, 93, 78, 90))
print(student.name)
print(student.average_grade())