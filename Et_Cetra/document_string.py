# doctstring


def meow(n: int) -> str:  # document functions, 3rd party convention 
        """
        :param n: number of times to meow
        :type n: int
        :raise TypeError: if n is not an integer
        :return: string
        :rtype: str

        >>> print("meow")
        meow
    
        """
        return "meow\n" * n


number: int =int(input("Enter a number of mews: "))  
meows: str = meow(number)
print(meows, end="")

help(meow)