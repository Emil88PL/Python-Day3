class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
    ...



class Profesor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
    ...


wizard = Wizard("Albus")
student = Student("Harry", "Griffindor")
profesor = Profesor("Severus", "Defense against the dark side")

print(wizard.name)
print(student.name)
print(profesor.name, profesor.subject)



# inheritance