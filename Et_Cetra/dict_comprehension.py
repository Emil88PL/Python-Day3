
students = ["Harry", "Hermione", "Ron"]

# gryffindors = []
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})

# list comprahention
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

#list dict comprehention
gryffindors = {student: "Gryffindor" for student in students}




print(gryffindors)