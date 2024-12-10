import os
import sys
import subprocess
import time

def clear_screen():
    if sys.stdout.isatty():
        clear_cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(clear_cmd, shell=True)

def get_level_files():
    return [f for f in os.listdir('levels') if f.startswith('level') and f.endswith('.in')]

def degridder(grid):
    time.sleep(0.5)
    clear_screen()
    display = ''
    for row in range(len(grid)):
        display += ''.join(grid[row]) + '\n'
    print(display)
