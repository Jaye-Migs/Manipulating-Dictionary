athlete = [
    {'athlete': 'Usain Bolt',
     'achievement': '8-time Olympic gold medalist and world record holder in 100m and 200m'
    },
    {'athlete': 'Michael Phelps',
     'achievement': '23-time Olympic gold medalist, most decorated Olympian of all time'
    },
    {'athlete': 'Serena Williams',
     'achievement': '23 Grand Slam singles titles'
    },
    {'athlete': 'Lionel Messi',
     'achievement': '7-time Ballon d\'Or winner and 2021 Copa America champion'
    },
    {'athlete': 'Muhammad Ali',
     'achievement': '3-time world heavyweight champion and Olympic gold medalist'
    },
    {'athlete': 'Tom Brady',
     'achievement': '7-time Super Bowl champion and 5-time Super Bowl MVP'
    },
    {'athlete': 'Roger Federer',
     'achievement': '20 Grand Slam singles titles and held the world No. 1 ranking for 310 weeks'
    },
    {'athlete': 'Michael Jordan',
     'achievement': '6-time NBA champion and 5-time NBA MVP'
    }
]

print (athlete)

print ('5th athlete\'s achievement is: ', athlete[4]['achievement'])

athlete[2]['achievement'] = '23 Grand Slam singles titles, 4 Olympic gold medals'
print (athlete)

athlete.pop(6)

print ('Last athlete is: ', athlete[-1])