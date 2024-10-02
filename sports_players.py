sports = [
    {'sport': 'Soccer',
     'player': 'Lionel Messi'},
    {'sport': 'Basketball',
     'player': 'Michael Jordan'},
    {'sport': 'Tennis',
     'player': 'Serena Williams'},
    {'sport': 'Cricket',
     'player': 'Sachin Tendulkar'},
    {'sport': 'American Football',
     'player': 'Tom Brady'},
    {'sport': 'Golf',
     'player': 'Tiger Woods'},
    {'sport': 'Baseball',
     'player': 'Babe Ruth'},
    {'sport': 'Ice Hockey',
     'player': 'Wayne Gretzky'},
    {'sport': 'Formula 1',
     'player': 'Lewis Hamilton'},
    {'sport': 'Rugby',
     'player': 'Jonah Lomu'}
]

print (sports)

print ('4th sport player is: ', sports[3]['player'])

sports[5]['player'] = 'Greg Norman'
print (sports)

sports.pop(9)

print ('Last sport is: ', sports[-1])