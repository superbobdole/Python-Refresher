#def add(x, y):
#    return x + y
# or
#
add = lambda x, y: x + y
# lambda functions automatically return the function
# you can name the lambda function by assigning it a variable
# if you don't name the lambda the function returns (and completes) in that line
print(add(5, 7))
# to use, surround by brackets, then call the function on the same line
print((lambda x, y: x + y)(5 ,7))