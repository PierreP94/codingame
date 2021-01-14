import math
class Zombie:
    def __init__(self, zombie_id, y, x, y_next, x_next):
        self.y = y
        self.x = x
        self.y_next = y_next
        self.x_next = x_next
        self.d_to_h = 99999999
        self.target = None
        self.zombie_id = zombie_id
    def dist_to_h(self):
        for h in human:
            d = distance(self.zombie_id, h)
            if self.d_to_h > d:
                self.d_to_h = d
                self.target = h
                human[h].c_attack.append(self.zombie_id)


class Human:
    def __init__(self, human_id, y, x):
        self.y = y
        self.x = x
        self.human_id = human_id
        self.savable = None
        self.c_attack = []
    def possible_to_save(self):
        min_ = 99999
        for z in zombie:
            d = distance(z, h)
            if min_ > d:
                min_ = d
                self.c_attack = z
        nb_turn = (min_ - 400) / 400
        dist_a_h = math.sqrt((x - self.x) ** 2 + (y - self.y) ** 2) - 2000
        turn_a = dist_a_h / 1000
        if turn_a <= nb_turn:
            self.savable = True
        else:
            self.savable = False


def barycentre(z, h):
    y = (1 / 3) * zombie[z].y + (1 / 3) * human[h].y + (1 / 3) * human[666].y
    x = (1 / 3) * zombie[z].x + (1 / 3) * human[h].x + (1 / 3) * human[666].x
    return x, y


def distance(z, h):
    return math.sqrt((human[h].x - zombie[z].x) ** 2 + (human[h].y - zombie[z].y) ** 2)


def update_dist():
    for z in zombie:
        zombie[z].dist_to_h()


def most_danger_z():
    for z in zombie:
        if human[zombie[z].target].savable and zombie[z].target != 666:
            t = (zombie[z].d_to_h, z)
            dangerous_ones.append(t)
    dangerous_ones.sort()
    return dangerous_ones


def closest_z_to_h():
    min_ = 99999
    for z in zombie:
        if min_ > zombie[z].d_to_h:
            min_z = z
            min_ = zombie[z].d_to_h
    return min_, min_z
# game loop
zombie = {}
human = {}
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    zombie = {}
    human = {}
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        human[human_id] = Human(human_id, human_y, human_x)
    human[666] = Human(666, y, x)
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombie[zombie_id] = Zombie(zombie_id, zombie_y, zombie_x, zombie_ynext, zombie_xnext)
        zombie[zombie_id].dist_to_h()
    update_dist()
    for h in human:
        human[h].possible_to_save()
    human[666].savable = False
    dangerous_ones = []
    dangerous_ones = most_danger_z()
    if not dangerous_ones:
        dangerous_ones.append(closest_z_to_h())
    answer_x, answer_y = barycentre(dangerous_ones[0][1], zombie[dangerous_ones[0][1]].target)
    answer = str(int(answer_x)) + " " + str(int(answer_y))
    print(answer)
