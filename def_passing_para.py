def my_func(file, dir, user="root"):
    print("File: {:}, dir {:}, user: {}".format(file, dir, user))

#by position
my_func("one", "two", "three")

#by default
my_func("one", "two")

#by name
my_func(file="one", dir="two", user="three")