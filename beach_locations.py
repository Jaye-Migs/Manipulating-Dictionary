beaches = [
    {'beach': 'Whitehaven Beach',
     'country': 'Australia'
    },
    {'beach': 'Maya Bay',
     'country': 'Thailand'
    },
    {'beach': 'Copacabana Beach',
     'country': 'Brazil'
    },
    {'beach': 'Waikiki Beach',
     'country': 'USA'
    },
    {'beach': 'Anse Source d\'Argent',
     'country': 'Seychelles'
    },
    {'beach': 'Bora Bora',
     'country': 'Polynesia'
    },
    {'beach': 'Kuta Beach',
     'country': 'Indonesia'
    },
    {'beach': 'Bondi Beach',
     'country': 'Australia'
    }
]

print (beaches)

print ('3rd beach location is: ', beaches[2]['country'])

beaches[5]['country'] = 'French Polynesia'
print (beaches)

beaches.pop(4)

print ('Last beach is: ', beaches[-1])