studGrades = {

"student1" : {
    "Name" : "Santos",
    "Grades" : 90
},
"student2" : {
    "Name" : "Dumo",
    "Grades" : 85
},
"student3" : {
    "Name" : "DeGuzman",
    "Grades" : 90
},
"student4" : {
    "Name" : "Buenaventura",
    "Grades" : 80
},
"student5" : {
    "Name" : "Escano",
    "Grades" : 95
},
}

print(studGrades)

print("Grade of: ", studGrades["student1"])

studGrades["student3"]["Grades"] = 95
print("Grade of: ", studGrades["student3"])

del studGrades["student4"]
print(studGrades)

last_pair = list(studGrades.items())[-1]
print(last_pair)