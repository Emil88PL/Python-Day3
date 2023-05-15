import sys
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("No name given")
        if house not in ["Gryffindor","Slythering", "RavenClaw", "Hufflepuff", "x"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} is form {self.house}"

    def charm(self):
        match self.patronus:
            case "kiss":
                return "😘"
            case "xxx":
                return "✨"
            case "nice":
                return "👍"
            case _:
                return "🐺"
    



def main():
    student = get_student()
    print("Expecto patronum")
    print(student.charm())

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


    

    
if __name__ =="__main__":
    main()