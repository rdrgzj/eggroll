from utility import degridder, clear_screen
from moves import egged
from moves import egglist, egglist_back, egglist_right
from moves import _true_back, _true_fwd, _true_left, _true_right
from moves import _move_back, _move_fwd, _move_left, _move_right
from moves import move_back, move_fwd, move_left, move_right
from game import ult_egg_ct, score

##############################################################################

# UTILITY FUNCTIONS

# degridder: prints grid but returns None (helper) 
# grid should be an indexable iter of iters 

def test_degridder():
    def da(grid): # degridder assert
        def f(unction):
            try:
                unction(grid)
                return True
            except:
                raise Exception
        assert f(degridder)
    da([])
    da((['one', 'two', 'three'], 'four', (), ('5' for _ in range(6))))
    da([('gen' for er in range(8)) for _ in range(7)])

    clear_screen() # degridder prints, hence the need for clear_screen
test_degridder()

##############################################################################

# MOVEMENT-RELATED FUNCTIONS

# egged: updates game elements when an egg rolls onto it (helper)

def test_egged():
    assert egged('🍳') == '🍳'
    assert egged('🪺') == None
    assert egged('🥚') == '🥚'
    assert egged(['🥚']) == None
    assert egged('5'*10**5) == None
test_egged()

# -------------------------------------------------------------------------- #

# egglists: read the eggs in the grid in the opposite direction as the movement (helper)
# this is so that no egg would be moved twice

def test_egglists():
    grid = [
        ['🥚', '🥚', '🥚'],
        ['🥚', '🟩', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*egglist(grid)} == {*egglist_back(grid)} == {*egglist_right(grid)}
    assert [*egglist(grid)] == [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0)]
    assert [*egglist_back(grid)] == [(2,0), (1,0), (1,2), (0,0), (0,1), (0,2)]
    assert [*egglist_right(grid)] == [(0,2), (0,1), (0,0), (1,2), (1,0), (2,0)]

    grid = [
        ['🥚', '🥚', '🥚', '🟩', '🟩', '🥚'],
        ['🥚', '🟩', '🥚', '🥚'],
        ['🥚', '🟩', '🟩'],
    ]
    assert {*egglist(grid)} == {*egglist_back(grid)} == {*egglist_right(grid)}
    assert [*egglist(grid)] == [(0,0), (0,1), (0,2), (0,5), (1,0), (1,2), (1,3), (2,0)]
    assert [*egglist_back(grid)] == [(2,0), (1,0), (1,2), (1,3), (0,0), (0,1), (0,2), (0,5)]
    assert [*egglist_right(grid)] == [(0,5), (0,2), (0,1), (0,0), (1,3), (1,2), (1,0), (2,0)]

    grid = []
    assert {*egglist(grid)} == {*egglist_back(grid)} == {*egglist_right(grid)} 
    assert [*egglist(grid)] == [*egglist_back(grid)] == [*egglist_right(grid)] 
    # no eggs, so equal

    grid = ['🟩', '🥚']
    assert {*egglist(grid)} == {*egglist_back(grid)} == {*egglist_right(grid)} 
    assert [*egglist(grid)] == [*egglist_back(grid)] == [*egglist_right(grid)] 
    # same egg, so equal
test_egglists()

# -------------------------------------------------------------------------- #

# _true_[dir]: truth condition for while loop, for continuous moving (helper)
# assumes egglists work

def test_truth_condition():
    err_ctr = 0
    grid = [
        ['🥚', '🟩', '🧱'],
        ['🥚', '🥚', '🪹'],
        ['🧱', '🪺', '🟩']
    ]
    assert not _true_back(grid)
    assert _true_right(grid)
    try: _true_fwd(grid)
    except: err_ctr += 1
    try: _true_left(grid)
    except: err_ctr += 1

    grid = [
        ['🟩', '🧱'],
        ['🧱', '🥚']
    ]
    try: _true_right(grid)
    except: err_ctr += 1
    try: _true_back(grid)
    except: err_ctr += 1

    assert err_ctr == 4
test_truth_condition()

# -------------------------------------------------------------------------- #

# _move_[dir]: moves all eggs to specified dir one space if applicable (helper)
# meant to raise IndexError when egg is about to fall out of bounds
# assumes egged and egglists work

def test_single_moves():
    err_ctr = 0 # counter to check if all index errs were raised

    # checks if moves in correct direction
    grid = [
        ['🟩', '🥚'],
        ['🟩', '🟩'],
    ]
    assert _move_back(grid) == [
        ['🟩', '🟩'], 
        ['🟩', '🥚']
    ]
    assert _move_left(grid) == [
        ['🟩', '🟩'], 
        ['🥚', '🟩']
    ]
    assert _move_fwd(grid) == [
        ['🥚', '🟩'], 
        ['🟩', '🟩']
    ]
    assert _move_right(grid) == [
        ['🟩', '🥚'], 
        ['🟩', '🟩']
    ]
    # checks if IndexError is raised when an egg moving right goes out of bounds
    try: _move_right(grid)
    except IndexError: err_ctr += 1

    # checks if grid doesn't change if no eggs
    grid = [['🟩', '🧱', '🪺', '🍳']]
    assert _move_back(grid) == [['🟩', '🧱', '🪺', '🍳']]
    assert _move_fwd(grid) == [['🟩', '🧱', '🪺', '🍳']]
    assert _move_left(grid) == [['🟩', '🧱', '🪺', '🍳']]
    assert _move_right(grid) == [['🟩', '🧱', '🪺', '🍳']]

    grid = [
        ['🟩', '🟩', '🥚'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪹', '🥚']
    ]
    # checks if update for nest works during a move
    assert _move_left(grid) == [
        ['🟩', '🥚', '🟩'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if egg acts as obstacle for other eggs
    assert _move_back(grid) == [
        ['🟩', '🥚', '🟩'],
        ['🧱', '🥚', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if pans consume eggs
    assert _move_right(grid) == [
        ['🟩', '🟩', '🥚'],
        ['🧱', '🟩', '🍳'],
        ['🟩', '🪺', '🟩']
    ]
    # checks if IndexError is raised when an egg moving forward goes out of bounds
    try: _move_fwd(grid)
    except IndexError: err_ctr += 1

    # checks if IndexError is raised when an egg moving left goes out of bounds
    grid = [['🥚']]
    try: _move_left(grid)
    except IndexError: err_ctr += 1

    # checks if IndexError is raised when an egg moving back goes out of bounds
    grid = [['🥚']]
    try: _move_back(grid)
    except IndexError: err_ctr += 1

    assert err_ctr == 4 
test_single_moves()

# -------------------------------------------------------------------------- #

# move_[dir]: moves all eggs towards the same dir until not _true_[dir]
# assumes _true_[dir] and _move_[dir] work
# indirectly assumes egged and egglists work

def test_contd_moves():
    err_ctr = 0
    grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    assert move_right(grid) == [
        ['🟩', '🟩', '🥚', '🥚', '🥚', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    assert move_back(grid) == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    assert move_back(grid) == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    # checks if pans continually consume eggs
    assert move_left(grid) == [
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]
    
    grid = [
        ['🟩'], 
        ['🥚']
    ]
    try: move_fwd(grid)
    except IndexError: err_ctr += 1

    assert err_ctr == 1

    clear_screen()
test_contd_moves()

##############################################################################

# SCORE-RELATED FUNCTIONS

# ult_egg_ct: counts all existing eggs, whether nested or not
# changes count when some eggs get cooked

def test_eggcount():
    # checks if accurate count
    assert ult_egg_ct([['🪺'*3]*5, ['🥚'*2]*6]) == 3*5+2*6
    assert ult_egg_ct([]) == 0
    # checks if count remains when no eggs have fallen to a pan
    # checks if count changes when some eggs fall into a pan
    assert ult_egg_ct([
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]) == ult_egg_ct([
        ['🟩', '🟩', '🥚', '🥚', '🥚', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]) == ult_egg_ct([
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🥚', '🟩', '🥚', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ]) != ult_egg_ct([
        ['🟩', '🟩', '🟩', '🟩', '🟩', '🪺'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪺', '🧱', '🟩']
    ])
test_eggcount()

# -------------------------------------------------------------------------- #

# score: calculates the score as follows:
# score = nested eggs * 10 - panned eggs * 5
# where we know panned eggs to be initial eggct - current eggct

def test_score():
    # check if computes properly
    assert score([['🪺'*3]*5, ['🥚'*2]*6], 30) == 15*10 - 5*(30-3*5-2*6)
    # check if correct computation throughout a simulated game
    grid = [
        ['🥚', '🥚', '🥚', '🥚', '🟩', '🪹'],
        ['🍳', '🟩', '🟩', '🟩', '🟩', '🟩'],
        ['🟩', '🟩', '🧱', '🪹', '🧱', '🟩']
    ]
    initial_eggct = ult_egg_ct(grid)
    move_right(grid)
    assert score(grid, initial_eggct) == 10
    move_back(grid)
    assert score(grid, initial_eggct) == 20
    move_left(grid)
    assert score(grid, initial_eggct) == 10
test_score()

##############################################################################
