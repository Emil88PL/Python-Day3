def my_func(*,file, dir, user="root"):
    print("File: {:}, dir {:}, user: {}".format(file, dir, user))

#by position
#my_func("one", "two", "three") # only file name is named

#by default
#my_func("one", "two") # neither file name named

#by name
my_func(file="one", dir="two", user="three") # all files are named