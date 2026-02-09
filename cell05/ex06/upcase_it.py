#!/bin/python3

import sys

argc = len(sys.argv) - 1;

if (argc != 1):
	print("none");
else:
	print(sys.argv[1].upper())