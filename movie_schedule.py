current_movies = {'The Lord of the Rings': '11:00am',
                  'Spiderman': '1:00pm',
                  'Matrix II': '3:00pm',
                  'Eyes Wide Shot': '10:00pm'}

print("We're currently showing the following movies:")
for movie in current_movies:
    print(movie)

movie = input('What movie would you like the showtime for?\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("Requested showtime isn't playing")
else:
    print(movie, 'is playing at', showtime)