#Bad idea: duplicating the name of a function
def print():
    print("Hello world!")
print()

#Self reference function - # can't use "friends" to create a function of friends

friends = ["Rolf", "Bob"]

def add_friends():
    friend_name = input("Enter your friends name: ")
    friends = friends + [friend_name]

add_friend()

# cant use functions before they are defined