import moves
import time
import os
from utility import degridder, get_level_files
from termcolor import colored

def load_level(filename):
    with open(filename, encoding='utf-8') as file:
        rows = int(file.readline().strip())
        moves_count = int(file.readline().strip())
        grid = [list(file.readline().strip()) for _ in range(rows)]
    return grid, moves_count

#SCORE STUFF

def ult_egg_ct(grid):
    return sum(1 for eg in ([row, col] for row in range(len(grid))
            for col in range(len(grid[0])) 
            if grid[row][col] == '🥚' or grid[row][col] == '🪺'))

def score(grid, inoe): # inoe - initial count of eggs and nest
    cnoe = ult_egg_ct(grid) # cnoe - current count of eggs and nest
    nested = sum(1 for _ in ([row, col] for row in range(len(grid))
            for col in range(len(grid[0])) 
            if grid[row][col] == '🪺'))
    return 10 * nested - 5 * (inoe - cnoe)

#############################

def print_game_state(prev_moves, moves_left, curr_score, grid):
    degridder(grid)
    print(colored(f'Moves played: {prev_moves}', 'light_blue'))
    print(colored(f'Moves left: {moves_left}', 'yellow'))
    print(colored(f'Score: {curr_score}', 'green'))
    print(colored('''
--------------------------------------------
| (X) Restart Game | (Y) Back to Main Menu |
--------------------------------------------
        ''', 'light_magenta'))
    
def input_germany(level_file): # many-ger (manager !!!!)
    direction_input = input(colored("Enter moves (L/R/F/B): ", 'cyan')).upper() 
    valid_moves = [char for char in direction_input if char in moves.dirs]
    invalid_moves = [char for char in direction_input if char not in moves.dirs and char not in ['X', 'Y']]
    if invalid_moves: print(colored(f"Invalid input(s): {', '.join(invalid_moves)}", 'red'))
    if 'X' in direction_input:
        print("Restarting the game...")
        gameplay(level_file)
        return
    if 'Y' in direction_input:
        from menu import main_menu
        main_menu()
        return
    return valid_moves

def gameplay(level_file):
    levels = get_level_files()
    grid, moves_count = load_level(level_file)
    curr_score = 0
    moves_left = moves_count
    prev_moves = ''
    inoe = ult_egg_ct(grid)

    print_game_state(prev_moves, moves_left, curr_score, grid)

    while moves_left > 0:
        valid_moves = input_germany(level_file)
        for direction in valid_moves:
            if moves_left <= 0: 
                break
            moves.to(grid, direction)
            curr_score = score(grid, inoe)
            prev_moves += moves.dirs[direction]
            moves_left -= 1
            print_game_state(prev_moves, moves_left, curr_score, grid)

            if not any('🥚' in row for row in grid): 
                break

        if not any('🥚' in row for row in grid):  
            break
        
    curr_score += moves_left
    if moves_left > 0:
        print(colored(f'+{moves_left} for the remaining {moves_left} move' + ('!' if moves_left == 1 else 's!'), 'light_magenta'))
    time.sleep(2)

    degridder(grid)
    print(colored(f'Moves played: {prev_moves}', 'light_blue'))
    print(colored(f'Final Score: {curr_score}', 'yellow'))

    empty_nests = any('🪹' in row for row in grid)
    
    if not empty_nests:
        print(colored('''
------------------------------------------------------------------------
| (N) Play Next Level | (X) Restart Game | (Any Key) Back to Main Menu |
------------------------------------------------------------------------
        ''', 'light_magenta')) 
    else:
        print(colored('''
--------------------------------------------------
| (X) Restart Game | (Any Key) Back to Main Menu |
--------------------------------------------------
        ''', 'light_magenta')) 


    choice = input(colored('Pick your next move: ', 'cyan')).upper()
    if choice == 'N': play_next_level(level_file, levels)
    elif choice == 'X': gameplay(level_file)  
    else: 
        from menu import main_menu
        main_menu()

def play_next_level(curr_level, levels):
    current_level = os.path.basename(curr_level)
    level_index = levels.index(current_level)

    if level_index + 1 < len(levels):
        next_level = os.path.join('levels', levels[level_index + 1])
        gameplay(next_level)
    else:
        print(colored('There are no more available levels for you to play.', 'magenta'))
        input(colored('Press ENTER to return to main menu.', 'green'))
        from menu import main_menu
        main_menu()
