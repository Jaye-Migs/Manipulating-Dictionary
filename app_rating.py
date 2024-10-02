app = [
    {'app': 'WhatsApp',
     'rating': 4.7
    },
    {'app': 'Spotify',
     'rating': 4.5
    },
    {'app': 'Instagram',
     'rating': 4.6
    },
    {'app': 'TikTok',
     'rating': 4.8
    },
    {'app': 'Google Maps',
     'rating': 4.8
    },
    {'app': 'Facebook',
     'rating': 4.1
    },
    {'app': 'Snapchat',
     'rating': 4.3
    },
    {'app': 'YouTube',
     'rating': 4.5
    },
    {'app': 'Twitter',
     'rating': 4.4
    },
    {'app': 'Microsoft Teams',
     'rating': 4.5
    }
]

print (app)

print ('6th app rating is: ', app[5]['rating'])

app[7]['rating'] = 3.0
print (app)

app.pop(8)

print ('Last app is: ', app[-1])