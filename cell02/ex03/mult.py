#!/bin/python3
st = int(input("Enter the first number:\n"))
nd = int(input("Enter the second number:\n"))

print(f"{st} x {nd} = {st * nd}")
if (st * nd == 0):
	print("The result is positive and negative.")
elif (st * nd > 0):
	print("The result is positive.")
else:
	print("The result is negative.")