# list of words.txt

filename = "foo"
#filename = "Warnings.py"
#filename = 99


errmsg = ""

try:
    f = open(filename)
except FileNotFoundError as err:
    errmsg = filename + " not found"
    print(err.args[1])
except (TypeError, ValueError, AttributeError, OSError, IOError):
    errmsg = "Invalid file format"
else:
    print("File opened....")


if errmsg != "":
    exit(errmsg)

