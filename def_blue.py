def main():
    name = input("What's your name? ").strip().title()
    hello(name)
    

def hello(to="World!"):
    print("Hello,", to)



def calc():
    try:
        while True:
            x = int(input("Enter a number "))
            print(f"Square of {x} is:", square(x))
    except:
        error()


def square(x):
    return x * x

def error():
        print("Only Numbers please!")
        calc()

main()
calc()