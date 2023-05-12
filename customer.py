from person import Person
from employee_py import Employee

class Customer(Person):
    _class_version = 0.02

    @classmethod
    def get_version(cls):
        return cls._class_version

    def __init__(self, name, initial):
        super().__init__(name)
        self._balance = initial

    def deposit(self, amt):
        self._balance += amt
        return f"You have doposited £{amt} your balance is £{self._balance}"
    
    def withdraw(self, amt):
        if self._balance - amt < 0:
            print("You have not enough money to withdraw")
        else:
            return f"You have withdraw £{amt} your balance is now £{self._balance}"
    
    def getbalance(self):
        return f"Your balance is {self._balance}"
    
    def set_balance(self, newamt):
        self._balance = newamt
        return f"{self._name} Your new balance is {self._balance}"
    

cus1 = Customer("Jimmy", 400)
print(cus1)
print(cus1.deposit(222))
print(cus1.getbalance())

cus2 = Customer("Lisa", 1432)
print(cus2.getbalance())
print(cus2.set_balance(332))

print("Customer version: ",cus1.get_version())
print("Customer version: ",cus2.get_version())





