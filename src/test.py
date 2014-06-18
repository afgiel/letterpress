import getWords 
import game 

board = [['a', 'b', 'c', 'd', 'e']]
state = game.Game(board)
state.setColor(0, 0, game.MAX_COLOR_UNLOCKED)
state.setColor(0, 1, game.MAX_COLOR_UNLOCKED)
state.setColor(1, 0, game.MAX_COLOR_UNLOCKED)
state.lockColors()
print state.getColor(0, 0), 'should be 2'
state.setColor(0, 1, game.MIN_COLOR_UNLOCKED)
state.lockColors()
print state.getColor(0, 0), 'should be 1'