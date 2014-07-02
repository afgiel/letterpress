import get_words 
import game

board = [['a', 'b', 'c', 'd', 'e']]*5
state = game.Game(board)
state.set_color(0, 0, game.MAX_COLOR)
state.set_color(0, 1, game.MAX_COLOR)
state.set_color(1, 0, game.MAX_COLOR)
state.lock_colors()
print state.get_lock_status(0, 0), 'should be True'
state.set_color(0, 1, game.MIN_COLOR)
state.lock_colors()
print state.get_lock_status(0, 0), 'should be False'