import sys
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("No name given")
        if house not in ["Gryffindor","Slythering", "RavenClaw", "Hufflepuff", "x"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} is form {self.house}"


def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name: ")
    house = input("House: ")
    
    return Student(name, house)
    

    
if __name__ =="__main__":
    main()