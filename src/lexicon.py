from lexNode import *

START = '<START>'
END = '<END>'

class Lexicon:

	def __init__(self):
		self.root = LexNode(START)

	def addWord(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.hasNext(letter):
				curr = curr.getNext(letter)
			else:
				newNode = LexNode(letter)
				curr.addNext(newNode)
				curr = newNode
		endNode = LexNode(END)
		curr.addNext(endNode)

	def hasWord(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.hasNext(letter):
				curr = curr.getNext(letter)
			else:
				return False
		return curr.hasNext(END)

	def beginsWith(self, word):
		curr = self.root
		word = word.strip()
		for letter in word:
			if curr.hasNext(letter):
				curr = curr.getNext(letter)
			else:
				return False
		return True
