#!/bin/python3

import sys

def main():
	n = len(sys.argv) - 1

	if (n == 0):
		print("none")
		return 
	for i in range (1, n+1):
		if ("ism" not in sys.argv[i]):
			print(sys.argv[i] + "ism")
		else:
			print(sys.argv[i])
main()