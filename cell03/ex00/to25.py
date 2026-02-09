#!/bin/python3

n = int(input("Enter a number less than 25\n"))

if (n > 25):
	print("Error")
for i in range(n, 25+1):
	print(f"Inside the loop, my variable is {i}")