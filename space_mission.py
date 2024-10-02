from encodings.idna import sace_prefix

spaceMission = [
    {'mission': 'Apollo 11',
     'year': 1969
    },
    {'mission': 'Voyager 1',
     'year': 1976
    },
    {'mission': 'Hubble Space Telescope',
     'year': 1990
    },
    {'mission': 'Mars Rover Curiosity',
     'year': 2012
    },
    {'mission': 'New Horizons',
     'year': 2006
    }
]

print (spaceMission)

print ('3rd space mission date is: ', spaceMission[2]['year'])

spaceMission[1]['year'] = '1977'
print (spaceMission)

spaceMission.pop(3)

print ('Last space mission is: ', spaceMission[-1])