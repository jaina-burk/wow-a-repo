import os
from time import sleep

# A game of hangman

### Functions ###

# Displays the current blanks and letters guessed
def hangman_header():
    print(hangman_word)

# Checks the guess against word. Then replaces _ in hangman_word
def check_letter():
    word_index = 0
    for letter in word:
        if guess == word[word_index]:
            hangman_word[word_index] = guess
            word_index = word_index + 1
        else:
            word_index = word_index + 1
            

### Main Loop ###

word = ' '
initial_word = ' '
hangman_word = []

# Asks for input from the user

print('Welcome to a game of Hangman!')
word = input('Please enter a word to start: ').lower()

initial_word = word
word = list(word)
number_guesses = 5
final_guesses = 0

# Convert the word into a series of _ for the player
for letter in word:
    hangman_word.append('_')

print(hangman_word)


while number_guesses > 0:
    if hangman_word == word:
        final_guesses = number_guesses
        number_guesses = 0
    else:
        os.system('cls')
        hangman_header()
        print("\nYou have %s guesses left." % number_guesses)
        guess = input('\nGuess a letter:').lower()
        if len(guess) > 1:
            print("Please type just one letter.")
            sleep(2)
        elif guess in hangman_word:
            print("You already guessed that letter.")
            sleep(2)
        elif guess in word:
            check_letter()
        else:
            number_guesses = number_guesses - 1
            print("That letter is not in the word.")
            sleep(2)


os.system('cls')
if final_guesses == 0:
    print('You ran out of guesses. Here is the word:')
    print(word)
    print('Thanks for playing!')
else:
    hangman_header()
    print("You did it! Congrats! You had %s guesses left." % final_guesses)
    print("Thanks for playing!")
