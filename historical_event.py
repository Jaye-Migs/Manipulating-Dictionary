event = [
    {'event': 'The Signing of the Declaration of Independence',
     'year': 1776
    },
    {'event': 'The French Revolution',
     'year': 1789
    },
    {'event': 'The American Civil War',
     'year': 1861
    },
    {'event': 'World War I',
     'year': 1914
    },
    {'event': 'The Great Depression',
     'year': 1929
    },
    {'event': 'World War II',
     'year': 1939
    },
    {'event': 'The Moon Landing',
     'year': 1969
    },
    {'event': 'The Fall of the Berlin Wall',
     'year': 1989
    }
]

print (event)

print ('2nd event date is: ', event[1]['year'])

event[6]['year'] = 1970
print (event)

event.pop(4)

print ('Last event is: ', event[-1])