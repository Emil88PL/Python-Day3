from multiprocessing import Process

def myfunc(*args):
    print("From proc: ", args)

def main():

    p1 = Process(target=myfunc, args="1") # in main
    p2 = Process(target=myfunc, args="2") # in main

    p1.start() # in main
    p2.start() # in main

    print("From main: ")

    p1.join()
    p2.join()

if __name__ == "__main__": # have to be in main
    main()
