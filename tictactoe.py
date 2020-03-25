import random
import os


def DisplayBoard(board):
    os.system("cls")
    print("+-------+-------+-------+")
    for item in board:
        print("|       |       |       |")
        print("|  ", item[0], "  |  ", item[1], "  |  ", item[2], "  |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

		
def UpdateBoard(board, player, PlayerInput):
	global globalBoard
	board_dict = {1 : {"row": 0, "col": 0},
	2 : {"row": 0, "col": 1},
	3 : {"row": 0, "col": 2},
	4 : {"row": 1, "col": 0},
	6 : {"row": 1, "col": 2},
	7 : {"row": 2, "col": 0},
	8 : {"row": 2, "col": 1},
	9 : {"row": 2, "col": 2}}
	row = board_dict[PlayerInput]["row"]
	col = board_dict[PlayerInput]["col"]
	globalBoard[row][col] = player

	
def MakeListOfFreeFields(board):
    FreeFields = ()
    for item in board:
        if item[0] not in ("X", "O"):
            FreeFields += (item[0],)
        if item[1] not in ("X", "O"):
            FreeFields += (item[1],)
        if item[2] not in ("X", "O"):
            FreeFields += (item[2],)
    return FreeFields

	
def EnterMove(board):
	FreeFields = MakeListOfFreeFields(board)
	InputValid = False
	while not InputValid:
		UserInput = int(input("Enter your move: "))
		if UserInput in FreeFields:
			InputValid = True
			UpdateBoard(board, "O", UserInput)

	
def VictoryFor(board):
	for y in ("X", "O"):
		if (board[0][0], board[0][1], board[0][2]) == (y, y, y) or \
		(board[1][0], board[1][1], board[1][2]) == (y, y, y) or \
		(board[2][0], board[2][1], board[2][2]) == (y, y, y) or \
		(board[0][0], board[1][0], board[2][0]) == (y, y, y) or \
		(board[0][1], board[1][1], board[2][1]) == (y, y, y) or \
		(board[0][2], board[1][2], board[2][2]) == (y, y, y) or \
		(board[0][0], board[1][1], board[2][2]) == (y, y, y) or \
		(board[0][2], board[1][1], board[2][0]) == (y, y, y):
			if y == "X":
				DisplayBoard(board)
				print("You Lost!")
				os.system("pause")
				exit()
			elif y == "O":
				DisplayBoard(board)
				print("You Won!")
				os.system("pause")
				exit()
		elif len(MakeListOfFreeFields(board)) == 0:
			DisplayBoard(board)
			print("Tie Game!")
			os.system("pause")
			exit()

	

def DrawMove(board):
	FreeFields = MakeListOfFreeFields(board)
	ComputerInput = random.choice(FreeFields)
	UpdateBoard(board, "X", ComputerInput)


globalBoard = [[1, 2, 3],
	[4, "X", 6],
	[7, 8, 9]]

	
i = 1

while i < 5:
	DisplayBoard(globalBoard)
	EnterMove(globalBoard)
	DrawMove(globalBoard)
	VictoryFor(globalBoard)
	i += 1
