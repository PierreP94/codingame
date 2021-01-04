import sys
import math
import numpy as np


breaker_mode = False
inversed_mode = False
successful = False
default_dir = "SOUTH"


def reset():
    breaker_mode = False
    inversed_mode = False
    successful = False
    position = (int(x), int(y))


def next_place(position, direction):
    x = position[0]
    y = position[1]
    if direction == "NORTH":
        x = position[0] - 1
    elif direction == "EAST":
        y = position[1] + 1
    elif direction == "WEST":
        y = position[1] - 1
    else:
        x = position[0] + 1
    return (x, y)


def next_obj(position, direction):
    return board[next_place(position, direction)]


def change_direction(direction):
    if not inversed_mode:
        if direction == "NORTH":
            new_dir = "WEST"
        elif direction == "EAST":
            new_dir = "NORTH"
        elif direction == "WEST":
            new_dir = "SOUTH"
        elif direction == "SOUTH":
            new_dir = "EAST"
        else:
            print("erreur de direction1", file=sys.stderr, flush=True)
    else:
        if direction == "NORTH":
            new_dir = "EAST"
        elif direction == "EAST":
            new_dir = "SOUTH"
        elif direction == "WEST":
            new_dir = "NORTH"
        elif direction == "SOUTH":
            new_dir = "WEST"
        else: 
            print("erreur de direction", file=sys.stderr, flush=True)
    return new_dir


def obstacle(position, direction):
    new_pos = position
    if not inversed_mode:
        new_dir = "SOUTH"
    else:
        new_dir = "WEST"
    while next_obj(position, new_dir) == '#' or (next_obj(position, new_dir) == 'X' and breaker_mode == False):
        new_dir = change_direction(new_dir)
    return new_pos, new_dir


def hustlin(position, direction):
    global breaker_mode
    global inversed_mode
    global successful
    next_pos = next_place(position, direction)
    new_pos = position
    new_dir = direction
    if board[next_pos] == '#':
        new_pos, new_dir = obstacle(position, direction)
    elif board[next_pos] == 'S':
        new_dir = "SOUTH"
        new_pos = next_pos
    elif board[next_pos] == 'E':
        new_dir = "EAST"
        new_pos = next_pos
    elif board[next_pos] == 'N':
        new_dir = "NORTH"
        new_pos = next_pos
    elif board[next_pos] == 'W':
        new_dir = "WEST"
        new_pos = next_pos
    elif board[next_pos] == 'X':
        if breaker_mode:
            board[next_pos] = ' '
            new_pos = next_pos
        else:
            new_pos, new_dir = obstacle(position, direction)
    elif board[next_pos] == 'I':
        if inversed_mode:
            inversed_mode = False
        else:
            inversed_mode = True
        new_pos = next_pos
    elif board[next_pos] == 'B':
        if breaker_mode:
            breaker_mode = False
        else:
            breaker_mode = True
        new_pos = next_pos
    elif board[next_pos] == 'T':
        for sec_teleport in list(zip(*np.where(board == 'T'))):
            if sec_teleport != next_pos:
                new_pos = sec_teleport
    elif board[next_pos] == '$':
        succesful = True
        new_pos = next_pos     
    else:
        new_pos = next_pos 

    return new_pos, new_dir


answer = ""
elements = []
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
l, c = [int(i) for i in input().split()]
for i in range(l):
    row = input()
    elements.extend(row)
board = np.asarray(elements,dtype=str).reshape(l, c)
x, y = np.where(board == "@")
position = (int(x), int(y))
new_pos = position
direction = default_dir
new_dir = direction
i = 0
while board[position] != '$' and i < 999:
    position = new_pos
    direction = new_dir
    new_pos, new_dir = hustlin(position, direction)
    if board[position] != '$' and new_pos != position:
        answer += direction + "\n"
    i += 1
if i == 999: 
    answer = "LOOP"
print(answer)

