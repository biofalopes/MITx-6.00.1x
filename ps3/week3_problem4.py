import string


def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    done = True
    for letter in secretWord:
        if letter in lettersGuessed:
            done = True
        else:
            return not done
    return done


def getGuessedWord(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    """
    for letter in secretWord:
        if letter not in lettersGuessed:
            secretWord = secretWord.replace(letter, '_ ')
    return secretWord


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    lettersAvailable = list(string.ascii_lowercase)
    for i in lettersGuessed:
        lettersAvailable.remove(i)
    return ''.join(lettersAvailable)


def hangman(secretWord):
    """
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
    """

    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")

    guesses = 8
    lettersGuessed = []

    while guesses > 0:
        print("You have " + str(guesses) + " guesses left.")
        print("Available letters: " + getAvailableLetters(lettersGuessed))
        letter = input("Please guess a letter: ")
        if letter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += letter
            if letter in secretWord:
                print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
        print("------------")
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        elif guesses == 0:
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")




secretWord = "sea"
hangman(secretWord)
