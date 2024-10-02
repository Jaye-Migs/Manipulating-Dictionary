company = [
    {'company': 'Apple Inc.',
     'founder': 'Steve Jobs, Steve Wozniak, Ronald Wayne'
    },
    {'company': 'Microsoft',
     'founder': 'Bill Gates'
    },
    {'company': 'Amazon',
     'founder': 'Jeff Bezos'
    },
    {'company': 'Facebook (Meta Platforms, Inc.)',
     'founder': 'Mark Zuckerberg, Eduardo Saverin, Andrew McCollum, Dustin Moskovitz, Chris Hughes'
    },
    {'company': 'Google (Alphabet Inc.)',
     'founder': 'Larry Page, Sergey Brin'
    },
    {'company': 'Tesla, Inc.',
     'founder': 'Elon Musk, Martin Eberhard, Marc Tarpenning, JB Straubel, Ian Wright'
    },
    {'company': 'Coca-Cola',
     'founder': 'John Stith Pemberton'
    },
    {'company': 'Nike, Inc.',
     'founder': 'Phil Knight, Bill Bowerman'
    }
]

print (company)

print ('6th company founder is: ', company[5]['founder'])

company[1]['founder'] = 'Bill Gates, Paul Allens'
print (company)

company.pop(7)

print ('Last company is: ', company[-1])