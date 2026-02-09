#!/bin/python3

def array_of_names(data):
	arr = []
	for key, value in data.items():
		name = ""
		name+= key.capitalize() +" "
		name+= value.capitalize()
		arr.append(name)
	return arr

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))