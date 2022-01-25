def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")

    return dividend / divisor

grades = []

print("Welcome to grade program")
try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:  # "as e" to assign the value of an error to a variable
    print(e)
    print("there are no grades yet in your list.")
else:
    print(f"The average grade is {average}.")
finally:
    print("thanks")