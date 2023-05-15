# mypy

# pip install mypy

# to check if our variabels using the right type

def meow(n: int) -> str:
        return "meow\n" * n


number: int =int(input("Enter a number of mews: "))  # add :int = to specify where int is excpected
meows: str = meow(number)
print(meows, end="")



# to run mypy type $ mypy [name of a file]