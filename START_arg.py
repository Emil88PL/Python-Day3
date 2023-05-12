def my_function(dir, *files):  #arg
    print("dir: ", dir, "Files: ", files)

print(my_function("C:/Sopra/data/test", "test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt"))

### *args returns a tuple