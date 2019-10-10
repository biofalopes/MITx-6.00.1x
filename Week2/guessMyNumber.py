print("Please think of a number between 0 and 100!")

midval = 50
ans = None
minval = 0
maxval = 100

while ans != 'c':
    midval = (minval + maxval) // 2
    print('Is your secret number ' + str(midval) + '?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to "
                "indicate I guessed correctly.")
    if ans == 'l':
        minval = midval
    elif ans == 'h':
        maxval = midval
    elif ans == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')

print("Game over. Your secret number was: " + str(midval))
