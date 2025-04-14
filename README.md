# Hangman ASCII

## About
Play the classic game of Hangman by guessing a secret word, with this Python implementation including optional ASCII art visuals to represent the figure and post. This game also has other options to configure the gameplay. If you like this game, I would appreciate if you starred it or even shared it with your friends.

## Instructions
* You will be presented with a series of dashes representing the letters of a secret word.
* Guess letters by inputting them one at a time.
* If the letter is in the secret word, the corresponding dashes will be replaced with that letter.
* If the letter is not in the secret word, a part of the figure will be drawn.
* You have 8 incorrect guesses before the figure is fully drawn and the game ends.
* Try to guess the word before the hangman is completed to win!

## Installation
1. Clone this repository or download it as a zip folder and uncompress it.
2. Navigate to the directory in Terminal that contains all the files. 
3. Run `python3 mainCode.py` to start and follow the instructions above.

#### Prerequisites
Hopefully this goes without saying, but you need Python 3.x installed.

#### Notes
This can also be pretty easily run on [Replit](https://replit.com/) if you copy and paste all the associated files into a new project.

## Configuration
Modify the following options in the [config](config.json) file.

- `useCuratedWords`: Whether or not to use a set of words curated by me. Otherwise, the words will be taken from a list of the 10,000 most common in the English language, but be warned that some of them may be NSFW.
- `debugEnabled`: Whether or not to show the secret word at the start of the game.
- `showVisuals`: Whether or not the ASCII visuals will be displayed.
- `minWordLength`: If not using the curated words, the shortest a word can be.
- `maxWordLength`: If not using the curated words, the longest a word can be.

## Contributors
Sachin Agrawal: I'm a self-taught programmer who knows many languages and I'm into app, game, and web development. For more information, check out my website or Github profile. If you would like to contact me, my email is [github@sachin.email](mailto:github@sachin.email).

## License
This package is licensed under the [MIT License](LICENSE.txt).
