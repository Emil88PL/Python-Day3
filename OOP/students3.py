def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "RavenClaw"
    print(f"{student['name']} is from {student['house']}")

def get_student():
    name = input("Name ")
    house = input("House ")
    return {"name": name, "house": house}
    
if __name__ =="__main__":
    main()