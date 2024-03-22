# Hangman

import random  # Needed to get a random word from the list of words
from functions import split  # Needed to store functions in a separate file

# Error message for when the user enters an invalid number
invalidNumber = "Your number must be an integer equal to or greater than 1."

# List of words
words = ["dog", "cat", "human", "teacher"]

while True:
    try:
        chances = int(
            input(
                "How many chances do you want? Please reply with an integer equal to or greater than 1. "
            )
        )
    except ValueError:
        print(invalidNumber)
        continue

    if chances < 1:
        print(invalidNumber)
        continue

    while chances != 0:
        # Defines the variables for the hangman
        selectedWord = random.choice(
            words
        )  # Picks a random word from the words list
        splitWord = split(selectedWord)  # Splits that word into single characters
        blankWord = "_" * len(
            selectedWord
        )  # Prints as many "_" as there are characters for the selected word
        splitBlankWord = split(
            blankWord
        )  # Splits the blank word into single characters

        while chances != 0 and splitBlankWord != splitWord:
            guess = input(f"Guess a letter: {splitBlankWord}").lower()

            if guess in splitWord:
                for i in range(len(splitWord)):
                    if splitWord[i] != guess:
                        continue
                    splitBlankWord[i] = guess

            else:
                print(f"Incorrect guess. {guess} is not a character in the word. ")
                chances = chances - 1

        if splitBlankWord == splitWord:
            print(splitBlankWord)
            print(f"You have guessed the correct word! The word was \"{selectedWord}\"")

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
