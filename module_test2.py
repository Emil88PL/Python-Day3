from modules_test import add as add
print(add(2,2))

from modules_test import  square
print(square(5))

import modules_test
print(modules_test.circle(3))

from modules_test import *  # do not do this

