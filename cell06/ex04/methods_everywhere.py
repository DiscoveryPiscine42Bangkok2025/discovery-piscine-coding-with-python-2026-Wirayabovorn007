#!/bin/python3

import sys

def shrink(str):
	print(str[0:8])


def enlarge(str):
	while (len(str) != 8):
		str += "Z"
	print(str)

def main():
	if (len(sys.argv) - 1 == 0):
		print("none")
		return
	for i in range(1, len(sys.argv)):
		if (len(sys.argv[i]) >= 8):
			shrink(sys.argv[i])
		else:
			enlarge(sys.argv[i])
main()