
def visulize_for_test(board, p):
	print(f"{p} checked:")
	for i in board:
		print(i)

def get_piece_pos(piece, board):
	y = 0
	for row in board:
		x = 0
		for col in row:
			if col == piece:
				return x, y
			x +=1
		y +=1
	return -1,-1

def can_fillX(p):
	p = p.upper()
	return (p != "P") and (p != "R") and (p != "B") and (p != "Q")

def check_pawn(board):
	x, y = get_piece_pos("P", board)

	if x == -1 and y == -1:
		return board
	board[y][x] = 'p'
	if y - 1 <  0: #bound check
		return board
	
	#top right check
	if not (x + 1 > len(board[0]) - 1):
		if (can_fillX(board[y - 1][x + 1])): 
			board[y - 1][x + 1] = 'X'
	
	#top left check
	if (not (x - 1 < 0)):
		if can_fillX(board[y - 1][x - 1]): 
			board[y - 1][x - 1] = 'X'

	# visulize_for_test(board, "Pawn") # for testing, this will be removed
	return board

def check_bishop(board, p):
	x, y = get_piece_pos(p, board)

	if x == -1 and y == -1:
		return board
	
	if p == "Q":
		board[y][x] = "Q"
	else:
		board[y][x] = 'b'
	new_y = y + 1 # top right
	for i in range(x + 1, len(board[y])):
		if new_y >= len(board):
			break
		if not can_fillX(board[new_y][i]):
			break
		board[new_y][i] = 'X'
		new_y += 1

	new_y = y - 1 # bottom left
	for i in range(x - 1, -1, -1):
		if new_y < 0:
			break
		if not can_fillX(board[new_y][i]):
			break
		board[new_y][i] = 'X'
		new_y -= 1

	new_y = y + 1 # top left
	for i in range(x - 1, -1, -1):
		if new_y >= len(board):
			break
		if not can_fillX(board[new_y][i]):
			break
		board[new_y][i] = 'X'
		new_y += 1

	new_y = y - 1 # bottom right
	for i in range(x + 1, len(board[y])):
		if new_y < 0:
			break
		if not can_fillX(board[new_y][i]):
			break
		board[new_y][i] = 'X'
		new_y -= 1

	# if p != "Q": visulize_for_test(board, "Bishop")
	return board

def check_rook(board, p):
	x, y = get_piece_pos(p, board)
	
	if x == -1 and y == -1:
		return board
	if p == "Q":
		board[y][x] = "q"
	else:
		board[y][x] = 'r'

	
	for i in range(x + 1, len(board[y])):
		if not can_fillX(board[y][i]): #found other piece blocking between path
			break
		board[y][i] = 'X'

	for i in range(x - 1, -1, -1):
		if not can_fillX(board[y][i]): #found other piece blocking between path
			break
		board[y][i] = 'X'

	for i in range(y + 1, len(board)):
		if not can_fillX(board[i][x]): #found other piece blocking between path
			break
		board[i][x] = 'X'

	for i in range(y - 1, -1, -1):
		if not can_fillX(board[i][x]): #found other piece blocking between path
			break
		board[i][x] = 'X'

	# if p != "Q": visulize_for_test(board, "Rook")
	return board


def check_queen(board):
	board = check_bishop(board, "Q")
	board = check_rook(board, "Q")
	# visulize_for_test(board, "Queen")
	return board

def check_cond(pos, board):
	match pos:
		case 'R':
			return check_rook(board, "R")
		case 'B':
			return check_bishop(board, "B")
		case 'P':
			return check_pawn(board)
		case'Q':
			return check_queen(board)
		case _:
			return board


def is_k_exist(board):
	for row in board:
		for col in row:
			if col == "K":
				return True
	return False

def has_err(board):
	for row in board: #check if board rectangle
		if len(row) != len(board):
			return True

	k_count = 0
	for row in board: #Must have only one K
		for col in row:
			if col == "K": 
				k_count += 1

	if k_count != 1: 
		return True
	return False

def in_check(b):
	board = [list(row) for row in b.split("\n")]
	if has_err(board):
		return -1
	for row in board:
		for position in row:
			board = check_cond(position, board)
	if is_k_exist(board):
		return False #Mean not in check
	return True #in check