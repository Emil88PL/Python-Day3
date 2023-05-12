def f(x):
    return x * 2
print(f(2))


# inline function lambda

g = lambda x: x * 2   # Do not write lambda like this
print(g(2))


ls = ["109", "120", "1111", "11222"]

ls.sort(key=lambda x: int(x[-1]))
print(ls)

compare = lambda a, b: -1 if a < b else (+1 if a > b else 0)  # showing 1 if true -1 if false -- 0 if equal

x = 322
y = 32

print("a > b", compare(x, y))  