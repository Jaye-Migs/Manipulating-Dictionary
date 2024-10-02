progLanguages = [
    {'language' : 'Python',
     'developer' : 'Rossum'
    },
    {'language' : 'Java',
     'developer' : 'Gosling'
    },
    {'language' : 'C',
     'developer' : 'Ritchie'
    },
    {'language' : 'Ruby',
     'developer' : 'Matsumoto'
    },
    {'language' : 'JavaScript',
     'developer' : 'Eich'
    },
    {'language' : 'Swift',
     'developer' : 'Apple Inc'
    },
    {'language' : 'Go',
     'developer' : ['Griesemer', 'Pike', 'Thompson']
    }
    ]
print (progLanguages)

print (progLanguages[3])

progLanguages[5]['developer'] = 'Lattner'
print (progLanguages)

progLanguages.pop(1)

print (progLanguages[-1])