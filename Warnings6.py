
# in development 

#raise IOError("Ohh no!!!")

def myfunc(*arguments):
    if not all(arguments):
        raise ValueError("False or empty argumnt in function")
    

try:
    myfunc("Tom", 42, "")
except ValueError as err:
    print("Missing / false data", err)

print("Continue.....")
