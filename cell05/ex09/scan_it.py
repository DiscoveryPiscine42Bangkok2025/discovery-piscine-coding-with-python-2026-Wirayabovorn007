#!/bin/python3

#!/bin/python3

import sys

argc = len(sys.argv) - 1;

if (argc != 2):
	print("none");
else:
	count = 0
	arr = sys.argv[2].split(" ")
	for i in arr:
		if (i == sys.argv[1]): count+=1
	print(count)