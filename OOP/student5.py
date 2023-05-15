class Student:
    def __init__(self, name, house):  # dunder init # adding veriables to the object
        self.name = name
        self.house = house



# classes come with methods
# 

# class is a blueprint 
# wjem you crate clas you create object 
# object is a intance


def main():
    student = get_student()
    print(f"{student._name} is from {student._house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house) # passing arguments to a function # constructor call
    return student


    
if __name__ =="__main__":
    main()