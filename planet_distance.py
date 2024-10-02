planet = [
    {'planet': 'Mercury',
     'distance': '57.91 million km'
    },
    {'planet': 'Venus',
     'distance': '108.2 million km'
    },
    {'planet': 'Earth',
     'distance': '149.6 million km'
    },
    {'planet': 'Mars',
     'distance': '227.9 million km'
    },
    {'planet': 'Jupiter',
     'distance': '778.5 million km'
    },
    {'planet': 'Saturn',
     'distance': '1.434 billion km'
    },
    {'planet': 'Uranus',
     'distance': '2.871 billion km'
    },
    {'planet': 'Neptune',
     'distance': '4.495 billion km'
    }
]

print (planet)

print ('3rd planet distance from sun is: ', planet[2]['distance'])

planet[4]['distance'] = '779 million km'
print (planet)

planet.pop(6)

print ('Last planet is: ', planet[-1])