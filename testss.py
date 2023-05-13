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







    
        
    
        























