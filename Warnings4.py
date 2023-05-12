# do and check
# try block


num = input("ENter a number")

try:
    float(num)
except ValueError:
    print("that was not a number")
else:
    print("Continue")
finally:
    print("Finished")
    