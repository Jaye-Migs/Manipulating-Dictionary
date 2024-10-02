festival = [
    {'festival': 'Rio Carnival',
     'location': 'Rio de Janeiro, Brazil'
    },
    {'festival': 'Diwali',
     'location': 'India'
    },
    {'festival': 'Oktoberfest',
     'location': 'Munich, Germany'
    },
    {'festival': 'Holi',
     'location': 'India'
    },
    {'festival': 'Mardi Gras',
     'location': 'New Orleans, USA'
    },
    {'festival': 'La Tomatina',
     'location': 'Buñol'
    },
    {'festival': 'Gion Matsuri',
     'location': 'Kyoto, Japan'
    },
    {'festival': 'Glastonbury Festival',
     'location': 'Pilton, England'
    }
]

print (festival)

print ('4th festival location is: ', festival[3]['location'])

festival[5]['location'] = 'Buñol, Spain'
print (festival)

festival.pop(1)

print ('Last festival is: ', festival[-1])