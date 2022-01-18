#positional arguments are listed in an order
def  say_hello(name, surname):
    print(f"Hello!, {name}, {surname}")

#the function is defined, but not called

say_hello("Bob", "Smith")

#key word or named arguments have to specified

say_hello(surname="Bob", name="Smith")