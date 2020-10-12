import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
site_dict = {}
site_pos = {}
barracks = {}
tower = {}
knight = {}
archer = {}
giant = {}
mine = {}
e_t_build = {}



num_sites = int(input())
class Site:  
    def __init__(self, ignore_1, ignore_2, structure_type, owner, param_1, param_2, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.ignore_1 = ignore_1
        self.ignore_2 = ignore_2
        self.structure_type = structure_type
        self.owner = owner
        self.param_1 = param_1
        self.param_2 = param_2
        self.distance = 0
        self.bar_type = ""
        self.mine_lvl = 0



class Unit:
    count_u = 0
    def __init__(self, x, y, owner, health):
        self.x = x
        self.y = y
        self.structure_type = 0
        self.owner = owner
        self.health = health
        Unit.count_u += 1
class Queen(Unit):
    def __init__(self, x, y, owner, health):
        Unit.__init__(self, x, y, owner, health)

class Archer(Unit):
    count_a = 0
    def __init__(self, x, y, owner, health):
        Unit.__init__(self, x, y, owner, health)
        Archer.count_a += 1

class Knight(Unit) :
    count_k = 0
    def __init__(self, x, y, owner, health):
        Unit.__init__(self, x, y, owner, health)
        Knight.count_k += 1

class Giant(Unit) :
    count_g = 0
    def __init__(self, x, y, owner, health):
        Unit.__init__(self, x, y, owner, health)
        Giant.count_g += 1
#avoiding turrets       
def out_range(site):
    out = True
    for site_id in e_t_build:
        if site_dict[site_id].owner == 1 and site_dict[site_id].structure_type == 1 :
            x_t_site = site_dict[site_id].x
            y_t_site = site_dict[site_id].y
            destination_x = site_dict[site].x
            destination_y = site_dict[site].y
            r_site = site_dict[site_id].radius
            x_diff = (x_t_site - destination_x)**2
            y_diff = (y_t_site - destination_y)**2
            distance_t = math.sqrt(x_diff+y_diff) - r_site
            if distance_t < site_dict[site_id].param_2 : out = False
        else : del e_t_build[site_id]
    return out
            

def search():
    distance_min = 0
    for site in site_dict :
        if site_dict[site].owner == -1 or (site_dict[site].structure_type == 0 and site_dict[site].owner == 1) :
            x_site = site_dict[site].x
            y_site = site_dict[site].y
            r_site = site_dict[site].radius
            x_diff = (queen.x - x_site)**2
            y_diff = (queen.y - y_site)**2
            distance = math.sqrt(x_diff+y_diff) - r_site
            out = out_range(site)
            if distance_min == 0 or(distance_min > distance and out) :
                distance_min = distance 
                destination = site
    return destination
    # Move of the queen

def queen_move(closest_place):
    cmd = "" 
    if touched_site < 0 or site_dict[touched_site].structure_type >= 0 :
        cmd = "MOVE" + " " + str(site_dict[closest_place].x) + " " + str(site_dict[closest_place].y)

    else :
        building = choose_building(touched_site)
        cmd = "BUILD" + " " + str(touched_site) + " " + str(building)

    return cmd
def training(gold):
    cmd = "TRAIN"
    gold_c = gold
    if e_t_build == 0 : detect_ennemy_tower()
    for site in site_dict :
        if site_dict[site].owner == 0 :
            if site_dict[site].param_2 == 1 and gold_c >= 100 and Archer.count_a < 2:
                cmd += " "  + str(site)
                gold_c -= 100
            if site_dict[site].param_2 == 2 and gold_c >= 140 and e_t_build == 1 and Giant.count_g < 2:
                cmd += " "  + str(site)
                gold_c -= 140
            if site_dict[site].param_2 == 0 and gold_c >= 80 :
                cmd += " "  + str(site)
                gold_c -= 80
    return cmd
"""def closest_barracks(already_training):
    distance_min = 999999
    for site_id in site_dict :
        if site_dict[site_id].owner == 0 and str(site_id) not in already_training : 
            f_x_site = site_dict[site_id].x
            f_y_site = site_dict[site_id].y
            for e_site_id in site_dict :
                if site_dict[e_site_id].owner ==1 :
                    e_x_site = site_dict[e_site_id].x
                    e_y_site = site_dict[e_site_id].y
                    x_diff = abs(f_x_site-e_x_site)
                    y_diff = abs(f_y_site-e_y_site)
                    distance_c = math.sqrt(x_diff**2+y_diff**2)
                    if distance_min > distance_c :
                        distance_min = distance_c
                        c_barracks = site_id
    return c_barracks"""
def detect_ennemy_tower() :
    for site in site_dict :
        if site_dict[site].owner == 1 and site_dict[site].structure_type == 1: e_t_build[site] =+ 1

def choose_building(site):
    cmd = ""
    if len(e_t_build) == 0 : detect_ennemy_tower()
    if  len(mine) < 3 :
        cmd += "MINE"
        mine[site] =+ 1
    elif barracks == {} :
        cmd += "BARRACKS-KNIGHT"
        site_dict[site].bar_type = "BARRACKS-KNIGHT"
        barracks[site] = "BARRACKS-KNIGHT"
    else :
            cmd += "TOWER"
            tower[site] =+ 1
    return cmd


        

for i in range(num_sites):
    site_id, x, y, radius = [int(j) for j in input().split()]
    site_pos[site_id]={'x':x,'y':y,'r':radius}

# game loop
while True:
    gold, touched_site = [int(i) for i in input().split()]
    for i in range(num_sites):


        site_id, ignore_1, ignore_2, structure_type, owner, param_1, param_2 = [int(j) for j in input().split()]
        
        x = site_pos[site_id]['x']
        y = site_pos[site_id]['y']
        radius = site_pos[site_id]['r']
        site_dict[site_id] = Site(ignore_1, ignore_2, structure_type, owner, param_1, param_2, x, y, radius)
    num_units = int(input())
    for i in range(num_units):
        # unit_type: -1 = QUEEN, 0 = KNIGHT, 1 = ARCHER
        x, y, owner, unit_type, health = [int(j) for j in input().split()]
        if unit_type == -1 and owner == 0 :
            queen = Queen(x, y, owner, health)
        elif unit_type == 0 :
            count_k = Knight.count_k
            knight[count_k] = Knight(x, y, owner, health)
        elif unit_type == 1 :
            count_a = Archer.count_a
            archer[count_a] = Archer(x, y, owner, health)
        elif unit_type == 2 :
            count_g = Giant.count_g
            giant[count_a] = Giant(x, y, owner, health)

    

    closest_place = search()
    queen_cmd = queen_move(closest_place)
    training_cmd = training(gold)

    print(queen_cmd)
    print(training_cmd)

