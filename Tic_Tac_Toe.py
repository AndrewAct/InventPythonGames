######## Chapter 10 ########
####     Tic-Tac-Toe    ####

# List reference 
# Artificial intelligence
# Short circuti evaluation 
import random

def drawBoard(board):
	print(board[7]+ '|'+ board[8]+ '|'+ board[9])
	print('-+-+-')
	print(board[4]+ '|'+ board[5]+ '|'+ board[6])
	print('-+-+-')
	print(board[1]+ '|'+ board[2]+ '|'+ board[3])
	
def inputPlayerLetter():
	letter = ''
	while not (letter == 'X' or letter == 'O'):
		print('Do you want to be X or O ?')
		letter = input().upper()
		
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']
		
def whoGoesFirst():
	if random.randint(0, 1) == 0:
		return 'Computer'
	else:
		return 'Player'
		
def makeMove(board, letter, move):
	board[move] = letter 
	
def isWinner(bo,le):
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or 
	(bo[4] == le and bo[5] == le and bo[6] == le) or
	(bo[1] == le and bo[2] == le and bo[3] == le) or 
	(bo[7] == le and bo[4] == le and bo[1] == le) or 
	(bo[8] == le and bo[5] == le and bo[2] == le) or
	(bo[9] == le and bo[6] == le and bo[3] == le) or 
	(bo[7] == le and bo[5] == le and bo[3] == le) or 
	(bo[9] == le and bo[5] == le and bo[1] == le))
	
def getBoardCopy(board):
	boardCopy = []
	for i in bard:
		boardCopy.append(i)
	return boardCopy
	
def isSpaceFree(board, move):
	return boardMove == ' '
	
def getPlayerMove(board):
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(moove)):
		print(' What is your next move? (1-9')
		move = input()
	return int(move)
	
def chooseRandomMoveFromList(board, moveList):
	possibleMoves = []
	for i in moveList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
		
		if len(possibleMoves) != 0:
			return random.choice(possibleMoves)
		else:
			return None 
			
def getComputerMove(board, comuterLetter):
	if comuterLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'
		
	for i in range(1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, comuterLetter, i)
			if isWinner(boardCopy, comuterLetter):
				return i 
				
	for i in range(1, 10):
		boardCopy = getBoardCopy(board)
		if isSpaceFree(boardCopy, i):
			makeMove(boardCopy, playerLetter, i)
			if isWinner(boardCopy, playerLetter):
				return i
				
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move
		
	if isSpaceFree(board, 5):
		return 5
		
	return chooseRandomMoveFromList(board, [2,4,6,8])
	
def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
		return True

print('Welcome to Tic Tac Toe !')

while True:
	theBoard = [' ']* 10
	playerLetter, computerLetter = inputPlayerLetter()
	turn = whoGoesFirst()
	print('The '+ turn+ 'will go first.')
	gameIsPlaying = True
	
	while gameIsPlaying:
		if turn == 'Player':
			drawBoard(theBoard)
			makeMove(theBoard, playerLetter, move)
			
			if isWinner(theBoard, playerLetter):
				drawBoard(theBoard)
				print('Hooray! You win the game!')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is in a tie!')
					break
				else:
					turn = 'Computer'
					
		else:
			move = getComputerMove(theBoard, computerLetter)
			makeMove(theBoard, computerLetter, move)
			
			if isWinner(theBoard, computerLetter):
				drawBoard(theBoard)
				print('The computer won the game! You lose.')
				gameIsPlaying = False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print('The game is in a tie!')
					break
				else:
					turn = 'Player'
		print('Do you want to play one more time? (yes or no)')
		if not input().lower().startwith('y'):
			break