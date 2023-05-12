def square(length):
    return f"The area of the square is {length * length}"
print(square(9)) # != hard code 

def rect(length, height):
    return f"The area of the rectangle is {length * height}"

def add(x,y):
    return x + y

import math

def circle(r):
    return f"The area of the circle is {round(math.pi * r**2)}"