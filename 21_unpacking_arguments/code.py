def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1,3,5))


# using a list
def add(x, y):
    return x + y

nums = [3,5]
print(add(*nums))
# by using a '*' python knows to assign each variable to an item on the list
# without the '*' python will assign the entire list to the first variable

#using a dictionary
dic = {"x": 15, "y": 25}
print(add(**dic))

#multiply
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."

print(apply(1,3,6,7,operator="*"))