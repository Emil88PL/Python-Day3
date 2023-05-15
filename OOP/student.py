def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "RavenClaw"
    print(f"{student[0]} is from {student[1]}")

def get_student():
    name = input("Name ")
    house = input("House ")
   # return name, house  # that is a tuple - you cannot change tuple 
    return [name, house]
    
if __name__ =="__main__":
    main()