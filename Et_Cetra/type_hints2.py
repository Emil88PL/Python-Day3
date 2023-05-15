# mypy

# pip install mypy

# to check if our variabels using the right type

def meow(n: int) -> None:
    for _ in range(n):
        print("meow")
    ...


number: int =int(input("Enter a number of mews: "))  # add :int = to specify where int is excpected
meows: str = meow(number)
print(meows)



# to run mypy type $ mypy [name of a file]