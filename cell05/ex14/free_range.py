#!/bin/python3

import sys

n = len(sys.argv) - 1
if n != 2:
	print("none")
arr = []
x = int(sys.argv[1])
y = int(sys.argv[2])
for i in range(x, y+1):
	arr.append(i)
print(arr)
