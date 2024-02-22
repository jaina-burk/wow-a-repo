from time import sleep
import os
import pickle


# Greeter is a terminal application that greets old friends warmly,
#       and remembers new friends.

### FUNCTIONS  ###

# Clears screen and displays a title bar
def display_title_bar():
    os.system('cls')

    print("\t************************************************")
    print("\t***   Greeter - Hello old and new friends!   ***")
    print("\t************************************************")

# Let's players know what they can do
def get_user_choice():
    print("\n[1] See a list of friends.")
    print("\n[2] Tell me about someone new.")
    print("\n[q] Quit.\n")

    return input("What would you like to do? ")

# Show all names in names list

def show_names():
    print("\nHere are the people I know.\n")
    for name in names:
        print(name.title())

# Enter in a new name
            
def get_new_name():
    new_name = input("\nPlease tell me this person's name: ")
    if new_name.lower() in names:
        print("\n %s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name.lower())
        print("\nI'm so happy to know %s!\n" % new_name.title())

# Loads names file, or creates new names.py file

def load_names():
    try:
        file_object = open('names.py', 'rb')
        names = pickle.load(file_object)
        file_object.close()
        return names
    except Exception as e:
        print(e)
        return []
    
# Saves the names before quitting
    
def quit():
    try:
        file_object = open('names.py', 'wb')
        pickle.dump(names, file_object)
        file_object.close()
        print("\nThanks for playing. I will remember these good friends.")
    except Exception as e:
        print("\nThanks for playing. I won't remember these names.")
        print(e)

    
### Main Program ###
    
# Set up a loop where users can choose what they'd like to do
names = load_names()

choice = ' '
display_title_bar()

while choice != 'q':

    choice = get_user_choice()

    # Respond to the user's choice
    display_title_bar()
    if choice == '1':
        show_names()
    elif choice == '2':
        get_new_name()
    elif choice == 'q':
        quit()
        print("\nThanks for playing!\n")
    else:
        print("\nI don't understand that choice.\n")