from random import randrange
from string import *

# Global Constants
MAX_GUESSES = 6
WORDLIST_FILENAME = "words.txt"


# Load word to play hangman
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split(' ')
    print(len(wordlist), "words loaded.")
    return wordlist


# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program

words_dict = load_words()


# new_word returns a random word from the global words list (word_dict)
def new_word():
    word = words_dict[randrange(0, len(words_dict))]
    return word


# word_guessed returns true if the secret word is guessed (i.e. every
# character in secret_word is in letters_guessed), and false otherwise
# requires: secret_word is a lowercase alphabetic string
#           letters_guessed is a list of lowercase alphabets
def word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


# print_progress prints out the secret words with correctly guessed
# letters revealed in hangman style_
# requires: secret_word is a lowercase alphabetic string
#           letters_guessed is a list of lowercase alphabets
# Example: print_progress("telephone", ['a', 'e', 's', 't']) prints
#          t e _ e _ _ _ _ e     and additional spacing for clarity
#
def print_progress(secret_word, letters_guessed):
    print('')
    for letter in secret_word:
        if letter in letters_guessed:
            print(letter, end = ' ')
        else:
            print('_', end = ' ')
    print('')
    print('')


# play_game is the main game function
def play_game():
    # Outer loop creates new game until user replies with 'no' when
    # asked if they want to play again
    while True:
        secret_word = new_word()
        letters_guessed = []
        mistakes_made = 0

        # Inside loop makes the game progress. The loop is terminated once
        # the game is over (correct word guessed or no more guesses left)
        while True:
            print(MAX_GUESSES - mistakes_made, 'incorrect guesses left')
            print_progress(secret_word, letters_guessed)

            guess = input('Enter your guess as a lower case alphabet: ')
            print('--------------------------------------------------------------')

            # This implementation does not count guessing a previously guessed
            # letter as a mistake, instead the user is prompted to try again
            guessed_before = guess in letters_guessed
            while guessed_before:
                guess = input('Letter already guessed, try again: ')
                guessed_before = guess in letters_guessed
                
            letters_guessed.append(guess)
            if word_guessed(secret_word, letters_guessed):
                print('Congratulations! You have guessed the word correctly.')
                print('The word was', secret_word)
                print('')
                break

            
            if guess in secret_word:
                print('Your guessed letter is in the word!')
            else:
                print('Your guess is not in the word.')
                mistakes_made += 1

            if MAX_GUESSES - mistakes_made == 0:
                print('No more guesses left. Better luck next time!')
                print('The word was', secret_word)
                print('')
                break

        # Game is over by this point
        print('Do you want to play again?')
        new_game = input('Enter yes or no: ')
        if new_game == 'no':
            break   # terminates the outer loop
    print('Thanks for playing!')

# Main function called to begin game
play_game()
