#alist = []

def my_function(value, alist=[]):
    alist = []
    alist.append(value)
    return alist  

print(my_function(1))
print(my_function(4))
print(my_function(6))
print(my_function(2))
print(my_function(9))
print(my_function(0))