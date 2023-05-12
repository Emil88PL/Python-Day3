def multiply(x, y):
    """
    Accept 2 numbers
    >>> multiply(3,3)
    9

    :return:
    """
    return x * y

def add(x, y):
    """
    >>> add(1,2)
    3

    """
    return x + y

def main():
    print(f"Multiply 3 * 3 is {multiply(3,3)}")
    print(f"Adding 1 + 2 is  {add(1,2)}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()

    # to run test python3 def_test.py -v OR use pyCharm(test running automatically)