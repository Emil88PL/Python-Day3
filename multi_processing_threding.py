# two seperate programs or elements of program running at the same time 
# multi threding diffrent part of the same program
# not asing.io

#threading

from threading import Thread
import time

def myfunc(*args): ## will return tuples
    print("From Thread: ", args)
    time.sleep(1)

th1 = Thread(target=myfunc, args="1")
th2 = Thread(target=myfunc, args="2")

th1.start()
th2.start()

print("From main")

th1.join()
th2.join()

print("The end")


# not fail safe 
# they can be accessed still
