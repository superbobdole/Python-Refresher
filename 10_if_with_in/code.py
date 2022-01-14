movies_watched = {"the matrix", "green book", "her"}
user_movie = input("Enter something you've watched recently: ").lower()

if user_movie in movies_watched:
    print(f"I've watched {user_movie} too!")
else:
    print("I haven't watched that yet.")