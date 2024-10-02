festival = [
    {'festival': 'New Year\'s Day',
     'date': 'January 1'
    },
    {'festival': 'Valentine\'s Day',
     'date': 'February 14'
    },
    {'festival': 'Holi',
     'date': 'Usually march'
    },
    {'festival': 'Eid al-Fitr',
     'date': 'Date varies (based on lunar calendar) - usually falls after Ramadan'
    },
    {'festival': 'Independence Day (USA)',
     'date': 'July 4'
    },
    {'festival': 'Diwali',
     'date': 'Date varies (October or November) - usually in October or November'
    },
    {'festival': 'Thanksgiving',
     'date': 'October'
    },
    {'festival': 'Christmas',
     'date': 'December 25'
    },
    {'festival': 'Oktoberfest',
     'date': 'September to October (typically late September to the first weekend in October)'
    },
    {'festival': 'Mardi Gras',
     'date': 'Date varies (February or March) - day before Ash Wednesday'
    }
]

print (festival)

print ('3rd festival date is: ', festival[2]['date'])

festival[6]['date'] = 'Fourth Thursday in November'
print (festival)

festival.pop(4)

print ('Last festival is: ', festival[-1])