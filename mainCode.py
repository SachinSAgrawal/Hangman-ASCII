'''
Sachin Agrawal
June 30th, 2021
Hangman.py
Play the classic game of hangman with ASCII art visuals!
'''

import random

# List of curated words to choose from
wordList = ["astronaut", "library", "police", "monkey", "raspberry", "standard", "globes", "javascript", "violin", "eunoia"]
# Select a random word from the list
secretWord = random.choice(wordList)

# Open a file containing the 10000 most common words to use as secret words
with open('wordList.txt') as file:
    # Read words from the file and split them into a list
    commonWords = file.read().splitlines()
# Filter out short words from the list of common words
longWords = [word for word in commonWords if len(word) > 4]
# Choose a random long word as the secret word
secretWord = random.choice(longWords)

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
    # Maximum number of incorrect tries allowed
    incorrectTries = 8
    # Set to store guessed letters
    guessedLetters = set()
    # Counter for incorrect guesses
    incorrectCount = 0
    # Main game loop
    while incorrectTries > 0:
        # Display the hangman visuals
        visual(incorrectCount)
        # Get user's guess
        userGuess = getGuess(guessedLetters)
        # Update the dashed word and incorrect count based on the guess
        dashedWord, incorrectCount = updateDashes(secretWord, dashedWord, userGuess, incorrectCount)
        print("\n" + dashedWord)
        # Add the guessed letter to the set
        guessedLetters.add(userGuess)
        # Calculate remaining incorrect tries
        incorrectTries = 8 - incorrectCount
        print("\nYou have", incorrectTries, "incorrect tries remaining.")
        # Check if the secret word has been guessed correctly
        if dashedWord == secretWord:
            print("\nCongratulations! You have guessed the word!")
            break
    # If the player runs out of tries without guessing the word
    if incorrectTries == 0 and dashedWord != secretWord:
        visual(incorrectCount)
        print("\nBetter luck next time!")
        print("\nThe secret word is " + secretWord + ".")

# Main function to start the game
def main():
    print("Play a game of Hangman with ASCII art visuals!\n")
    print("Try to guess the word in a certain number of tries.\n")
    print("Good luck!\n")
    # Start the game
    update()

# Function to display ASCII art visuals representing the hangman
def visual(count):
    if count == 0:
        print('''
               +---+
               |   |
                   |
                   |
                   |
                   |
             =========''')
    elif count == 1:
        print('''
               +---+
               |   |
               O   |
                   |
                   |
                   |
                   |
             =========''')
    elif count == 2:
        print('''
               +---+
               |   |
               O   |
               |   |
                   |
                   |
                   |
             =========''')
    elif count == 3:
        print('''
               +---+
               |   |
               O   |
              /|   |
                   |
                   |
                   |
             =========''')
    elif count == 4:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
                   |
                   |
                   |
             =========''')
    elif count == 5:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
               |   |
                   |
                   |
             =========''')
    elif count == 6:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
               |   |
              /    |
                   |
             =========''')
    elif count == 7:
        print('''
               +---+
               |   |
               O   |
              /|\\  |
               |   |
              / \\  |
                   |
             =========''')
    elif count == 8:
        print('''
               +---+
               |   |
               X   |
              /|\\  |
               |   |
              / \\  |
                   |
             =========''')

# Entry point of the program
if __name__ == "__main__":
    main()