EMPTY_COLOR = 0
MIN_COLOR = 1
MAX_COLOR = 2

class Game:

    def __init__(self, board):
        self.letter_board = board
        self.color_board = [[EMPTY_COLOR for x in range(len(board))] for y in range(len(board[0]))]
        self.lock_board = [[False for x in range(len(board))] for y in range(len(board[0]))]

    def set_color(self, x, y, color):
        self.color_board[x][y] = color

    def get_color(self, x, y):
    	return self.color_board[x][y]

    def get_lock_status(self, x, y):
    	return self.lock_board[x][y]

    def lock_colors(self):
    	for i in range(len(self.color_board)):
    		for j in range(len(self.color_board[0])):
    			if self.neighbors_match(i, j): 
    				self.lock_board[i][j] = True
    			else:
    				self.lock_board[i][j] = False

    def neighbors_match(self, x, y):
    	to_match = self.color_board[x][y]
    	for i in range(x-1, x+2):
    		for j in range(y-1, y+2):
    			if self.in_range(x, y, i, j):
    				if not self.color_board[i][j] == to_match:
    					return False
    	return True

    def in_range(self, x, y, i, j):
    	return i >= 0 and j >=0 and i < len(self.color_board) and j < len(self.color_board[0]) and abs(x-i) + abs(y-j) < 2