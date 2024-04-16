import os
from time import sleep
import random

## This script generates a random password 

def header():
    os.system('cls')
    print("************  Password Generator  ************")

def generate_pass(characters=12):
    password = []
    while characters > 0:
        case = random.randint(1,10)
        if case <4:
            randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
            password.append(randomLowerLetter)
            characters -= 1
        elif case > 8:
            randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
            password.append(randomUpperLetter)
            characters -= 1
        elif case == 5 or 6:
            randomNumber = random.randint(1,9)
            password.append(randomNumber)
            characters -= 1
        elif case == 8 or 7:
            symbols = ['!','?','$']
            randomSymbol = random.choice(symbols)
            password.append(randomSymbol)
            characters -= 1
    pass_final = ''.join(str(x) for x in password)
    return pass_final


def menu():
    header()
    print("Select type of password")
    print("Random Password [1]")
    print("HSSEDI Password [2]")
    print("Quit [q]")
    selection_menu = input("\nEnter Selection: ")
    while selection_menu != 'q':
        if selection_menu == '1':
            characters = int(input("Enter number of characters in password:"))
            password = generate_pass(characters)
            print(password)


menu()