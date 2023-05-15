class Student:   # put in other file
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


## file student11.py calling Student class
# 
# 
# 
# @staticmethod