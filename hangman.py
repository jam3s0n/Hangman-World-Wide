#Hangman program(theme: Countries)

import random
import pyfiglet
from termcolor import colored

HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     === ''', '''
  +---+
  O   |
      |
      |
     === ''', '''
  +---+
  O   |
  |   |
      |
     === ''', '''
  +---+
  O   |
 /|   |
      |
     === ''', '''
  +---+
  O   |
 /|\  |
      |
     === ''', '''
   +---+
   O   |
  /|\  |
  /    |   
      === ''', '''
   +---+
   o   |
  /|\  |
  / \  |
      === ''']

# List of countries wordbank
words = ['United States', 'Denmark', 'Finland', 'Japan', 'Ireland', 'Netherlands', 'China', 'Iran', 'Argentina', 'Mexico', 'South Africa',
         'France', 'Russia', 'Hungary', 'Chile', 'Costa Rica', 'Germany', 'Singapore', 'Thailand', 'Greece', 'Norway', 'Sweden', 'Albania', 'Iraq',
         'Dominican Republic', 'Philippines', 'New Zealand', 'Portugal', 'Rwanda', 'India', 'Canada', 'Brazil', 'Kazakhstan', 'Mongolia', 'Sudan',
         'Nigeria', 'Pakistan', 'Turkey', 'Somalia', 'Ukraine', 'Spain', 'Syria', 'United Kingdom', 'French Guiana', 'Peru', 'Argentina', 'Kazakhstan']


# picks country
def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end= '')
    print()
    
    blanks = ''
    for i in range(len(secretWord)):
        if secretWord[i] == ' ' :
            blanks = blanks + ' '
        else:
            blanks = blanks + '_'



    for i in range(len(secretWord)):
        if secretWord[i].lower() in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
      print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False
# need a copy fo the secret word that is closer to user input(no caps/spaces)
sWordbuf = ''.join(secretWord.split()).lower()

# Opening display
introText = "HangMan: \nWorldWide"
introArt = pyfiglet.figlet_format(introText, font = "larry3d")

print(colored(introArt, 'green'))

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in sWordbuf:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(sWordbuf)):

            if sWordbuf[i] not in correctLetters:
                foundAllLetters = False
                break
            
        # win scenario
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess
        
        # lose scenario
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            # reset
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getRandomWord(words)
            sWordbuf = ''.join(secretWord.split()).lower()

        else:
            break
            
            
            

