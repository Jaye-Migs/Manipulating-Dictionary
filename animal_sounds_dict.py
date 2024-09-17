animalSounds = {

"Cat" : {
    "Sounds" : "Meow",
},
"Dog" : {
    "Sounds" : "Bark",
},
"Cow" : {
    "Sounds" : "Moo",
},
"Bird" : {
    "Sounds" : "Twit Twit",
},
"Snake" : {
    "Sounds" : "Hisss",
},
"Crow" : {
    "Sounds" : "Caw Caw",
},
"Duck" : {
    "Sounds" : "Quack Quack",
},
"Horse" : {
    "Sounds" : "Neigh",
},
}

print(animalSounds)

print("Sound of 4th animal: ", animalSounds["Bird"]["Sounds"])

animalSounds["Duck"]["Sounds"] = "Honk"
print("New Sound of 7th animal: ", animalSounds["Duck"]["Sounds"])

soundPair = list(animalSounds.items())[4]
del soundPair
print(animalSounds)

last_pair = list(animalSounds.items())[-1]
print(last_pair)