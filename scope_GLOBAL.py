# Variabels in functions
# global are any in main.py

result = 3
def scope_test():
    global result   # take global inside function and change it in Global scope
    print("Before", result)
    result = 42
    print("After", result)

scope_test()
print("Global", result)