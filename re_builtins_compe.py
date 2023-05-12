import builtins
import re

names = dir(builtins)

my_string = "Hllo There"
new_list = []
for name in names:
    if name.startswith("E"):
        new_list.append(name)
print(new_list)

new_list2 = [name for name in names if name.startswith("E")]
print(new_list[1:5])