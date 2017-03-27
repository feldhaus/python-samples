import random, string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    '''
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    
    returns (list): all words loaded
    '''
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    '''
    Returns a word from wordlist at random.
    
    wordlist (list): list of words (strings)
    '''
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    Returns if all letters was discovered.
    
    secretWord (string): the word the user is guessing
    lettersGuessed (list): what letters have been guessed so far
    
    returns (boolean): True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    l = list(secretWord)
    for c in lettersGuessed:
        while c in l:
            l.remove(c)
    return len(l) == 0

def getGuessedWord(secretWord, lettersGuessed):
    '''
    Returns the guessed word, with underscore in the letters not guessed.
    
    secretWord (string): the word the user is guessing
    lettersGuessed (list) what letters have been guessed so far
    
    returns (string): comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = []
    
    for c in secretWord:
        guessedWord.append(c if c in lettersGuessed else '_')
            
    return " ".join(guessedWord)

def getAvailableLetters(lettersGuessed):
    '''
    Returns all available letters.
    
    lettersGuessed (list): what letters have been guessed so far
    returns (string): comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = list(string.ascii_lowercase)
    
    for c in lettersGuessed:
        if c in availableLetters:
            availableLetters.remove(c)
            
    return "".join(availableLetters)

def hangman(secretWord):
    '''
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
    
    secretWord (string): the secret word to guess.
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
            
            if guess in secretWord:
                if isWordGuessed(secretWord, lettersGuessed):
                    break
            else:
                guesses -= 1
                
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            availableLetters = getAvailableLetters(lettersGuessed)
            print("{0}  ♥({1}) [{2}]".format(guessedWord, guesses, availableLetters))
            
    print("-------------")
    if guesses > 0:
        print("Congratulations, you won! The word was: '{0}'".format(secretWord))
    else:
        print("Sorry, you ran out of guesses. The word was: '{0}'".format(secretWord))

# load the list of words into the variable wordlist
wordlist = loadWords()
# choose a word
secretWord = chooseWord(wordlist).lower()
# start the hangman game
hangman(secretWord)