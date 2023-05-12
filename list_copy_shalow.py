
fruit = ["Apple", "Pear", "Peach"]
print(fruit[1])

lunch = fruit
print(lunch) # shalow copy of fruit
lunch[1] = "Eggs"
print(fruit)

lunch = fruit[:] # coping list
lunch[1] = "Eggs"
print("Fruit:",fruit, "\nLunch:", lunch)

fruit = ["Knife", "Spoon", ["Apple", "Peach", "Orange"]]
lunch = fruit[:]
lunch[2][1] = "Eggggsss"
print("New Fruit:",fruit, "\nNew Lunch:", lunch)

import copy                                                 
fruit = ["Knife", "Spoon", ["Apple", "Peach", "Orange"]]
lunch[2][1] = "Eggggsss"
print("Fruit3:", fruit, "\nLunch3:",lunch)
