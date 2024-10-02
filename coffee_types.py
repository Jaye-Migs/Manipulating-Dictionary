coffee = [
    {'coffee': 'Espresso',
     'description': 'Strong, concentrated coffee made by forcing hot water through finely-ground beans.'
    },
    {'coffee': 'Latte',
     'description': 'Espresso with steamed milk and a small amount of milk foam.'
    },
    {'coffee': 'Cappuccino',
     'description': 'Espresso with steamed milk and thick milk foam, often topped with cocoa.'
    },
    {'coffee': 'Americano',
     'description': 'Espresso diluted with hot water, similar strength to drip coffee.'
    },
    {'coffee': 'Macchiato',
     'description': 'Espresso with a small amount of steamed milk or foam.'
    },
    {'coffee': 'Mocha',
     'description': 'Espresso with steamed milk and chocolate syrup, topped with whipped cream.'
    },
    {'coffee': 'Flat White',
     'description': 'Espresso with steamed milk and velvety microfoam, higher coffee-to-milk ratio.'
    },
    {'coffee': 'Cortado',
     'description': 'Espresso cut with equal amount of warm milk.'
    },
    {'coffee': 'Ristretto',
     'description': 'Short shot of espresso, more concentrated and less bitter.'
    },
    {'coffee': 'Affogato',
     'description': 'Hot espresso poured over a scoop of vanilla ice cream or gelato.'
    }
]

print (coffee)

print ('4th coffee description is: ', coffee[3]['description'])

coffee[7]['description'] = 'Espresso cut with equal amount of warm milk, balanced flavor.'
print (coffee)

coffee.pop(4)

print ('Last coffee is: ', coffee[-1])