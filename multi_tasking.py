# multi taskking  

import subprocess # running a program (go and do this) 
# calling - parent #  we call child
import sys

#  print(sys.executable)


#proc = subprocess.run([sys.executable, "hello.py"])

proc = subprocess.run([sys.executable, "hello.py"], ## like promise or fetch from JAVA
                      stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE
                      )

if proc.stderr:
    print("error ", proc.stderr.decode('utf-8'))


print(proc.stdout.decode())

print("Child extended with: ", proc.returncode)


