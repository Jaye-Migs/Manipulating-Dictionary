city ={
    "Manila" : {
        "Population" : 1600000
    },
    "Caloocan" : {
        "Population" : 1500000
    },
    "Quezon" : {
        "Population" : 2700000
    },
    "Davao" :{
        "Population" : 1200000
    },
    "Cebu" : {
        "Population" : 790000
    },
    "Taguig" : {
        "Population" : 600000
    },
    "Pasig" : {
        "Population" : 600000
    },
    "Antipolo" : {
        "Population" : 550000
    },
    "Las Pinas" : {
        "Population" : 590000
    },
    "Makati" : {
        "Population" : 510000
    }
}

print(city)

city4 =list(city.items())[5]
print(city4)

city["Quezon"]["Population"] = 2750000
print("New Population of 3rd city is: ", city["Quezon"]["Population"])

del city["Las Pinas"]

print(city)

last_pair = list(city.items())[-1]
print(last_pair)