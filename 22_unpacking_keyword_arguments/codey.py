def starstar(**kwargs):
    print(kwargs)
# '**' collects keyword arguments

starstar(name="Bob", age=25)
# using the named function stores the keyword arguments and stores them in a dictionary

def named(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
# use unpacking to pass dictonary items to a named key
named(**details)

