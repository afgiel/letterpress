from lexicon import Lexicon

ENGLISH_WORDS = '../words/en.txt'

def create_lexicon():
	lexicon = Lexicon()
	words_file = open(ENGLISH_WORDS, 'r')
	print '=== CREATING LEXICON ==='
	print '=== READING WORDS FILE ==='
	for word in words_file:
		lexicon.add_word(word)
	print '=== LEXICON CREATED ==='
	return lexicon

def get_words(board):
	lexicon = create_lexicon()
	letters = []
	for row in board:
		for letter in row:
			letters.append(letter)
	print '=== CREATING POSSIBLE WORDS ==='
	return search_for_words(letters, lexicon, '')

def search_for_words(letters, lexicon, word):
	words = set()
	for letter in letters:
		if lexicon.has_word(word + letter):
			words.add(word+letter)
		if lexicon.begins_with(word + letter):
			new_letters = list(letters)
			new_letters.remove(letter)
			new_word = word + letter
			words = words | search_for_words(new_letters, lexicon, new_word)
	return words

