from aocd import get_data
import numpy as np

move_map = {
    '|':'NS',
    '-':'EW',
    'L':'NE',
    'J':'NW',
    '7':'SW',
    'F':'ES',
    '.':'',
    'S':'NESW',
}

lines = get_data(year=2023, day=10).splitlines()
array = np.array([list(line.strip()) for line in lines])
startRow, startCol = np.where(array == 'S')
start = tuple(zip(startRow,startCol))[0]

distance_map = np.empty_like(array,dtype=int)
def traverse_the_map(pos, step):
    dirs = move_map[array[pos[0]][pos[1]]]

def go_north(pos):
    pass
def go_east(pos):
    pass
def go_south(pos):
    pass
def go_west(pos):
    pass
