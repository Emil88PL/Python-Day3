name = input("Your name: ")

with open("names.txt","a") as file: #Pythonic way of closing file
    file.write(f"{name}\n")

