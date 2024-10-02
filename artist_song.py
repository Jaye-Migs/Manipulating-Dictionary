artist = [
    {'artist': 'Taylor Swift',
     'song': 'Blank Space'
    },
    {'artist': 'Ed Sheeran',
     'song': 'Shape of You'
    },
    {'artist': 'Adele',
     'song': 'Rolling in the Deep'
    },
    {'artist': 'Drake',
     'song': 'God\'s Plan'
    },
    {'artist': 'Beyoncé',
     'song': 'Crazy in Love'
    },
    {'artist': 'The Weeknd',
     'song': 'Blinding Lights'
    },
    {'artist': 'Bruno Mars',
     'song': 'Uptown Funk'
    },
    {'artist': 'Billie Eilish',
     'song': 'Bad Guy'
    }
]

print (artist)

print ('3rd artist top song is: ', artist[2]['song'])

artist[5]['song'] = 'Starboy'
print (artist)

artist.pop(6)

print ('Last artist is: ', artist[-1])