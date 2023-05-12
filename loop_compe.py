import builtins
import re

names = dir(builtins)
my_string = "Hello there!"
new_list = []

numbers = list(range(1100))

#loop comprehensions

print([number for number in numbers if number%2 == 0])