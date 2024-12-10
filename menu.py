import os
from game import gameplay
from utility import clear_screen, get_level_files
from termcolor import colored

def main_menu_user_input():
    while True:
        try:
            choice = int(input(colored('\nEnter your choice: ', 'cyan')))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print(colored('Invalid choice. Enter a number from 1 to 4 only.', 'red'))
        except ValueError:
            print(colored('Invalid choice. Please enter a NUMBER from 1 to 4 only.', 'red'))
            
def print_game_title():
    print(colored('''
    ███████╗░██████╗░░██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░
    ██╔════╝██╔════╝░██╔════╝░██╔══██╗██╔══██╗██║░░░░░██║░░░░░
    █████╗░░██║░░██╗░██║░░██╗░██████╔╝██║░░██║██║░░░░░██║░░░░░
    ██╔══╝░░██║░░╚██╗██║░░╚██╗██╔══██╗██║░░██║██║░░░░░██║░░░░░
    ███████╗╚██████╔╝╚██████╔╝██║░░██║╚█████╔╝███████╗███████╗
    ╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝
''', 'green'))

def show_levels_and_play_level_choice():
    clear_screen()
    levels = get_level_files()
    if not levels:
        print(colored("There are no levels that can be loaded from your current game folder.", 'red'))
        input(colored('Press ENTER to return to main menu.', 'green'))
        return

    print_game_title()
    print(colored('LEVELS:', 'green'))
    for i, level in enumerate(levels, 1):
        print(colored(f'({i}) {level}', 'yellow'))
    choice = level_user_input(levels)

    if choice not in levels:
        print(colored(f'Error: The selected level {choice} does not exist.', 'red'))
        input(colored('Press ENTER to return to the main menu.', 'green'))
    else:
        try:
            level_file = os.path.join('levels', choice)  
            gameplay(level_file) 
        except FileNotFoundError:
            print(colored(f'Error: The file {choice} does not exist. Please try again.', 'red'))

def level_user_input(levels):
    while True:
        try:
            choice = int(input(colored(f'\nChoose the level you want to play (or 0 to go back to main menu): ', 'cyan')))
            if 1 <= choice <= len(levels): 
                return levels[choice - 1]
            elif choice == 0:
                main_menu()
            else:
                print(colored(f'Invalid choice. Please enter a number between 0 and {len(levels)} only.', 'red'))
        except ValueError:
            print(colored(f'Invalid choice. Please enter a NUMBER between 0 and {len(levels)} only.', 'red'))

def print_mechanics():
    clear_screen()
    print_game_title()
    print(colored('''
GAME MECHANICS:
Egg-citing Movement!
---------------------------------------------------------------
🥚 Take control of rolling eggs! Guide them left (L), right (R), 
forward (F), or backward (B) across the grid.
---------------------------------------------------------------
🧱🪺 The eggs don’t stop until they hit something—so think 
carefully before each move!
---------------------------------------------------------------
Goal!
---------------------------------------------------------------
🪺 Put eggs in the nest! The ultimate goal is to roll each egg 
into a safe nest. But be quick, your moves are limited!
---------------------------------------------------------------
🍳 Avoid the Frying Pan! If an egg lands in the frying pan... 
well, it’s a scrambled mess and you'll lose points!
---------------------------------------------------------------
Score!
---------------------------------------------------------------
🥚 For every egg you successfully nest, you score +10 points.
---------------------------------------------------------------
🍳 If an egg lands in the frying pan, you’ll lose 5 points.
---------------------------------------------------------------
LEVEL UP! 
---------------------------------------------------------------
🚀 Each level brings new challenges. More obstacles, 
tighter spaces, and even more frying pans! Can you solve 
each level before your moves run out?
---------------------------------------------------------------
    ''', 'yellow'))
    input(colored('--------- PRESS ENTER TO RETURN TO MAIN MENU. ----------', 'green'))

def main_menu():
    while True:    
        clear_screen()
        print_game_title()
        print(colored('MAIN MENU', 'magenta', attrs=['bold']))
        print(colored('\n(1) Start Game', 'light_blue'))
        print(colored('(2) Load Level', 'yellow'))
        print(colored('(3) Game Mechanics', 'green'))
        print(colored('(4) Quit', 'red'))
        
        choice = main_menu_user_input()
        if choice == 1:
            level_file = os.path.join('levels', 'level1.in')  
            gameplay(level_file)   
        elif choice == 2:
            show_levels_and_play_level_choice()
        elif choice == 3:
            print_mechanics()
        else:
            print(colored('You are now going to exit the game. See you later!', 'red'))
            exit()

main_menu()

