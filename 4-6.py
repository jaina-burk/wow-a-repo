import random
import os
from time import sleep

guess = 0
number_guess = 0
number = random.randint(1,9)

while guess != 'exit':
    os.system('cls')
    guess = input("Guess the number between 1 and 9. Type exit to quit: ")
    number_guess += 1
    if number == int(guess):
        print("That's right! Great guess")
        print("It took you %s guesses." % number_guess)
        sleep(2)
        guess = 'exit'
    elif number > int(guess):
        print("You are too low")
        sleep(2)
    elif number < int(guess):
        print("You are too high.")
        sleep(2)
    elif number == 'exit':
        print("Thanks for playing!")
        sleep(2)
        guess = 'exit'

