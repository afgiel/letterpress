from lex_node import *

START = '<START>'
END = '<END>'

class Lexicon:

	def __init__(self):
		self.root = LexNode(START)

	def add_word(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.has_next(letter):
				curr = curr.get_next(letter)
			else:
				new_node = LexNode(letter)
				curr.add_next(new_node)
				curr = new_node
		end_node = LexNode(END)
		curr.add_next(end_node)

	def has_word(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.has_next(letter):
				curr = curr.get_next(letter)
			else:
				return False
		return curr.has_next(END)

	def begins_with(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.has_next(letter):
				curr = curr.get_next(letter)
			else:
				return False
		return True
