# map

#yell

def main():
    yell("This", "is", "a", "unpacking")

def yell(*words): # unpacking first time form yell function
    uppercase = []
    for word in words:
        uppercase.append(word.upper())
    #print(uppercase, end=" ") # printing with []
    print(*uppercase, end=" ") # unpacking with out [] unpacking 2nd time from for loop


if __name__ == "__main__":
    main()

