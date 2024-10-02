movieGenre = [
    {'genre': 'Action',
     'movie': 'Mad Max: Fury Road'
    },
    {'genre': 'Comedy',
     'movie': 'Superbad'
    },
    {'genre': 'Drama',
     'movie': 'The Shawshank Redemption'
    },
    {'genre': 'Horror',
     'movie': 'Get Out'
    },
    {'genre': 'Science Fiction',
     'movie': 'Inception'
    },
    {'genre': 'Fantasy',
     'movie': 'The Lord of the Rings: The Fellowship of the Ring'
    },
    {'genre': 'Romance',
     'movie': 'The Notebook'
    },
    {'genre': 'Thriller',
     'movie': 'Gone Girl'
    }
]

print (movieGenre)

print ('3rd genre example is: ', movieGenre[2]['movie'])

movieGenre[4]['movie'] = 'IT'
print (movieGenre)

movieGenre.pop(6)

print ('Last genre is: ', movieGenre[-1])