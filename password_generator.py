import os
from time import sleep
import random

## This script generates a random password 

def header():
    os.system('cls')
    print("************  Password Generator  ************")

def generate_pass(characters=12):
    password = []
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    password.append(randomUpperLetter)
    characters -= 1
    while characters > 0:
        case = random.randint(1,10)
        if case < 4:
            randomLowerLetter = chr(random.randint(ord('a'), ord('z')))
            password.append(randomLowerLetter)
            characters -= 1
        elif case > 7:
            randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
            password.append(randomUpperLetter)
            characters -= 1
        elif case > 4:
            randomNumber = random.randint(1,9)
            password.append(randomNumber)
            characters -= 1
        elif case < 5:
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
    while selection_menu != 'Q':
        if selection_menu == '1':
            characters = input("Enter number of characters in password, or q: ")
            if characters == 'q':
                selection_menu = 'Q'
            else:
                for x in range(1,6):
                    password = generate_pass(int(characters))
                    print(password)
        if selection_menu == '2':
            characters = 12
            for x in range(1,6):
                password = generate_pass(int(characters))
                password += '11'
                print(password)
            input("Press enter to continue")
            selection_menu = 'Q'
        if selection_menu == 'q':
            return 'q'



main_menu = '0'
while main_menu != 'q':
    main_menu = menu()