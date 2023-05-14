def main():
    x = input("Enter a number to sqer: ")
    print("x square is ", square(x))

def square(x):
    """
    >>> square(2)
    4


    """
    return x * x


if __name__=="__main__":
    main()
    