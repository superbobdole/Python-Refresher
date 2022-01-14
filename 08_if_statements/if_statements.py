# elif creates a second if branch
# if the if statement is hit, the elif and else statements are ignored
# .lower() formats user input to lowercase
# when using .lower() strings should all be in lower case

day_of_week = input("What day of the week is it today? ").lower()

if day_of_week == "monday":
    print("I hate Mondays")
elif day_of_week == "tuesday":
    print("Tuesday sucks")
else:
    print("cool")

print("This code always runs.")