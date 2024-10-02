softwares = [
    {'software': 'Microsoft Office',
     'version': 'Office 2021'
    },
    {'software': 'Adobe Photoshop',
     'version': 'Photoshop 2023'
    },
    {'software': 'Google Chrome',
     'version': 'Chrome 118.0'
    },
    {'software': 'Mozilla Firefox',
     'version': 'Firefox 118.0'
    },
    {'software': 'Visual Studio Code',
     'version': '1.84.0'
    },
    {'software': 'Zoom',
     'version': '5.16.0'
    }
]

print (softwares)

print ('4th software latest version is: ', softwares[3]['version'])

softwares[1]['version'] = 'Photoshop 2024'
print (softwares)

softwares.pop(4)

print ('Last software is: ', softwares[-1])