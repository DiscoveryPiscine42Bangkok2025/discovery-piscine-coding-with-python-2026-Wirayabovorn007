#!/bin/python3

n = input()

for i in n:
	if (i.isalpha()):
		if (i.isupper()):
			print(i.lower(), end="")
		else:
			print(i.upper(), end="")
print()