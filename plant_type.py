plant = [
    {'plant': 'Rose',
     'type': 'Shrub'
    },
    {'plant': 'Oak',
     'type': 'Shrub'
    },
    {'plant': 'Basil',
     'type': 'Herb'
    },
    {'plant': 'Lavender',
     'type': 'Herb'
    },
    {'plant': 'Maple',
     'type': 'Tree'
    },
    {'plant': 'Hibiscus',
     'type': 'Shrub'
    },
    {'plant': 'Mint',
     'type': 'Herb'
    },
    {'plant': 'Pine',
     'type': 'Tree'
    }
]

print (plant)

print ('5th plant type is: ', plant[4]['type'])

plant[1]['type'] = 'Tree'
print (plant)

plant.pop(5)

print ('Last plant is: ', plant[-1])