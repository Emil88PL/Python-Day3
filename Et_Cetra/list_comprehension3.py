
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

def is_gryffindor(s):
    return s["house"] == "Gryffindor"
     
    
gryffindors = filter(is_gryffindor, students)

for gryf in sorted(gryffindors, key=lambda s: s["name"]):
    print(gryf["name"])

#print(gryffindors)