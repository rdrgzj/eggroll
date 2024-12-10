import time
from utility import degridder

def egged(emoji):
    if emoji in ['🥚', '🍳']: return emoji
    elif emoji == '🟩': return '🥚'
    elif emoji == '🪹': return '🪺'

## MOVEMENT FUNCTIONS ##

# LEFT

def egglist(grid):
    return ((row, col) for row in range(len(grid))
            for col in range(len(grid[row])) if grid[row][col] == '🥚')

def _move_left(grid):
    for [ex, ey] in egglist(grid):  # gives egg coords
        grid[ex][ey] = '🟩'  # removes egg first
        if ey == 0: raise IndexError
        if grid[ex][ey - 1] not in ['🧱', '🪺', '🥚']:  # list of obstacles
            grid[ex][ey - 1] = egged(grid[ex][ey - 1])
        else:
            grid[ex][ey] = '🥚'  # returns egg if obstacle, meaning egg didn't move
    return grid

def _true_left(grid):  # while condition
    if any(y <= 0 for [x, y] in egglist(grid)):
        raise IndexError
    else:
        return any(grid[x][y - 1] not in ['🧱', '🪺', '🥚'] for [x, y] in egglist(grid))

def move_left(grid):  # just call, no need to print
    while _true_left(grid):
        degridder(grid)
        grid = _move_left(grid)
    degridder(grid)
    time.sleep(0.5)
    return grid


# FORWARD

def _move_fwd(grid):
    for [ex, ey] in egglist(grid):
        grid[ex][ey] = '🟩'  # removes egg first
        if ex == 0: raise IndexError
        if grid[ex - 1][ey] not in ['🧱', '🪺', '🥚']:
            grid[ex - 1][ey] = egged(grid[ex - 1][ey])
        else:
            grid[ex][ey] = '🥚'
    return grid

def _true_fwd(grid):  # while condition
    if any(x <= 0 for [x, y] in egglist(grid)):
        raise IndexError
    else:
        return any(grid[x - 1][y] not in ['🧱', '🪺', '🥚'] for [x, y] in egglist(grid))

def move_fwd(grid):
    while _true_fwd(grid):
        degridder(grid)
        grid = _move_fwd(grid)
    degridder(grid)
    time.sleep(0.5)
    return grid


# RIGHT

def egglist_right(grid):
    return ((row, col) for row in range(len(grid))
            for col in range(len(grid[row])-1, -1, -1) if grid[row][col] == '🥚')

def _move_right(grid):
    for [ex, ey] in egglist_right(grid):
        grid[ex][ey] = '🟩'  # removes egg first
        if grid[ex][ey + 1] not in ['🧱', '🪺', '🥚']:
            grid[ex][ey + 1] = egged(grid[ex][ey + 1])
        else:
            grid[ex][ey] = '🥚'
    return grid

def _true_right(grid):
    if any(y >= len(grid[x]) for [x,y] in egglist_right(grid)):
        raise IndexError
    else:
        return any(grid[x][y + 1] not in ['🧱', '🪺', '🥚'] for [x, y] in egglist_right(grid))

def move_right(grid):
    while _true_right(grid):
        degridder(grid)
        grid = _move_right(grid)
    degridder(grid)
    time.sleep(0.5)
    return grid


# BACK

def egglist_back(grid):
    return ((row, col) for row in range(len(grid)-1, -1, -1)
            for col in range(len(grid[row])) if grid[row][col] == '🥚')

def _move_back(grid):
    for [ex, ey] in egglist_back(grid):
        grid[ex][ey] = '🟩'  # removes egg first
        if grid[ex + 1][ey] not in ['🧱', '🪺', '🥚']:
            grid[ex + 1][ey] = egged(grid[ex + 1][ey])
        else:
            grid[ex][ey] = '🥚' 
    return grid

def _true_back(grid):
    if any(x >= len(grid) for [x, y] in egglist_back(grid)):
        raise IndexError
    else:
        return any(grid[x + 1][y] not in ['🧱', '🪺', '🥚'] for [x, y] in egglist_back(grid))

def move_back(grid):
    while _true_back(grid):
        degridder(grid)
        grid = _move_back(grid)
    degridder(grid)
    time.sleep(0.5)
    return grid

#MOVEMENT HANDLER

def to(grid, direction):
    direction = direction.upper()
    if direction == 'L':
        move_left(grid)
    elif direction == 'R':
        move_right(grid)
    elif direction == 'F':
        move_fwd(grid)
    elif direction == 'B':
        move_back(grid)
    else:
        print('Invalid movement!')

dirs = {
    'L': '←',  
    'F': '↑', 
    'R': '→',  
    'B': '↓',  
}
