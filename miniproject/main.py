import checkmate as helper


def checkmate(board):
	if (helper.in_check(board) == True):
		print("Success")
	elif (helper.in_check(board) == -1):
		print("Error")
	else:
		print("Fail")

def main():
	board = """\
R...
...K
PB..
....\
"""
	checkmate(board)

if __name__ == "__main__":
	main()