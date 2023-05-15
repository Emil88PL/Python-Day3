import sys
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("No name given")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} is form {self.house}"
# porperties, attributes @ decorator functions which modify other functions


    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Slythering", "RavenClaw", "Hufflepuff", "x"]:
            raise ValueError("Invalid house")
        self._house = house
    

def main():
    student = get_student()
    print(student)
   

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

if __name__ =="__main__":
    main()