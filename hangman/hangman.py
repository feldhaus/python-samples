import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
	"""
	Returns a list of valid words. Words are strings of lowercase letters.
	
	Depending on the size of the word list, this function may
	take a while to finish.
	"""
	print("Loading word list from file...")
	# inFile: file
	inFile = open(WORDLIST_FILENAME, 'r')
	# line: string
	line = inFile.readline()
	# wordlist: list of strings
	wordlist = line.split()
	print("  ", len(wordlist), "words loaded.")
	return wordlist

def chooseWord(wordlist):
	"""
	wordlist (list): list of words (strings)
	
	Returns a word from wordlist at random
	"""
	return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: boolean, True if all the letters of secretWord are in lettersGuessed;
	  False otherwise
	'''
	l = list(secretWord)
	for c in lettersGuessed:
		while c in l:
			l.remove(c)
	return len(l) == 0


def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
	  what letters in secretWord have been guessed so far.
	'''
	guessedWord = []
    
	for c in secretWord:
		"""
        if c in lettersGuessed:
            guessedWord += c
		else:
            guessedWord += "_ "
		"""
		guessedWord.append(c if c in lettersGuessed else '_')
            
	return " ".join(guessedWord)


def getAvailableLetters(lettersGuessed):
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	  yet been guessed.
	'''
	availableLetters = list(string.ascii_lowercase)
	
	for c in lettersGuessed:
	    if c in availableLetters:
	        availableLetters.remove(c)
	        
	return "".join(availableLetters)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guesses = 8
    lettersGuessed = []
    
    print("Welcome to the game, Hangman! ")
    print("I am thinking of a word that is {0} letters long.".format(len(secretWord)))
    while(guesses > 0):
    	guess = input("Please guess a letter: ")
    	
    	if guess in lettersGuessed:
    		continue
    	else:
    		lettersGuessed.append(guess.lower())
    		
    		if guess not in secretWord:
    			guesses -= 1
    		
    		guessedWord = getGuessedWord(secretWord, lettersGuessed)
    		availableLetters = getAvailableLetters(lettersGuessed)
    		print("{0}  ♥({1}) [{2}]".format(guessedWord, guesses, availableLetters))

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)