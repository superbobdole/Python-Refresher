size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_meters = square_feet / 10.8
# using :.2f formats the number to only display the first two decimal places
print(f"{square_feet} is equal to {square_meters:.2f} square meters")



#my attempt not using f string (working)
#longer_phrase = "{} Square feet is {} square meters"
#formatted = longer_phrase.format(square_feet, square_meters)
#print(formatted)