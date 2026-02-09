#!/bin/python3

import sys

n = len(sys.argv) - 1

if (n == 0 or ("z" not in sys.argv[1])):
	print("none")
else:
	if ("z" in sys.argv[1]):
		print("z"*sys.argv[1].count("z"))