sportEvent = [
    {'event': 'FIFA World Cup',
     'year': 2018
    },
    {'event': 'Summer Olympics',
     'year': 2021
    },
    {'event': 'Super Bowl',
     'year': 2023
    },
    {'event': 'Wimbledon',
     'year': 2022
    },
    {'event': 'NBA Finals',
     'year': 2021
    },
    {'event': 'Tour de France',
     'year': 2023
    },
    {'event': 'The Masters',
     'year': 2023
    }
]

print (sportEvent)

print ('3rd sport event date is: ', sportEvent[2]['year'])

sportEvent[5]['year'] = 2022
print (sportEvent)

sportEvent.pop(4)

print ('Last sport is: ', sportEvent[-1])