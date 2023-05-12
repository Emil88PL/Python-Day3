from multiprocessing import Process, Queue
import os

def my_func(*args):
    queue = args[0]

    word = ""
    while word != "END":
        word = queue.get()
        if len(word) == 15:
            print(os.getpid(), ":", word)

def main():
    queue = Queue()

    p1 = Process(target=my_func, args=(queue, "1"))
    p2 = Process(target=my_func, args=(queue, "2"))

    p1.start()
    p2.start()

    for line in open('words.txt'):
            queue.put(line[:-1]) 

    queue.put("END")
    queue.put("END")

    p1.join()
    p2.join()
    print("ALl done!")


if __name__ == "__main__": # have to be in main
     main()

