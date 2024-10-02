phone = [
    {'model': 'iPhone 14',
     'manufacturer': 'Apple'
    },
    {'model': 'Galaxy S23',
     'manufacturer': 'Samsung'
    },
    {'model': 'Pixel 7',
     'manufacturer': 'Google'
    },
    {'model': 'OnePlus 11',
     'manufacturer': 'OnePlus'
    },
    {'model': 'Xperia 1 IV',
     'manufacturer': 'Sony'
    },
    {'model': 'Nokia G50',
     'manufacturer': 'Nokia'
    },
    {'model': 'Moto G Power',
     'manufacturer': 'Motorola'
    },
    {'model': 'Oppo Find X5 Pro',
     'manufacturer': 'Vivo'
    },
    {'model': 'Xiaomi 12 Pro',
     'manufacturer': 'Xiaomi'
    },
    {'model': 'Huawei P50 Pro',
     'manufacturer': 'Huawei'
    }
]

print (phone)

print ('2nd phone manufacturer is: ', phone[1]['manufacturer'])

phone[7]['manufacturer'] = 'Oppo'
print (phone)

phone.pop(5)

print ('Last phone is: ', phone[-1])