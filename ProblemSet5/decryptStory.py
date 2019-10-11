from ProblemSet5.ps6 import *


def decrypt_story():
    encryptedStory = get_story_string()
    decryptedStory = CiphertextMessage(encryptedStory)
    return decryptedStory.decrypt_message()
