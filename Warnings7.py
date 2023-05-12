class MyError(Exception):
    pass

def myfunc(*arguments):
    if not all(arguments):
        raise MyError("False or empty argumnt in function")
    
try:
    myfunc("Tom", 42, "")
except MyError as err:
    print("Missing / false data", err)





# trace back, object, 