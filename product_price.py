product = [
    {'product': 'Smartphone',
     'pesos': 25000
    },
    {'product': 'Laptop',
     'pesos': 50000
    },
    {'product': 'Washing Machine',
     'pesos': 20000
    },
    {'product': 'Refrigerator',
     'pesos': 30000
    },
    {'product': 'Television',
     'pesos': 40000
    },
    {'product': 'Air Conditioner',
     'pesos': 35000
    },
    {'product': 'Microwave Oven',
     'pesos': 5000
    },
    {'product': 'Electric Kettle',
     'pesos': 1500
    },
    {'product': 'Headphones',
     'pesos': 2500
    },
    {'product': 'Bluetooth Speaker',
     'pesos': 3500
    }
]

print (product)

print ('4th product price in pesos is: ', product[3]['pesos'])

product[8]['pesos'] = 3000
print (product)

product.pop(5)

print ('Last product is: ', product[-1])