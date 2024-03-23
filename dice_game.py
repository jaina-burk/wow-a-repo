# Dice Game - A Game where you roll dice and buy power ups
# The goal of the game is to last as many rounds as possible before you run out of money

import os
from time import sleep
import random

###### Definitions ######

def header():
    print("*****************************************")
    print("*****           Dice Time           *****")
    print("*****************************************")

def gameheader():
    os.system('cls')
    print("***********************************************")
    print(" Coins:%s                            Round:%s" % (coins, round_number))
    print("                                     Multiplier: %s" % multiplier)
    print(" Power Ups: %s                               " % powerups)
    print("***********************************************")

def calculate_roll():
    result = random.randint(1,dice_max)
    return result

def roll():
    roll_result = calculate_roll()
    return roll_result

###### Main Loop ######
startgame = 0

while startgame != 'q':
    os.system('cls')
    header()
    print("\nWelcome to Dice Time!\n")
    print("In this game, you start with 10 coins.\n")
    print("Each roll you bet up to 5 coins.  Beat the required number, you get X multiplier coins back\n")
    print("After 3 rounds, you get a chance to buy power ups.\n")

    startgame = input("Enter [1] to begin, or [q] to quit: ")
    while startgame == '1':
        round_number = 1
        coins = 10
        powerups = None
        dice_max = 6
        startgame = 'a'
    
    while startgame =='a':
        coins_bet = 0
        beat_number = 2
        multiplier = 2
        gameheader()
        print("\nThe number to beat is %s" % beat_number)
        coins_bet = input("\nHow many coins would you like to bet? (Max 5): ")
        if coins_bet < 1:
            print("Please enter a number between 1 and 5")
            sleep(2)
        elif coins_bet > 5:
            print("Please enter a number between 1 and 5")
            sleep(2)
        else:
            coins = coins - coins_bet
            gameheader()
            print("\nThe number to beat is %s" % beat_number)
            input("\nYou have %s coins on the line! Hit enter to roll")
            print("\nRolling...")
            sleep(2)
            