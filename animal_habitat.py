animal = [
    {'animal': 'African Elephant',
     'habitat': 'Savannahs, forests, and grasslands'
    },
    {'animal': 'Polar Bear',
     'habitat': 'Arctic regions and sea ice'
    },
    {'animal': 'Bengal Tiger',
     'habitat': 'Tropical forests, grasslands, and mangroves'
    },
    {'animal': 'Great Barrier Reef Coral',
     'habitat': 'Coral reefs in warm, shallow ocean waters'
    },
    {'animal': 'Panda',
     'habitat': 'Bamboo forests'
    },
    {'animal': 'Koala',
     'habitat': 'Eucalyptus forests'
    },
    {'animal': 'Red Fox',
     'habitat': 'Forests, grasslands, and urban areas'
    },
    {'animal': 'Emperor Penguin',
     'habitat': 'Antarctic ice and surrounding waters'
    }
]

print (animal)

print ('3rd animal habitat is: ', animal[2]['habitat'])

animal[4]['habitat'] = 'Mountainous Regions'
print (animal)

animal.pop(6)

print ('Last animal is: ', animal[-1])