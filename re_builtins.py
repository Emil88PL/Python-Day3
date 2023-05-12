import builtins
import re

names = dir(builtins)
print(len(names))

my_string = "Hello there!"
print("Error" in my_string)

#for error in filter(lambda string: "Error" in string, names):   ##         error in names
#    print(error)

#for name in filter(lambda string: "it" in string, names):  ##      it in names
#    print(name)

#for name in filter(lambda string : string.startswith("E"), names): ## E in names
#    print(name)

#for name in filter(lambda x : re.search(r"t$", x), names):   # ending with "t" in names
#    print(name)

for name in filter(lambda x : re.search(r"^t", x), names):   # starting with "t" in names
    print(name)