import string

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    """
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    """
    lettersAvailable = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        lettersAvailable.remove(letter)
    return ''.join(lettersAvailable)


print(getAvailableLetters(lettersGuessed))
