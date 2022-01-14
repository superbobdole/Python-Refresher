number = 7
user_input = input("enter 'y' if you want to play: ").lower() #change the users input into lowercase

#using 'in' instead of '==' allows use of a tuple or list
if user_input in ("y", "Y"):
    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1): #reducing the user_input by number. if the difference is 1, or -1 the user gets a hint
                                          #can also add abs(number - usernumber) creates absolute number - ends the need to include negative numbers
        print("You were off by 1")
    else:
        print("Sorry, it's wrong!")

Y