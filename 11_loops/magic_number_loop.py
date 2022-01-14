number = 7

while user_input != "n":
    user_input = input("Would you like to play? (Y/n) ").lower()

    if user_input == "n"
        break

    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif number - user_number in (1, -1):
        print("You were off by 1")
    else:
        print("Sorry, it's wrong!")

    user_input = input("Would you like to play? (Y/n) ").lower()