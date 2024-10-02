job = [
    {'job': 'Software Developer',
     'salary': 480000
    },
    {'job': 'Accountant',
     'salary': 360000
    },
    {'job': 'Nurse',
     'salary': 300000
    },
    {'job': 'Teacher',
     'salary': 240000
    },
    {'job': 'Call Center Agent',
     'salary': 240000
    },
    {'job': 'Mechanical Engineer',
     'salary': 420000
    },
    {'job': 'Graphic Designer',
     'salary': 300000
    },
    {'job': 'Sales Manager',
     'salary': 600000
    },
    {'job': 'HR Manager',
     'salary': 480000
    },
    {'job': 'Electrician',
     'salary': 240000
    }
]

print (job)

print ('3rd job average salary is: ', job[2]['salary'])

job[6]['salary'] = '350000'
print (job)

job.pop(8)

print ('Last job is: ', job[-1])