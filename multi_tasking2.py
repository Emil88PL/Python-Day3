# multi taskking  

import subprocess # running a program (go and do this) 
# calling - parent #  we call child
import sys

#  print(sys.executable)


#proc = subprocess.run([sys.executable, "hello.py"])

proc = subprocess.run([sys.executable, "hello2.py"], ## like promise or fetch from JAVA
                      input = b"You got my message",
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE
                      )

if proc.stderr:
    print("error ", proc.stderr.decode())


#print(proc.stdout.decode())

print("Output: ", proc.stdout.decode())


