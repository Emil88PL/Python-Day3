import sys
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house  # do not use _ as that have to go through setter 

    def __str__(self):
        return f"{self.name} is form {self.house}"
# porperties, attributes @ decorator functions which modify other functions



    # Getter
    @property
    def name(self):
        return self._name
    
    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("No name given")
        self._name = name

        

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