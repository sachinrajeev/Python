#!/usr/bin/py

import sys

if(len(sys.argv)==1)
	print("atleast one input")
	exit()

try:
           				  # Convert it into int
            val = int(sys.argv[1])
        except ValueError:
            print("No.. input is not a number.")
            exit()

print("%.nf" % (22/7))

