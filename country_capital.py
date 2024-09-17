country = {
"Afghanistan" : {
    "Capital" : "Kabul"
},
"Albania" : {
    "Capital" :"Tirana (Tirane)"
},
"Algeria" : {
    "Capital" :"Algiers"
},
"Andorra" : {
    "Capital" :"Andorra la Vella"
},
"Angola" : {
    "Capital" :"Luanda"
},
"Antigua and Barbuda" : {
    "Capital" :"Saint John's"
},
"Argentina" : {
    "Capital" :"Buenos Aires"
},
"Armenia" : {
    "Capital" :"Yervandashat"
},
"Australia" : {
    "Capital" :"Canberra"
},
"Austria" : {
    "Capital" :"Vienna"
},
"Azerbaijan" : {
    "Capital" :"Baku"
},
"Bahamas" : {
    "Capital" :"Nassau"
}
}

print(country)

country5 = list(country.items())[4]
print("Capital of 5th country is: ", country5)

country["Armenia"]["Capital"] = "Yerevan"
print("New Capital of 8th country is: ", country["Armenia"]["Capital"])

needRemoveThis = list(country.items())[10]
country.pop(needRemoveThis[0])
print(country)

last_pair = list(country.items())[-1]
print(last_pair)