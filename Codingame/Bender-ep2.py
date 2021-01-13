import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Room:
    def __init__(self, price, out_1, out_2):
        self.price = price
        self.out_1 = out_1
        self.out_2 = out_2
        self.parents = []
        self.value = 0


def reverse_tree():
    r = n - 1
    while r >= 0 :
        daughter_1 = rooms[r].out_1
        daughter_2 = rooms[r].out_2
        if daughter_1 != n and daughter_2 != n:
            rooms[r].value = rooms[r].price + max(rooms[daughter_1].value, rooms[daughter_2].value)
        elif daughter_2 != n :
            rooms[r].value = rooms[r].price + max(0, rooms[daughter_2].value)
        elif daughter_1 != n :
            rooms[r].value = rooms[r].price + max(0, rooms[daughter_1].value)
        else:
            rooms[r].value = rooms[r].price
        r -= 1
    return rooms[0].value


rooms = {}
n = int(input())
for i in range(n):
    room = input()
    room_id, price, out_1, out_2  = room.split()
    if out_1 =='E' : 
        out_1 = int(n)
    if out_2 == 'E':
        out_2 = int(n)
    print(int(room_id),int(price), int(out_1), int(out_2), file=sys.stderr, flush=True)
    rooms[int(room_id)] = Room(int(price), int(out_1), int(out_2))
answer = reverse_tree()

print(answer)
