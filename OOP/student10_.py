import sys
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house  

    def __str__(self):
        return f"{self.name} is form {self.house}"
    
    @classmethod # calling student form get student - not creating student and then coalling
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # instantiate student object   



def main():
    student = Student.get()
    print(student)
   

if __name__ =="__main__":
    main()