from lexicon import Lexicon

ENGLISH_WORDS = '../words/en.txt'

def createLexicon():
	lexicon = Lexicon()
	wordsFile = open(ENGLISH_WORDS, 'r')
	print '=== CREATING LEXICON ==='
	print '=== READING WORDS FILE ==='
	for word in wordsFile:
		lexicon.addWord(word)
	print '=== LEXICON CREATED ==='
	return lexicon



def getWords(board):
	lexicon = createLexicon()
	letters = []
	for row in board:
		for letter in row:
			letters.append(letter)
	print '=== CREATING POSSIBLE WORDS ==='
	return searchForWords(letters, lexicon, '')

def searchForWords(letters, lexicon, word):
	words = set()
	for letter in letters:
		if lexicon.hasWord(word + letter):
			words.add(word+letter)
		elif lexicon.beginsWith(word + letter):
			newLetters = list(letters)
			newLetters.remove(letter)
			newWord = word + letter
			words = words | searchForWords(newLetters, lexicon, newWord)
	return words

