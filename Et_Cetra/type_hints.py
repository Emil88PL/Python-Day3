# mypy

# pip install mypy

# to check if our variabels using the right type

def meow(n: int):
    for _ in range(n):
        print("meow")
    ...


number: int =int(input("Enter a number of mews: "))  # add :int = to specify where int is excpected

meow(number)


# to run mypy type $ mypy [name of a file]