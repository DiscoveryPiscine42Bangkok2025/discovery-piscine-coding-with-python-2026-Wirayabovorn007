import checkmate as helper


def checkmate(board):
	status = helper.in_check(board)
	if (status == True):
		print("Success")
	elif (status == -1):
		print("Error")
	else:
		print("Fail")

def main():
	board = """\
...K
....
....
....\
"""
	checkmate(board)

if __name__ == "__main__":
	main()