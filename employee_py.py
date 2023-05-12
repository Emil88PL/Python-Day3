from person import Person

class Employee(Person):
    def __init__(self, name, dep):
        super().__init__(name)
        self._dep = dep

emp1 = Employee("David", "IT")
print(emp1)

emp2 = Employee("William", "Sales")

print(emp2, emp2._dep)