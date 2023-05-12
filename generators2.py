# Generators

def infinite_seq():
    num = 0
    while True:
        yield num
        num += 1


gen = infinite_seq()

print(next(gen))  # save memory 
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
