innovation = [
    {'technology': 'Internet',
     'innovator': 'Tim Berners-Lee'
    },
    {'technology': 'Telephone',
     'innovator': 'Graham Bell'
    },
    {'technology': 'Computer',
     'innovator': 'Charles Babbage'
    },
    {'technology': 'Light Bulb',
     'innovator': 'Thomas Edison'
    },
    {'technology': 'Operating System',
     'innovator': 'Ken Thompson and Dennis Ritchie'
    },
    {'technology': 'Electricity',
     'innovator': 'Nikola Tesla'
    },
    {'technology': 'Airplane',
     'innovator': 'Wright Brothers'
    },
    {'technology': 'Blockchain',
     'innovator': 'Satoshi Nakamoto'
    }
]

print (innovation)

print ('4th technology innovator is: ', innovation[3]['innovator'])

innovation[1]['innovator'] = 'Alexander Graham Bell'
print (innovation)

innovation.pop(5)

print ('Last technology is: ', innovation[-1])