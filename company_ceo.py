ceo = [
    {'company': 'Apple Inc.',
     'ceo': 'Tim Cook'
    },
    {'company': 'Microsoft',
     'ceo': 'Satya Nadella'
    },
    {'company': 'Amazon',
     'ceo': 'Jeff Bezos'
    },
    {'company': 'Google (Alphabet Inc.)',
     'ceo': 'Sundar Pichai'
    },
    {'company': 'Tesla, Inc.',
     'ceo': 'Elon Musk'
    },
    {'company': 'Facebook (Meta Platforms, Inc.)',
     'ceo': 'Mark Zuckerberg'
    },
    {'company': 'Berkshire Hathaway',
     'ceo': 'Warren Buffett'
    },
    {'company': 'Coca-Cola',
     'ceo': 'James Quincey'
    },
    {'company': 'IBM',
     'ceo': 'Arvind Krishna'
    },
    {'company': 'Netflix',
     'ceo': 'Ted Sarandos'
    }
]

print (ceo)

print ('6th company ceo is: ', ceo[5]['ceo'])

ceo[2]['ceo'] = 'Andy Jassy'
print (ceo)

ceo.pop(8)

print ('Last company is: ', ceo[-1])