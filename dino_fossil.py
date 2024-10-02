fossil = [
    {'dinosaur': 'Tyrannosaurus rex',
     'location': 'North America (USA and Canada)'
    },
    {'dinosaur': 'Triceratops',
     'location': 'North America'
    },
    {'dinosaur': 'Velociraptor',
     'location': 'Central Asia (Mongolia and China)'
    },
    {'dinosaur': 'Stegosaurus',
     'location': 'North America (USA)'
    },
    {'dinosaur': 'Brachiosaurus',
     'location': 'North America (USA) and Africa (Tanzania)'
    },
    {'dinosaur': 'Spinosaurus',
     'location': 'North Africa (Egypt and Morocco)'
    },
    {'dinosaur': 'Diplodocus',
     'location': 'North America (USA)'
    }
]

print (fossil)

print ('4th dinosaur fossil location is: ', fossil[3]['location'])

fossil[1]['location'] = 'North America (USA and Canada)'
print (fossil)

fossil.pop(5)

print ('Last fossil is: ', fossil[-1])