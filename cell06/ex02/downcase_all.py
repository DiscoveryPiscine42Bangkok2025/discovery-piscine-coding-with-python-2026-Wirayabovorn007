#!/bin/python3

import sys

def downcase_it(str):
	return str.lower()

def main():
	if len(sys.argv) - 1 == 0:
		print("none")
		return 
	for i in range(1, len(sys.argv)):
		print(downcase_it(sys.argv[i]))
main()