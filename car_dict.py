car = [
    {'car' : 'Toyota',
     'origin' : 'Japan'
    },
    {'car' : 'Ford',
     'origin' : 'US'
    },
    {'car' : 'BMW',
     'origin' : 'Germany'
    },
    {'car' : 'Ferrari',
     'origin' : 'Italy'
    },
    {'car' : 'Hyundai',
     'origin' : 'South Korea'
    },
    {'car' : 'Renault',
     'origin' : 'France'
    },
    {'car' : 'Volvo',
     'origin' : 'Sweden'
    },
    {'car' : 'Volkswagen',
     'origin' : 'Germany'
    },
    {'car' : 'Fiat',
     'origin' : 'Italy'
    },
    {'car' : 'Chevrolet',
     'origin' : 'US'
    }
    ]
print (car)

print (car[2])

car[6]['origin'] = 'Gothenburg'
print (car)

car.pop(7)

print (car[-1])