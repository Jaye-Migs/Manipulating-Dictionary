continent = [
    {'continent': 'Africa',
     'country': 'Nigeria'
    },
    {'continent': 'Asia',
     'country': 'Japan'
    },
    {'continent': 'Europe',
     'country': 'France'
    },
    {'continent': 'North America',
     'country': 'Canada'
    },
    {'continent': 'Oceania',
     'country': 'Australia'
    },
    {'continent': 'South America',
     'country': 'Brazil'
    }
]

print (continent)

print ('4th continent country is: ', continent[3]['country'])

continent[4]['country'] = 'Fiji'
print (continent)

continent.pop(5)

print ('Last continent is: ', continent[-1])