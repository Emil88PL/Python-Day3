names = []


with open("names.txt") as file:
    for line in file:
        names.append(line)

for name in sorted(names, reverse=True):
    print(f"hello, {name}")