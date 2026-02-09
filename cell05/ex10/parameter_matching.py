#!/bin/python3



import sys

argc = len(sys.argv) - 1;

if (argc != 1):
	print("none");
else:
	n = input("What was the parameter? ")
	if (n == sys.argv[1]):
		print("Good job!")
	else:
		print("Nope, sorry...")