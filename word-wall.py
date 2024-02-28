import os
from time import sleep
import pickle

# An app that stores words and meanings in a local dictionary

### Definitions ###

def titlebar():
    print('**************************************')
    print('***********   Word Bank   ************')
    print('**************************************')

def menu():
    print('Select an option below:')
    print('Display/modify known words [1]')
    print('Enter a new word [2]')
    print('Quit [q]')

def display_words():
    done = ' '
    while done != 'q':
        os.system('cls')
        titlebar()
        print("The following definitions are stored: ")
        for word, definitions in words.items():
            print("%s: %s" % (word, definitions))
        done = input('Enter [1] to modify a word, or [q] when finished:')
        if done == '1':
            modify_word()

def modify_word():
    modify = ' '
    modify_select = ' '
    modify = input('Which word would you like to modify? Enter [q] to quit: ')
    while modify != 'q':
        if modify in words:
            while modify_select != 'q':
                os.system('cls')
                titlebar()
                print("How would you like to modify this word %s?" % modify)
                print("\nModify word [1]")
                print("\nModify definition [2]")
                print("\nDelete word [3]")
                print("\nQuit [q]\n")
                modify_select = input('Enter selection:')
                if modify_select == '1':
                    new_spelling = ' '
                    new_spelling = input('Enter new spelling for %s:' % modify)
                    words[new_spelling] = words[modify]
                    del words[modify]
                    modify_select = 'q'
                elif modify_select == '2':
                    new_def = ' '
                    new_def = input('Enter new definition for %s: ' % modify)
                    words[modify] = new_def
                    modify_select = 'q'
                elif modify_select == '3':
                    del words[modify]
                    print("Deleted %s and definition." % modify)
                    sleep(2)
                    modify_select = 'q'
            modify = 'q'
        else:
            print("I don't know that word.")
            sleep(2)
            modify = 'q'


def input_word():
    os.system('cls')
    titlebar()
    new_word = ' '
    while new_word != 'q':
        new_word = input('Please enter a new word, or q to quit: ').lower()
        if new_word in words:
            os.system('cls')
            titlebar()
            print('Word already in dictionary, enter new word')
        elif new_word != 'q':
            new_def = input("Please enter the word's definition: ")
            words[new_word] = new_def
            print('The following word and definition have been saved:')
            print("%s: %s" % (new_word, words[new_word]))
            sleep(2)
            os.system('cls')
            titlebar()
            new_word = ' '



### Main Loop ###

try:
    words = pickle.load(open('wordwall.pickle','rb'))
except:
    words = {}

selection = ' '
new_word = ' '

print('\nWelcome to the Word Bank app!\n')
while selection != 'q':
    os.system('cls')
    titlebar()
    menu()
    selection = input('Enter your choice: ')
    if selection == '1':
        display_words()
    elif selection == '2':
        input_word()


try:
    file_object = open('wordwall.pickle', 'wb')
    pickle.dump(words, file_object)
    file_object.close()
    
    print('I will remember the following words: ')
    for word, definitions in words.items():
        print("%s: %s" % (word, definitions))
except Exception as e:
    print(e)
    print("\nI couldn't figure out how to store these words.")