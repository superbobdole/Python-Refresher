class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # magic method is called when you want to change your object into a string
        # str method is more common
        return f"Person {self.name}, {self.age} years old."

    def __repr__(self):
        # repr is called when you want a copy of the output for programming
        return f"<Person{self.name}, {self.age}"



bob = Person("Bob", 35)
print(bob)

