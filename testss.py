# def main():
#     times = int(input("How many times? "))
#     cat_do(times)
#     dog_do(times)


# def cat_do(times):
#     x = "meow"
#     i = 1 # from 1 for reading - Better to start from 0 
#     while i < times:
#         print(f"{x} : {i} times")
#         i += 1

# def dog_do(times):
#     x = "bark"
#     i = 1
#     while i < times:
#         print(f"{x} : {i} times")
#         i += 1

# main()

# # square = assignment
# # ttriangle = question
# # circle = start / stop

# list

# for _ in range(11): # Pythonic version
#     print("Moew")

# print("Moew\n" * 3, end="")  # Pythonic version

# while True:

# while True:
#     n = int(input("What is n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("Meow")

# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("How many times? "))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("Meow")

    
# main()


# students = ["Hermione", "Harry", "Roen"]

# #print(students[0])

# # for student in students:
# #     print(student)

# for i in range(len(students)):
#     print(i + 1, students[i])

# Dictionaries key and value


# dict = {"Gryffindor": ["Hermione", "Harry", "Ron"], "Slytheryn": "Draco"}

# for key in dict:
#     print(key, dict[key])

# new_val = input("Enter new value for Gryffindor: ")


# dict["Gryffindor"].append(new_val)

# print(dict["Gryffindor"])

# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel terrier"},
#     {"name": "Draco", "house": "Slytheryn", "patronus": None}, # None absent of value 
# ]


# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=": ")

# MARIO
# MARIO
# MARIO

# def main():
#        # print_column(3)
#        # print_row(4)
#         print_square(3)

# def print_column(height):
#         print("#\n" * height, end="" )

# def print_row(width):
#         print("?" * width)

## 1

# def print_square(size):
#         for i in range(size):
#                 for j in range(size):
#                         print("#", end="") # printing in the line
#                 print() # new line after 

## 2

# def print_square(size):
#         for i in range(size):
#                print("#" * size) 

## 3

# def print_square(size):
#         for i in range(size):
#               printing_row(size) 

# def printing_row(width):
#          print("#" * width)
        
# main()

# ## 1
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("Put a number "))
#             #break no else then
#         except ValueError:
#             print("Put a correct number")
#         else:
#             break
#             #print(f"x is {x}")
#     return x

# main
    
#  ## 2

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("Put a number ")) # return is equal to break
#         except ValueError:
#             print("Put a correct number")
       

# main()       

## 3

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("Put a number "))
#         except ValueError:
#             pass # just pass if you dont want to show the error to the user 
#             print("Put a correct number")
       
# main()

 ## 4

# def main():
#     x = get_int("What is x? ")
#     print(f"x is {x}")

# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass # just pass if you dont want to show the error to the user 
#             print("Put a correct number")
       
## raise.....
# main()

#libraries
# module one or more feature
# random
# import random
#print(dir(__builtins__))


## 1
# import random

# coin = random.choice(["Heads", "Tails"])
# print(coin)

## 2
# from random import choice

# coin = choice(["Heads", "Tails"])
# print(coin)

## 3

# from random import choice as chi

# coin = chi(["Heads", "Tails"])
# print(coin)

# from random import randint

# number_random = randint(0, 10000)
# print(number_random)

# from random import shuffle

# cards = ["Jack", "Queen", "King", "Player"]

# shuffle(cards)

# for card in cards:
#     print(card)

## 4
# import statistics
# # avrage calculatcion
# print(statistics.mean([100,20]))

## command line arguments
## sys.argv

# argument vector

## 1
# import sys
# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Too few arguments")

## 2

# import sys
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("hello, my name is", sys.argv[1])

## 3

# import sys

# #check for errors

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")  # exit after prompt

# # print name tags
# print("hello, my name is", sys.argv[1])

## 4

# import sys

# #check for errors

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# # slice
# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)

# packages
# PyPi
# cowsay

# import cowsay
# import sys

# if len(sys.argv) == 3:
#     cowsay.cow("Hello, " + sys.argv[1] + "! " + sys.argv[2] + "! ")
#     cowsay.dragon("Hello, " + sys.argv[1] + "! " + sys.argv[2] + "! ")
#     cowsay.trex("Hello, " + sys.argv[1] + "! " + sys.argv[2] + "! ")


# APIs !!!!
#####################################################################################################################################################


# requests install by pip
# itunes API APPPLE

## https://itunes.apple.com/search?entity=song&limit=1&term=weezer
## JSON
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit()

#                                                                     #limit of the songs 50
# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# #print(json.dumps(response.json(), indent=2)) # translate json to readable format

# o = response.json()  ## storing all json response in to a variable
# for result in o["results"]:
#     print(result["trackName"])







































