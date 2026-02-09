#!/bin/python3
i = 0
while (True):
	if (i == 0):
		print("What you gotta say? : ", end="")
		i+=1
	else:
		print("I got that! Anything else? : ", end="")
	n = input()
	if (n == "STOP"):
		break