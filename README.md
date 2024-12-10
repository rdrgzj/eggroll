<p align="center">
███████╗░██████╗░░██████╗░██████╗░░█████╗░██╗░░░░░██╗░░░░░<br>
██╔════╝██╔════╝░██╔════╝░██╔══██╗██╔══██╗██║░░░░░██║░░░░░<br>
█████╗░░██║░░██╗░██║░░██╗░██████╔╝██║░░██║██║░░░░░██║░░░░░<br>
██╔══╝░░██║░░╚██╗██║░░╚██╗██╔══██╗██║░░██║██║░░░░░██║░░░░░<br>
███████╗╚██████╔╝╚██████╔╝██║░░██║╚█████╔╝███████╗███████╗<br>
╚══════╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝
</p>

<br><br>

<p align="center">
  <h1><strong>PLAYER MANUAL</strong></h1>
</p>

## OBJECTIVE:
Guide the eggs 🥚 to the nests 🪹 before you run out of moves.  
Avoid obstacles like frying pans 🍳.

## HOW TO PLAY:
- **Move the Eggs**: Use these keys to move the eggs:
    - `L`  - Move left
    - `R`  - Move right
    - `F`  - Move forward
    - `B`  - Move backward

- **Goal**: Get all the eggs into the nests 🪺.

- **Avoid**: Don’t let the eggs land in the frying pans 🍳 or they’ll be scrambled!

## SCORING:
- +10 points for each egg you get into a nest 🪺.
- -5 points for every egg that lands in a frying pan 🍳.
- At the end of the game, you get bonus points for any moves you did not use (1 point per move).

## MENUS:
- **Main Menu**:
    - `(1)` Start a new game
    - `(2)` Load a saved level
    - `(3)` Learn the game rules
    - `(4)` Quit the game

- **After Each Game**:
    - `(N)` Play the next level
    - `(X)` Restart the current level
    - `(Y)` Return to the main menu

## TIPS:
- Think carefully before you move the eggs. They roll until they hit something!
- Use your moves wisely. You only have a limited number of moves to get the eggs into the nests.

## GAME OVER:
- The game ends when either all the eggs are in nests or when you run out of moves.
- After completing a level, you can choose to play the next level, restart, or return to the main menu.
- If you finish a level but did not fill all the nests, you can only restart the current level or return to the main menu.

<p align="center">
  <h3><strong>Thank you for playing!</strong><h3>
</p>

<br><br>

<p align="center">
  <h1><strong>CODE DOCUMENTATION</strong></h1>
</p>

We've divided our code into four files: `game.py`, `menu.py`, `moves.py`, and `utility.py`.

## 1. game.py
Handles the main game logic. It brings all the functions to display the game itself and create the actual gameplay experience.

| *Function Name*                               | *Description*                                                            |
|-----------------------------------------------|----------------------------------------------------------------------------|
| `load_level(filename)`                        | Loads the grid and number of available moves from a level file.            |
| `ult_egg_ct(grid)`                            | Counts the total number of eggs and nests on the grid.                     |
| `score(grid, inoe)`                           | Calculates the score based on the number of nested eggs and penalties for misplaced eggs. |
| `print_game_state(prev_moves, moves_left, curr_score, grid)` | Displays the current state of the game: moves played, moves left, and current score. |
| `input_germany(level_file)`                   | Handles user input for moves (L, R, F, B) and navigates game flow with options like restarting or going to the main menu. |
| `gameplay(level_file)`                        | Executes the main game loop, processing player input and updating the grid and score. |
| `play_next_level(curr_level, levels)`         | Handles level progression, moving to the next level, or displays a message if no levels are available. |

## 2. `menu.py`

Handles all menu-related functionality, providing an interface for the player to start the game, pick a level, read the game mechanics, or exit the game.

| *Function Name*                              | *Description*                                                            |
|----------------------------------------------|----------------------------------------------------------------------------|
| `main_menu_user_input()`                     | Handles user input for selecting options from the main menu.               |
| `print_game_title()`                         | Displays the game title with a stylized and colored format.                |
| `show_levels_and_play_level_choice()`        | Displays a list of levels and allows the user to select one.               |
| `level_user_input(levels)`                   | Prompts the user to choose a level or return to the main menu.             |
| `print_mechanics()`                          | Displays the game mechanics and instructions.                              |
| `main_menu()`                                | The main entry point for the menu loop, prompting users to start a new game, load levels, view mechanics, or quit. |

## 3. moves.py
Includes all movement-related functionality, handling egg movement mechanics and collision detection.

|*Function Name*|*Description*|
|---------------|-------------|
|`egglist(grid)`|Returns a list of coordinates where eggs are present.|
|`_move_left(grid), _move_right(grid), _move_fwd(grid), _move_back(grid)`|Functions that perform the actual movement of eggs in the specified direction (left, right, forward, or backward) by checking conditions and updating the grid.|
|`move_left(grid), move_right(grid), move_fwd(grid), move_back(grid)`|Functions that check conditions for moving eggs in the specified direction and then call the corresponding function above to perform the movement.|
|`to(grid, direction)`|Handles user input for directions (L, R, F, B) and calls the appropriate function to move the eggs.|

## 4. utility.py
Includes all the helper functions that will support the game operation.

| *Function Name*                              | *Description*                                                            |
|----------------------------------------------|----------------------------------------------------------------------------|
| `clear_screen()`                             | Clears the terminal screen for better visualization of the game state.     |
| `get_level_files()`                          | Returns a list of available level files in the levels directory.           |
| `degridder(grid)`                            | Displays the current grid with eggs and obstacles.                         |

<br><br>

<p align="center">
  <h1><strong>UNIT TESTS</strong></h1>
</p>

These are found in `unit_tests.py`. The functions that are used for unit testing are as follows. 

|*Function Name*|*Description*|
|---------------|-------------|
|`test_degridder()`|Tests the `degridder` function from `utility`.|
|`test_egged()`|Tests the `egged` function from `moves`.|
|`test_egglists()`|Tests the `egglist`, `egglist_back`, and `egglist_right` functions from `moves`.|
|`test_truth_condition()`|Tests the `_true_[dir]` function for each direction from `moves`.|
|`test_single_moves()`|Tests the `_move_[dir]` function for each direction from `moves`.|
|`test_contd_moves()`|Tests the `_move_[dir]` function for each direction from `moves`.|
|`test_eggcount()`|Tests the `ult_egg_ct` function from `game`.|
|`test_score()`|Tests the `score` function from `game`.|

The assertions included in the unit tests guarantee the outputs for each function from edge cases to common cases that are actually used in the implementation of the game levels. To add additional unit tests for the `degridder` function, since it has no output, go to the `test_degridder()` function and call the `da()` function inside. It will raise an exception if the `degridder` function encounters an error. Other than that, the rest of the functions that underwent unit tests return an output, and so one can simply go to the respective `test_[function]()` function and add an assertion about the function as follows `assert function(*args) == output`.

<br><br>

<p align="center">
  <h1><strong>BONUS FEATURES</strong></h1>
</p>

1. **Main menu** - The player can access a main menu to start the game with the first level, view mechanics, load levels, or quit the game.
2. **Level selection** - The game allows the player to choose from multiple levels with varying difficulty. Each level has a unique grid layout.
3. **Game mechanics display** - The player can view the game mechanics and rules to better understand how to play and move eggs within the grid.
4. **Ability to restart game or return to main menu while playing** - The player has the option to restart the current level or return to the main menu at any point during gameplay.
5. **Ability to play next level after completing current level** - After finishing a level, the player can choose to proceed to the next level if available.
6. **Post-game options** - After completing a level, the player can choose to advance to the next level, restart the current level, or return to the main menu.
7. **Ability to exit game through main menu** - The player can exit the game through the main menu.
