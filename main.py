# Hangman

from functions import split  # Needed to store functions in a separate file
from random_word import RandomWords  # Needed to get a random word from the list of words

# Error message for when the user enters an invalid number
invalidNumber = "Your number must be an integer equal to or greater than 1.\n"


while True:
    try:
        chances = int(
            input(
                "How many chances do you want? Please reply with an integer equal to or greater than 1. \n"
            )
        )
        print("")

    except ValueError:
        print(invalidNumber)
        continue

    if chances < 1:
        print(invalidNumber)
        continue

    while chances != 0:
        # Defines the variables for the hangman
        randomWord = RandomWords().get_random_word()  # Gets a random word from the RandomWords library
        splitWord = split(randomWord)  # Splits that word into single characters
        blankWord = "_" * len(randomWord)  # Prints as many "_" as there are characters for the selected word
        splitBlankWord = split(blankWord)  # Splits the blank word into single characters

        print(f"The word you have to guess is {len(randomWord)} characters long. Good luck! \n")

        while chances != 0 and splitBlankWord != splitWord:
            guess = input(f"Guess a letter: {splitBlankWord}\n").lower()

            if guess in splitWord:
                for i in range(len(splitWord)):
                    if splitWord[i] != guess:
                        continue
                    splitBlankWord[i] = guess
                print(f"Correct guess! \"{guess}\" is a character in the word.")
                print(f"You still have {chances} chances left. \n")

            else:
                chances = chances - 1
                print(f"Incorrect guess. \"{guess}\" is not a character in the word.")
                print(f"You now have {chances} chances left. \n")

        if splitBlankWord == splitWord:
            print(splitBlankWord)
            print(f"You have guessed the correct word! The word was \"{randomWord}\"\n")

            while True:
                playAgain = str.lower(input('Would you like to play again? (Y/n): '))
                if playAgain == "y":
                    chances = 0
                    break
                elif playAgain == "n":
                    print('Thanks for playing! Terminating program...')
                    quit()
                else:
                    print('Input not recognized.')
                    continue

        elif chances == 0:
            print(f"You have run out of chances. The word was \"{randomWord}\"\n")
            break
