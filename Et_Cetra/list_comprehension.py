
# map

#yell

def main():
    yell("This", "is", "a", "usee", "of", "map")

def yell(*words):
    uppercase = [word.upper() for word in words]
    print(*uppercase, end=" ") 


if __name__ == "__main__":
    main()

