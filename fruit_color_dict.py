fruitColor = [
    {'fruit': 'Apple',
     'color': 'Red'},
    {'fruit': 'Banana',
     'color': 'Yellow'},
    {'fruit': 'Grapes',
     'color': 'Green'},
    {'fruit': 'Orange',
     'color': 'Orange'},
    {'fruit': 'Blueberry',
     'color': 'Blue'},
    {'fruit': 'Kiwi',
     'color': 'Brown'},
    {'fruit': 'Strawberry',
     'color': 'Red'},
    {'fruit': 'Pineapple',
     'color': 'Yellow'}
]

print (fruitColor)

print (fruitColor[5])

fruitColor[3]['color'] = 'Pumpkin'
print (fruitColor)

fruitColor.pop(6)

print (fruitColor[-1])