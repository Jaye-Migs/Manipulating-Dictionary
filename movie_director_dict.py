movies = [
    {'movie': 'Inception', 
     'director': 'Christopher Nolan'},
    {'movie': 'The Godfather', 
     'director': 'Francis Ford Coppola'},
    {'movie': 'Pulp Fiction', 
     'director': 'Quentin Tarantino'},
    {'movie': 'The Shawshank Redemption', 
     'director': 'Frank Darabont'},
    {'movie': 'The Dark Knight', 
     'director': 'Christopher Nolan'},
    {'movie': 'Fight Club', 
     'director': 'David Fincher'},
    {'movie': 'Forrest Gump', 
     'director': 'Robert Zemeckis'},
    {'movie': 'The Matrix', 
     'director': 'Lana and Lilly'},
    {'movie': 'Interstellar', 
     'director': 'Chris Nolan'},
    {'movie': 'The Lord of the Rings: The Return of the King', 
     'director': 'Peter Jackson'}
]

print (movies)

print ('5th movie Director is: ', movies[4]['director'])

movies[8]['director'] = 'Christopher Nolan'
print (movies)

movies.pop(6)

print ('Last Movie is: ', movies[-1])