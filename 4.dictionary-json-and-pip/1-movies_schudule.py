current_movies = {
    'The Grinch' : '11:00pm',
    'Rudolph': '1:00pm',
    'Frosty the Snowman': '3:00pm'
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input('Which movie would you like the showtime ?\n')

showtime = current_movies.get(movie)

if not showtime:
    print("Requested movie isn't playing !!!")
else:
    print(movie, 'is playing at',showtime)