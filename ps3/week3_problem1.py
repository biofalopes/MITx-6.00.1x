

def isWordGuessed(secretWord, lettersGuessed):
    """
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    """
    for letter in secretWord:
        if letter in lettersGuessed:
            lettersGuessed.remove(letter)
            result = True
        else:
            result = False
            break
    return result


secretWord = 'ba'
lettersGuessed = ['a', 'b', 'c']

print(str(isWordGuessed(secretWord, lettersGuessed)))
