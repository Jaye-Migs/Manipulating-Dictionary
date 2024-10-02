car = [
    {'model': 'Toyota Camry',
     'engine': '2.5L I4 or 3.5L V6'
    },
    {'model': 'Honda Civic',
     'engine': '2.0L I4 or 1.5L Turbo I4'
    },
    {'model': 'Ford Mustang',
     'engine': '2.3L EcoBoost I4, 5.0L V8'
    },
    {'model': 'Chevrolet Silverado',
     'engine': '4.3L V6, 5.3L V8, 6.2L V8'
    },
    {'model': 'BMW 3 Series',
     'engine': '2.0L I4, 3.0L I6'
    },
    {'model': 'Mercedes-Benz C-Class',
     'engine': '2.0L I4, 3.0L V6'
    },
    {'model': 'Audi A4',
     'engine': '2.0L Turbo I4'
    },
    {'model': 'Nissan Altima',
     'engine': '2.5L I4 or 2.0L Turbo I4'
    },
    {'model': 'Subaru Outback',
     'engine': '2.5L I4'
    },
    {'model': 'Volkswagen Golf',
     'engine': '1.4L Turbo I4 or 2.0L Turbo I4'
    }
]

print (car)

print ('4th car specification is: ', car[3]['engine'])

car[8]['engine'] = '2.5L I4 or 2.4L Turbo I4'
print (car)

car.pop(4)

print ('Last car is: ', car[-1])