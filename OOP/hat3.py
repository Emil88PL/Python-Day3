# @classmethod
import random

class Hat:

    houses = ["Gryffindor","Slythering", "RavenClaw", "Hufflepuff", "x"] # with out self. houses are accesable to all methods
    
    @classmethod
    def sort(cls, name): # reference to class itself
        print(name, "is in", random.choice(cls.houses))

# when you want it just once - you do not need more hats doing same thing



Hat.sort("Harry")
Hat.sort("Ron")
Hat.sort("Hermione")
Hat.sort("Draco")


