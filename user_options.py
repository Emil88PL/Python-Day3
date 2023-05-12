def hello():
    print("hello")
def goodbay():
    print("goodbay")
def insult():
    print("Insult")
def complement():
    print("complement")

while True:
    choice = input("""

    Press "h" for Greeting
    Press "g" for farewell
    Press "i" for insult
    Press "c" for complement
    Press "x" for exit
    
    """)

    if choice in ("H", "h"):
        hello()
    elif choice in ("G", "g"):
        goodbay()
    elif choice in ("I", "i"):
        insult()
    elif choice in ("C", "c"):
        complement()
    elif choice in ("X", "x"):
        break
    else:
        print("Not a valid choice")

print("THank you for using the machine")