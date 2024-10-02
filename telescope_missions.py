telescope = [
    {'telescope': 'Hubble Space Telescope',
     'mission': 'To observe distant stars, galaxies, and other celestial objects'
    },
    {'telescope': 'James Webb Space Telescope',
     'mission': 'To study the formation of stars and planets, and to observe the most distant objects in the universe in infrared light'
    },
    {'telescope': 'Chandra X-ray Observatory',
     'mission': 'To observe X-rays from high-energy regions of the universe, such as the remnants of exploded stars'
    },
    {'telescope': 'Spitzer Space Telescope',
     'mission': 'To observe the universe in infrared light, focusing on distant galaxies, young stars, and forming planetary systems'
    },
    {'telescope': 'Kepler Space Telescope',
     'mission': 'To discover Earth-like planets orbiting other stars in the Milky Way by detecting their transits across their host stars'
    }
]

print (telescope)

print ('3rd telescope mission is: ', telescope[2]['mission'])

telescope[0]['mission'] = 'To observe distant stars, galaxies, and other celestial objects in visible, ultraviolet, and near-infrared light'
print (telescope)

telescope.pop(3)

print ('Last telescope is: ', telescope[-1])