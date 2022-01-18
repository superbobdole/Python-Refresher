def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor #instead of printing the result, use return
    else:
        return "Cannot divide by zero"
# Do not return two kinds of data (string/number) - can't do maths on the return value of a string very well

result = divide(15,3)
print(result)