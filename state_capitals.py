state = [
    {'state': 'California',
     'capital': 'Sacramento'
    },
    {'state': 'Texas',
     'capital': 'Austin'
    },
    {'state': 'Florida',
     'capital': 'Tallahassee'
    },
    {'state': 'New York',
     'capital': 'Albany'
    },
    {'state': 'Illinois',
     'capital': 'Springfield'
    },
    {'state': 'Pennsylvania',
     'capital': 'Harrisburg'
    },
    {'state': 'Ohio',
     'capital': 'Columbus'
    },
    {'state': 'Georgia',
     'capital': 'Augusta'
    },
    {'state': 'Michigan',
     'capital': 'Lansing'
    },
    {'state': 'Arizona',
     'capital': 'Phoenix'
    }
]

print (state)

print ('4th state capital is: ', state[3]['capital'])

state[8]['capital'] = 'Atlanta'
print (state)

state.pop(6)

print ('Last state is: ', state[-1])