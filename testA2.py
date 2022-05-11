p1='x'
p2='o'

def isMoveLeft(board):
	for i in range(3):
		for j in range(3):
			if board[i][j]=='_':
				return True
	return False

def checkVal(board):
	for i in range(3):
		if board[i][0]==board[i][1] and board[i][1]== board[i][2]:
			if board[i][0] == p1:
				return 10
			else:
				return -10

	for i in range(3):
		if board[0][i]==board[1][i] and board[1][i]== board[2][i]:
			if board[0][i] == p1:
				return 10
			else:
				return -10

	if board[0][0] == board[1][1]  and board[1][1]==board[2][2]:
		if board[0][i] == p1:
			return 10
		else:
			return -10

	if board[2][0] == board[1][1]  and board[1][1]==board[2][0]:
		if board[0][i] == p1:
			return 10
		else:
			return -10

def minmax(board,ismax):
	score = checkVal(board)
	if score == 10:
		return score
	if score == -10:
		return score
	if isMoveLeft(board):
		return 0

	if ismax:
		bestScore=-1000

		for i in range(3):
			for j in range(3):
				if board[i][j]=='_':
					board[i][j]=p1
					bestScore= max(bestScore,minmax(board, not ismax))
					board[i][j]='_'
		return bestScore
	else:
		bestScore=1000
		for i in range(3):
			for j in range(3):
				if board[i][j]=='_':
					board[i][j]=p2
					bestScore = min(bestScore,minmax(board,not ismax))
					board[i][j]='_'
		return bestScore

def maxscore(board):
	bestScore=-1000
	bestMove=(-1,-1)
	for i in range(3):
		for j in range(3):
			if board[i][j]=='_':
				board[i][j]=p1
				bestVal = minmax(board,False)
				board[i][j]='_'
				if bestVal>bestScore:
					bestMove=(i,j)
					bestScore=bestVal

	return bestMove

board=[
	['x','o','x'],
	['o','o','x'],
	['_','_','_']
]
bestMove= maxscore(board)

print(bestMove)