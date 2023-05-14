import csv

students = []

with open("File I.O/new_students.csv") as file:
    reader = csv.DictReader(file, skipinitialspace=True)   
    for row in reader:
        students.append({"name": row["name"], "home": row["house"], "location": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']} lives in {student['location']}")