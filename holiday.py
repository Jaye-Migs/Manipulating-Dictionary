holiday = [
    {'holiday': 'New Year\'s Day',
     'date': 'January 1'
    },
    {'holiday': 'Valentine\'s Day',
     'date': 'February 14'
    },
    {'holiday': 'Independence Day',
     'date': 'July 4'
    },
    {'holiday': 'Halloween',
     'date': 'October 31'
    },
    {'holiday': 'Thanksgiving',
     'date': 'Fourth Thursday in November'
    },
    {'holiday': 'Christmas',
     'date': 'December 25'
    },
    {'holiday': 'Easter',
     'date': 'Date varies (between March 22 and April 25)'
    },
    {'holiday': 'Labor Day',
     'date': 'First Monday in September'
    },
    {'holiday': 'Memorial Day',
     'date': 'May'
    },
    {'holiday': 'Veterans Day',
     'date': 'November 11'
    }
]

print (holiday)

print ('4th holiday date is: ', holiday[3]['date'])

holiday[8]['date'] = 'last Monday in May'
print (holiday)

holiday.pop(1)

print ('Last holiday is: ', holiday[-1])