# Dice Game - A Game where you roll dice and buy power ups
# The goal of the game is to last as many rounds as possible before you run out of money

import os
from time import sleep
import random

###### Definitions ######

def header():
    # header text for menu
    print("*****************************************")
    print("*****           Dice Time           *****")
    print("*****************************************")

def gameheader():
    # Displays info about the run (coins, round, multiplier, power ups)
    os.system('cls')
    print("****************************************************")
    print(" Coins:%s                            Round:%s" % (coins, round_number))
    print("                                     Multiplier: %s" % multiplier)
    print(" Dice Sides: %s " % power_ups["Dice Sides"])
    print(" Chance to multiply roll: %s " % power_ups["Chance to multiply"])
    print("****************************************************")

def calculate_roll():
    # Calculate's the base roll, returns value
    result = random.randint(1,power_ups["Dice Sides"])
    return result

def roll():
    multiplied = 0
    multiply_by = 1
    # Takes resulte of calculate_roll() and applies the modifiers from power ups
    roll_result = calculate_roll()
    if power_ups["Chance to multiply"] > 0:
        multiplied = random.randint((1 * int((power_ups["Chance to multiply"] / 10))), 10)
    if multiplied == 10:
        multipy_by = 2
    else:
        multiply_by = 1
    return roll_result, multiply_by

def next_round(coins, round_number):
    begin = 0
    while begin == 0:
        # Sets begin to 1 when number between 1 and 5 entered, which starts the loop
        gameheader()
        print("\nThe number to beat is %s" % beat_number)
        coins_bet = int(input("\nHow many coins would you like to bet? (Max 5): "))
        if coins_bet < 1:
            print("Please enter a number between 1 and 5")
            sleep(2)
        elif coins_bet > 5:
            print("Please enter a number between 1 and 5")
            sleep(2)
        else:
            coins = coins - coins_bet
        if coins < 0:
            print("Can't go below 0!")
            sleep(2)
            coins = coins + coins_bet
        else:
            begin = 1
    if begin == 1:
        gameheader()
        print("\nThe number to beat is %s" % beat_number)
        input("\nYou have %s coins on the line! Hit enter to roll" % coins_bet)
        print("\nRolling %s sided dice..." % power_ups["Dice Sides"])
        sleep(2)
        roll_result1, multiply_by = roll()
        roll_result = roll_result1 * multiply_by
        if roll_result >= beat_number:
            coins = (coins_bet * multiplier) + coins
            print("You rolled %s" % roll_result)
            if multiply_by == 2:
                print("Your roll got doubled!")
            print("Nice! You now have %s coins." % coins)
            sleep(2)
            # adds 1 to the round number
            round_number = round_number + 1
            begin = 2
        else:
            print("You rolled %s" % roll_result)
            if multiply_by == 2:
                print("Your roll got doubled!")
            print("Ouch. You now have %s coins." % coins)
            sleep(2)
            # adds 1 to the round number
            round_number = round_number + 1
            begin = 2
    return coins, round_number

def game_store(coins):
    selection = 0
    while selection != 'q':
        os.system('cls')
        print("Welcome to the store! Select a power up, or enter [q] to continue.\n")
        print("Currently owned power ups:\n")
        print("Dice Sides: %s" % power_ups["Dice Sides"])
        print("Chance to double roll: %s percent" % power_ups["Chance to multiply"])
        print("\nYou have %s coins to spend." % coins)
        print("[1] Add 2 to your dice max (10 coins)")
        print("[2] Add a 10 percent chance to double your dice roll (5 coins)")
        selection = input("\nSelection: ")
        if selection == '1':
            coins = coins - 10
            if coins < 2:
                print("You can't go below 2 coins!")
                sleep(2)
                coins = coins + 10
                selection = 0
            else:
                power_ups["Dice Sides"] = power_ups["Dice Sides"] + 2
                selection = 0
        if selection == '2':
            coins = coins - 5
            if coins < 2:
                print("You can't go below 2 coins!")
                sleep(2)
                coins = coins + 5
                selection = 0
            else:
                power_ups["Chance to multiply"] = power_ups["Chance to multiply"] + 10
                selection = 0
    return coins, power_ups["Dice Sides"], power_ups["Chance to multiply"]
        


###### Main Loop ######
startgame = 0
round_number = 1
coins = 10
coins_bet = 0
beat_number = 1
multiplier = 2
new_coins = 0
new_round = 0
power_ups = {"Dice Sides":6, "Chance to multiply":0}
multiply_by = 1

while startgame != 'q':
    os.system('cls')
    header()
    print("\nWelcome to Dice Time!\n")
    print("In this game, you start with 10 coins.\n")
    print("Each roll you bet up to 5 coins.  Beat the required number, you get X multiplier coins back\n")
    print("After 3 rounds, you get a chance to buy power ups.\n")

    startgame = input("Enter [1] to begin, or [q] to quit: ")
    # Sets base value for start of run and begins loop
    if startgame == '1':
        while coins > 0:
            if 1 == round_number%2:
                # Every 2 rounds, adds 1 to beat number
                beat_number += 1
            if 0 == round_number%4:
                # Enters the store and adds 1 to multiplier every 3 rounds
                multiplier += 1
                coins , power_ups["Dice Sides"], power_ups["Chance to multiply"] = game_store(coins)
            coins, round_number = next_round(coins, round_number)
        print("You ran out of coins!")
        print("\nYou made it %s rounds." % round_number)

    else:
        print("Please enter [1] or [q]")
        sleep(2)
