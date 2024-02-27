import os
from time import sleep
import pickle

# An app that stores words and meanings in a local dictionary

### Definitions ###

def titlebar():
    print('************************************')
    print('*********   Word Bank   ************')
    print('************************************')

def menu():
    print('Select an option below:')
    print('Display known words [1]')
    print('Enter a new word [2]')
    print('Quit [q]')

### Main Loop ###

selection = ' '

titlebar()
print('\nWelcome to the Word Bank app!\n')
while selection != 'q':
    menu()
    selection = input('Enter your choice: ')
