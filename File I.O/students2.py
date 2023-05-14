with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")  #split returns a list   name, house assign two variables at once
        print(f"{name} is in {house}")

