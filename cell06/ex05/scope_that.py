#!/bin/python3

def add_one(n):
	n+=1
	print("Inside add_one():", n)

x = 5
print("Before function:", x)
add_one(x)
print("After function", x)