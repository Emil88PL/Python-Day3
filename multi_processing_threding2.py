# two seperate programs or elements of program running at the same time 
# multi threding diffrent part of the same program
# not asing.io

#threading

from threading import Thread
import time

def myfunc(*args): ## will return tuples  ## *kwargs dictionarty
    print("From Thread: ", args)
    time.sleep(1)

def myOther(*args):
    time.sleep(5)
    print("From Thread: ", args)

th1 = Thread(target=myfunc, args="1")
th2 = Thread(target=myfunc, args="2")
th3 = Thread(target=myOther, args="3")

th1.start()
th2.start()
th3.start()

print("From main")
th3.join()
th1.join()
th2.join()

print("The end")


# not fail safe 
# they can be accessed still
