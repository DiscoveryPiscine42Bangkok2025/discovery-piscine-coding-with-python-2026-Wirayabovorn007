#!/bin/python3

import sys

argc = len(sys.argv) - 1;

if (argc < 3):
	print("none");
else:
	while (argc > 0):
		print(sys.argv[argc])
		argc -= 1