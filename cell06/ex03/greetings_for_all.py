#!/bin/python3

def greetings(name=None):
    if name is None:
        print("Hello, noble stranger.")
        return

    if not isinstance(name, str):
        print("Error! It was not a name.")
        return

    if not name.isalpha():
        print("Error! It was not a name.")
        return

    print("Hello,", name)


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
