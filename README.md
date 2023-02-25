# Computer-Guessing-the-number

This is a number guessing game in which the computer tries to guess the number selected by the user.

The user must specify the upper limit so that the system knows the range within which to select a number.

After the user specifies the upper limit, the computer starts guessing a number. 

If the number guessed by the computer is higher than the user's selected number, the user enters 'h' to indicate that the computer needs to guess a lesser number. The upper limit is then changed to 'guess-1'. 

Conversely, if the number guessed by the computer is lower than the user's selected number, the user enters 'l' to indicate that the computer needs to guess a higher number. The lower limit is then set to 'guess+1'. 

If the computer correctly guesses the number, the user enters 'c', and the program ends by displaying the number of attempts it took to guess the correct number.
