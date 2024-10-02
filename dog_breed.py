dog = [
    {'breed': 'Chihuahua',
     'size': 'Small'
    },
    {'breed': 'Beagle',
     'size': 'Medium'
    },
    {'breed': 'Labrador Retriever',
     'size': 'Large'
    },
    {'breed': 'Poodle (Toy)',
     'size': 'Small'
    },
    {'breed': 'Bulldog',
     'size': 'Medium'
    },
    {'breed': 'German Shepherd',
     'size': 'Large'
    },
    {'breed': 'Corgi',
     'size': 'Medium'
    },
    {'breed': 'Siberian Husky',
     'size': 'Medium'
    },
    {'breed': 'Yorkshire Terrier',
     'size': 'Small'
    },
    {'breed': 'Golden Retriever',
     'size': 'Large'
    }
]

print (dog)

print ('5th dog breed size is: ', dog[4]['size'])

dog[7]['size'] = 'Large'
print (dog)

dog.pop(5)

print ('Last dog is: ', dog[-1])