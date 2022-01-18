def add(x, y=8): #since x does not have a value here, it is a non default value.
    # a non default value must be filled in later
    # y is an default value
    # a default value must not proceed a non-default
    # (x=2, y) will not work
    print(x + y)

add(5)

#you can overwrite the y value later on
add(5,2)