videogame = [
    {'game': 'The Legend of Zelda: Breath of the Wild',
     'platforms': ['Nintendo Switch', 'Wii U']
    },
    {'game': 'The Last of Us Part II',
     'platforms': ['PlayStation 4']
    },
    {'game': 'Minecraft',
     'platforms': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Mobile']
    },
    {'game': 'Call of Duty: Warzone',
     'platforms': ['PC', 'PlayStation', 'Xbox']
    },
    {'game': 'Fortnite',
     'platforms': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch', 'Mobile']
    },
    {'game': 'Animal Crossing: New Horizons',
     'platforms': ['Nintendo Switch']
    },
    {'game': 'Overwatch',
     'platforms': ['PC', 'PlayStation', 'Xbox', 'Nintendo Switch']
    },
    {'game': 'God of War',
     'platforms': ['PlayStation 4', 'PC']
    }
]

print (videogame)

print ('2nd videogame platform is: ', videogame[1]['platforms'])

videogame[5]['platforms'] = 'Steam Deck'
print (videogame)

videogame.pop(3)

print ('Last videogame is: ', videogame[-1])