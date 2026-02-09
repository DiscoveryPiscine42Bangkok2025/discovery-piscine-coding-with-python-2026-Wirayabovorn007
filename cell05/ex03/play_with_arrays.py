#!/bin/python3



og = [2, 8, 9, 48, 8, 22, -12, 2]
new = set()
for i in og:
	if ((i > 5)):
		new.add(i+2)
print("Original array: ", og)
print("New array: ", new)