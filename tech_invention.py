inventions = [
    {'technology': 'Telephone',
     'inventor': 'Alexander Graham Bell'
    },
    {'technology': 'Light Bulb',
     'inventor': 'Thomas Edison'
    },
    {'technology': 'Computer',
     'inventor': 'Charles Babbage'
    },
    {'technology': 'Internet',
     'inventor': 'Tim Berners-Lee'
    },
    {'technology': 'Airplane',
     'inventor': 'Wright Brothers'
    },
    {'technology': 'Vaccination',
     'inventor': 'Edward Jenner'
    }
]

print (inventions)

print ('4th technology inventor is: ', inventions[3]['inventor'])

inventions[1]['inventor'] = 'Nikola Tesla'
print (inventions)

inventions.pop(5)

print ('Last technology is: ', inventions[-1])