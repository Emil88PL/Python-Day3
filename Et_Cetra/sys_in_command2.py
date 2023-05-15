#argparse 

import argparse

parser = argparse.ArgumentParser(description="meow like a cat")
parser.add_argument("-n", default=1, help="number of time meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
        print("meow")



# run from terminal $python [name of file] -n [times of meow]
