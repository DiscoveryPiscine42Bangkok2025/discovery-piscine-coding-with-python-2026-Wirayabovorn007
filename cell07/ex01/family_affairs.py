#!/bin/python3

def find_the_redheads(fam):
	red_head = []
	for key, val in fam.items():
		if (val == "red"):
			red_head.append(key)
	return red_head


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))