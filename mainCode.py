'''
Sachin Agrawal
June 30th, 2021
Hangman.py
Play the classic game of Hangman by guessing a secret word with optional ASCII art visuals!
'''

import random
import json
from visuals import visual  # Import the visual function

# Load configuration from config.json
with open('config.json') as config_file:
    config = json.load(config_file)

# Determine the secret word based on the configuration
if config.get("useCuratedWords", False):
    # List of curated words to choose from
    wordList = ["astronaut", "library", "police", "monkey", "raspberry", "standard", "globes", "javascript", "violin", "eunoia"]
    # Select a random word from the list
    secretWord = random.choice(wordList)
else:
    # Open a file containing the 10000 most common words to use as secret words
    with open('wordList.txt') as file:
        # Read words from the file and split them into a list
        commonWords = file.read().splitlines()
    # Filter words based on min and max length from the configuration
    minLength = config.get("minWordLength", 5)
    maxLength = config.get("maxWordLength", 15)
    # Automatically swap bounds if minLength is greater than maxLength
    if minLength > maxLength:
        minLength, maxLength = maxLength, minLength
    filteredWords = [word for word in commonWords if minLength <= len(word) <= maxLength]
    # Choose a random word from the filtered list
    secretWord = random.choice(filteredWords)

# Function to update the dashes representing the secret word
def updateDashes(secretWord, dashedWord, userGuess, incorrectCount):
    updatedDashes = dashedWord
    if userGuess in secretWord:
        # Replace dashes with correctly guessed letters
        updatedDashes = ''.join([char if char == userGuess or dashedWord[i] != '_' else '_' for i, char in enumerate(secretWord)])
    else:
        # Increment the count of incorrect guesses
        incorrectCount += 1
    return updatedDashes, incorrectCount

# Function to get user's guess
def getGuess(guessedLetters):
    while True:
        userGuess = input("\nGuess a character: ").lower()
        if len(userGuess) != 1 or not userGuess.isalpha():
            # Check if the input is a single alphabetic character
            print("\nPlease enter a single alphabetic character.")
        elif userGuess in guessedLetters:
            # Check if the letter has already been guessed
            print("\nThat letter has already been guessed!")
        else:
            return userGuess

# Function to update the game state
def update():
    # Initialize the dashed word representation of the secret word
    dashedWord = '_' * len(secretWord)
    print("\n" + dashedWord)
    print("\nYou have 8 incorrect tries remaining.")
    # Maximum number of incorrect tries allowed
    incorrectTries = 8
    # Set to store guessed letters
    guessedLetters = set()
    # Counter for incorrect guesses
    incorrectCount = 0
    # Main game loop
    while incorrectTries > 0:
        # Display the hangman visuals if enabled
        if config.get("showVisuals", True):
            visual(incorrectCount)
        # Get user's guess
        userGuess = getGuess(guessedLetters)
        # Update the dashed word and incorrect count based on the guess
        dashedWord, incorrectCount = updateDashes(secretWord, dashedWord, userGuess, incorrectCount)
        print("\n" + dashedWord)
        # Add the guessed letter to the set
        guessedLetters.add(userGuess)
        # Check if the secret word has been guessed correctly
        if dashedWord == secretWord:
            print("\nCongratulations! You have guessed the word!")
            if config.get("showVisuals", True):
                visual(incorrectCount)
            print("")
            break
        # Calculate remaining incorrect tries
        incorrectTries = 8 - incorrectCount
        print("\nYou have", incorrectTries, "incorrect tries remaining.")
    # If the player runs out of tries without guessing the word
    if incorrectTries == 0 and dashedWord != secretWord:
        if config.get("showVisuals", True):
            visual(incorrectCount)
        print("\nBetter luck next time!")
        print("\nThe secret word is " + secretWord + ".\n")

# Main function to start the game
def main():
    # Print the secret word if debug mode is enabled
    if config.get("debugEnabled", False):
        print(f"\nDEBUG: The secret word is '{secretWord}'")
    print("\nPlay the classic game of Hangman by guessing a secret word.")
    if config.get("showVisuals", True):
        print("\nASCII art visuals are currently enabled.")
    else:
        print("\nASCII art visuals are currently disabled.")
    print("\nGood luck!")
    # Start the game
    update()

# Entry point of the program
if __name__ == "__main__":
    main()