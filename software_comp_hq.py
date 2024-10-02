companies = [
    {'company': 'Microsoft',
     'hq': 'Redmond, Washington, USA'},
    {'company': 'Apple',
     'hq': 'Cupertino, California, USA'},
    {'company': 'Google',
     'hq': 'Mountain View, California, USA'},
    {'company': 'Adobe',
     'hq': 'San Jose, California, USA'},
    {'company': 'Oracle',
     'hq': 'Redwood City, California, USA'},
    {'company': 'IBM',
     'hq': 'Armonk, New York, USA'},
    {'company': 'SAP',
     'hq': 'Walldorf, Germany'},
    {'company': 'Salesforce',
     'hq': 'San Francisco, California, USA'},
    {'company': 'Intuit',
     'hq': 'Mountain View, California, USA'},
    {'company': 'Atlassian',
     'hq': 'Sydney, Australia'}
]

print (companies)

print ('3rd company hq is: ', companies[2]['hq'])

companies[7]['hq'] = 'Philippines'
print (companies)

companies.pop(8)

print ('Last company is: ', companies[-1])