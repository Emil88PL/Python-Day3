import csv

name = input("Your name: ")
home = input("Where is your home?: ")

with open("name_home.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"], skipinitialspace=True)
    writer.writerow({"name": name, "home": home})
