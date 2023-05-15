# generators 
# give it to you a bit of data at time

#yield


import time


def main():
    n = int(input("What's is n "))
    for s in sheep(n):
        print(s)
        
        

def sheep(n):
    for i in range(n):
        yield "🐏" * i  # one data at the time (little data at the time)
        # yield returning iterator 
    


if __name__=="__main__":
    main()

