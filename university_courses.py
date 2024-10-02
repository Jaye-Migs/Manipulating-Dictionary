uni = [
    {'university': 'Harvard University',
     'popular_courses': ['Computer Science', 'Business Administration', 'Law']
    },
    {'university': 'Stanford University',
     'popular_courses': ['Engineering', 'Biological Sciences', 'Business']
    },
    {'university': 'Massachusetts Institute of Technology (MIT)',
     'popular_courses': ['Engineering', 'Computer Science', 'Physics']
    },
    {'university': 'University of California, Berkeley',
     'popular_courses': ['Computer Science', 'Economics', 'Environmental Science']
    },
    {'university': 'University of Cambridge',
     'popular_courses': ['Engineering', 'Mathematics', 'Medicine']
    },
    {'university': 'University of Oxford',
     'popular_courses': ['Philosophy, Politics and Economics (PPE)', 'Law', 'History']
    },
    {'university': 'California Institute of Technology (Caltech)',
     'popular_courses': ['Physics', 'Engineering', 'Chemistry']
    },
    {'university': 'University of Chicago',
     'popular_courses': ['Economics', 'Business', 'Political Science']
    }
]

print (uni)

print ('3rd university course is: ', uni[2]['popular_courses'])

uni[4]['popular_courses'] = 'Law'
print (uni)

uni.pop(6)

print ('Last university is: ', uni[-1])