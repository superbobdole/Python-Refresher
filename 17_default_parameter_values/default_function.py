#can't edit a value later if it's set as a default variable
default_y = 3

def add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)

#reassigning the variable doesn't work for the function
default_y = 4
add(2)