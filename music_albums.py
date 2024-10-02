album = [
    {'album': 'Thriller',
     'release': 1982
    },
    {'album': 'The Dark Side of the Moon',
     'release': 1973
    },
    {'album': 'Abbey Road',
     'release': 1969
    },
    {'album': 'Back in Black',
     'release': 1980
    },
    {'album': 'Rumours',
     'release': 1977
    },
    {'album': 'Nevermind',
     'release': 1991
    },
    {'album': 'Hotel California',
     'release': 1976
    },
    {'album': '21',
     'release': 2010
    },
    {'album': 'The Wall',
     'release': 1979
    },
    {'album': 'Born to Run',
     'release': 1975
    }
]

print (album)

print ('3rd album release date is: ', album[2]['release'])

album[7]['year'] = '2011'
print (album)

album.pop(4)

print ('Last album is: ', album[-1])