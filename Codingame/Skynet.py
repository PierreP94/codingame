import sys
import math
import random
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]

# Added 2 lists
node = list()
gateway = list()
for i in range(n):
    node.append(list())
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]

    # Adding piles to the list
    if n1 not in node[n2]:
        node[n2].append(n1)
    if n2 not in node[n1]:
        node[n1].append(n2)


for i in range(e):
    ei = int(input())  # the index of a gateway node

    # List of gateway
    gateway.append(ei)


def prev_from_win(si): 
    action = ""
    for exit_node in gateway:
        if exit_node in node[si]:
            action = (str(node[exit_node].pop(node[exit_node].index(si))) + " " 
                     + str(node[si].pop(node[si].index(exit_node))))
    return action


def del_gate():
    for i in gateway:
        count = 0
        for j in range(len(node)):
            if i in node[j]:
                count += 1
        if count == 0:
            gateway.remove(i)
    return gateway


def sel_rand_gate(si):
    action = ""
    first_node = node[si].pop()
    second_node = node[first_node].pop()
    action = str(second_node) + " " + str(first_node)
    return action


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    action = prev_from_win(si) 
    if action == "": 
        action = sel_rand_gate(si)
    del_gate()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(action)

