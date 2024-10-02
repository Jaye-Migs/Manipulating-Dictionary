currency = [
    {'currency': 'United States Dollar',
     'symbol': '$'
    },
    {'currency': 'Euro',
     'symbol': '€'
    },
    {'currency': 'British Pound Sterling',
     'symbol': '£'
    },
    {'currency': 'Japanese Yen',
     'symbol': '¥'
    },
    {'currency': 'Swiss Franc',
     'symbol': 'CHF'
    },
    {'currency': 'Canadian Dollar',
     'symbol': 'C$'
    },
    {'currency': 'Australian Dollar',
     'symbol': 'A$'
    },
    {'currency': 'Chinese Yuan',
     'symbol': '¥'
    },
    {'currency': 'Indian Rupee',
     'symbol': 'INR'
    },
    {'currency': 'Brazilian Real',
     'symbol': 'R$'
    }
]

print (currency)

print ('5th currency symbol is: ', currency[4]['symbol'])

currency[8]['symbol'] = '₹'
print (currency)

currency.pop(2)

print ('Last currency is: ', currency[-1])