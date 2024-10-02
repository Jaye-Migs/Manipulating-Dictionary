city = [
    {'city': 'Paris',
     'landmark': 'Eiffel Tower'
    },
    {'city': 'New York',
     'landmark': 'Statue of Liberty'
    },
    {'city': 'London',
     'landmark': 'Big Ben'
    },
    {'city': 'Rome',
     'landmark': 'Colosseum'
    },
    {'city': 'Sydney',
     'landmark': 'Sydney Opera House'
    },
    {'city': 'Cairo',
     'landmark': 'Pyramids of Giza'
    },
    {'city': 'Beijing',
     'landmark': 'Great Wall of China'
    },
    {'city': 'Agra',
     'landmark': 'Taj Mahal'
    }
]

print (city)

print ('6th city landmark is: ', city[5]['landmark'])

city[1]['landmark'] = 'Empire State Building'
print (city)

city.pop(6)

print ('Last city is: ', city[-1])