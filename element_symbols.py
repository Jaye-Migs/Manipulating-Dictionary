element = [
    {'element': 'Hydrogen',
     'symbol': 'H'
    },
    {'element': 'Helium',
     'symbol': 'He'
    },
    {'element': 'Lithium',
     'symbol': 'Li'
    },
    {'element': 'Beryllium',
     'symbol': 'Be'
    },
    {'element': 'Boron',
     'symbol': 'B'
    },
    {'element': 'Carbon',
     'symbol': 'C'
    },
    {'element': 'Nitrogen',
     'symbol': 'N'
    },
    {'element': 'Oxygen',
     'symbol': 'o'
    },
    {'element': 'Fluorine',
     'symbol': 'F'
    },
    {'element': 'Neon',
     'symbol': 'Ne'
    }
]

print (element)

print ('6th element symbol is: ', element[5]['symbol'])

element[7]['symbol'] = 'O'
print (element)

element.pop(8)

print ('Last element is: ', element[-1])