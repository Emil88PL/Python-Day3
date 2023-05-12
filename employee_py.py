from person import Person

class Employee(Person):
    _class_version = 0.03

    @classmethod
    def get_version(cls):
        return cls._class_version
    
    def __init__(self, name, dep):
        super().__init__(name)
        self._dep = dep

emp1 = Employee("David", "IT")
print(emp1)

emp2 = Employee("William", "Sales")

print(emp2, emp2._dep)
print("Employee version: ",emp1.get_version())