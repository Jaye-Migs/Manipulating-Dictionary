river = [
    {'river': 'Nile',
     'length_km': 6650
    },
    {'river': 'Amazon',
     'length_km': 6400
    },
    {'river': 'Yangtze',
     'length_km': 6300
    },
    {'river': 'Mississippi-Missouri',
     'length_km': 6275
    },
    {'river': 'Yenisei',
     'length_km': 5539
    },
    {'river': 'Yellow River (Huang He)',
     'length_km': 5464
    }
]

print (river)

print ('2nd river length in km is: ', river[1]['length_km'])

river[4]['length_km'] = '5540'
print (river)

river.pop(3)

print ('Last river is: ', river[-1])