import sys
import math
from itertools import product

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
grid = []
moves = [(-1, 0), (1,0), (0,-1), (0,1)]
for i in range(10):
    row = input()
    if 'C' in row:
        child_y = i
        child_x = row.index('C')
    if 'M' in row:
        mother_y = i
        mother_x = row.index('M')
    grid += [row]


def valid_pos(position):
    """Possibles positions"""
    v_pos = []
    for try_move in moves:
        new_pos = position[0] + try_move[0], position[1] + try_move[1] 
        if (new_pos[0] >= 0 and new_pos[1] >= 0 
            and new_pos[0] <= 9 and new_pos[1] <= 9 
            and grid[new_pos[0]][new_pos[1]] != '#'):
            v_pos.append(new_pos)
    return v_pos


def bds():
    """Breadth First Search"""
    track_done = {}
    for x, y in product(range(10), repeat=2):
        if grid[y][x] != '#':
            track_done[y, x] = False
    tracks = dict()
    position = child_y, child_x
    tracks[position] = None
    track_done[position] = True
    pile =[]
    pile.append(position)
    while pile :
        position = pile.pop(0)
        for v_pos in valid_pos(position):
            if not track_done[v_pos]:
                tracks[v_pos] = position
                pile.append(v_pos)
        track_done[position] = True
    return tracks


def distance(tracks):
    """calculate distance following tracks"""
    pos = (mother_y, mother_x)
    length = 0
    while pos != (child_y, child_x):
        pos = tracks[pos]
        length +=1
    return (str(length*10)+"km")


tracks = bds()
answer = distance(tracks)
print(answer)

