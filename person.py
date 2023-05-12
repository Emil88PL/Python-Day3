
# from abc import ABCMeta


class Person:    # (metaclass=ABCMeta)
    uniqueID = 0
    #@abstractmethod
    def __init__(self, name):
        self._name = name
        Person.uniqueID += 1

    def __str__(self):
        return f"{self._name}: ID: {self.uniqueID}"
    
test1 = Person("Jimmy")
print(test1)
test2 = Person("Clark")
print(test2)