
cubes = [ i ** 3 for i in range(11)]
print(cubes)

evens = [i ** 2 for i in range(11) if i % 2 == 0]
print(evens)

#list of all numbers below input number that are multiple of 3 and 5

x = 100 #

list = [i for i in range(x) if i % 3 == 0 and i % 5 == 0]

print(list)

def make_even(number):
    if number % 2 == 1:
        return number + 1
    else:
        return number

y = [551, 332, 447, 324, 753, 341, 341, 222, 103, 893, 99, 100, 101, 482]

z = [make_even(number) for number in y]

print(z)