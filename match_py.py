name = input("What is your name? ").strip().title()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slythering")
    case _:
        print("Who?")

print(name)