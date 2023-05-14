# it works with skipinitialspace=True !!!

import csv

students = []

with open("File I.O/students2.csv") as file:
    reader = csv.reader(file, skipinitialspace=True)   
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")



## belove example dosent work - https://cs50.harvard.edu/python/2022/notes/6/ copy from harvard webstie still not working as intended
## reading only half line
# import csv

# students = []

# with open("File I.O/students2.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "home": row[1]})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")