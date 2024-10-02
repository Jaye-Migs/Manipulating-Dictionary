flower = [
    {'flower': 'Rose',
     'meaning': 'Love and passion'
    },
    {'flower': 'Lily',
     'meaning': 'Purity and renewal'
    },
    {'flower': 'Sunflower',
     'meaning': 'Adoration and loyalty'
    },
    {'flower': 'Tulip',
     'meaning': 'Perfect love'
    },
    {'flower': 'Cherry Blossom',
     'meaning': 'Transience and beauty'
    },
    {'flower': 'Orchid',
     'meaning': 'Luxury and strength'
    },
    {'flower': 'Daisy',
     'meaning': 'Purity'
    },
    {'flower': 'Peony',
     'meaning': 'Romance and prosperity'
    }
]

print (flower)

print ('5th flower meaning is: ', flower[4]['meaning'])

flower[6]['meaning'] = 'Innocence and purity'
print (flower)

flower.pop(5)

print ('Last flower is: ', flower[-1])