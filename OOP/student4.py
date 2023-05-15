class Student:
    ...

# wjem you crate clas you create object 





def main():
    student = get_student()
    print(f"{student._name} is from {student._house}")

def get_student():
    student = Student()
    student._name = input("Name ").title()
    student._house = input("House ").title()
    return student


    
if __name__ =="__main__":
    main()