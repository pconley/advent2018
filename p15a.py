xrows = [ # example 1
    "#######",
    "#E..G.#",
    "#...#.#",
    "#.G.#G#",
    "#######",
]

xrows = [ # my test example
    "#######",
    "#E....#",
    "#...#.#",
    "#.G.#G#",
    "#######",
]

xrows = [ # example 2
    "#######",
    "#.E...#",
    "#.....#",
    "#...G.#",
    "####### ",
]

xrows = [
    "#########",
    "#G..G..G#",
    "#.......#",
    "#.......#",
    "#G..E..G#",
    "#.......#",
    "#.......#",
    "#G..G..G#",
    "#########",
]

xrows = [  # full combat example
    "#######",
    "#.G...#",
    "#...EG#",
    "#.#.#G#",
    "#..G#E#",
    "#.....#",
    "#######",
]

map = []

def mstring(map):
    text = ""
    for r in range(len(map)) :
        row = map[r]
        map_text = "".join([str(x) for x in row])
        player_text = " {} >> ".format(r)
        for cell in row:
            if is_player(cell.marker):
                player_text += "{}({}) ".format(cell,cell.points)
        text += map_text + player_text + "\n"
    return text

def mset(pos,value,target=map):
    (r,c) = pos
    target[r][c] = value

def mget(pos):
    (r,c) = pos
    return map[r][c]

def debug(*argv):
    print(*argv)
    pass

ELF = "E"
GOB = "G"
POWER = 3
MAX_POINTS = 200

class Marker:
    def __init__(self,marker):
        self.marker = marker
        # some creature values
        self.points = MAX_POINTS
        self.power = POWER
    def __str__(self):
        return self.marker

def adjacents(pos):
    (r,c) = pos
    # not this is very specifically the reading order
    return [(r-1,c),(r,c-1),(r,c+1),(r+1,c)]

def is_player(marker):
    return marker == GOB or marker == ELF

def other(marker):
    if marker == GOB : return ELF
    if marker == ELF : return GOB
    raise ValueError

def is_empty(pos):
    # print("is_empty",pos,mget(pos),map[1][3])
    return mget(pos).marker == '.'

def contains(positions, marker):
    return [x for x in positions if mget(x).marker == marker]
    # for pos in positions :
    #     # if any match then true...
    #     if mget(pos).marker == marker : return True
    # return False

def empty(positions):
    return [ x for x in positions if is_empty(x) ]

def filter(positions,marker):
    return [ pos for pos in positions if mget(pos).marker == marker ]

class Adjacents:
  
    def __init__(self,pos):
        (self.r, self.c) = pos
        self.adjs = adjacents(self.r,self.c)
 
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.adjs):
            self.counter += 1
            return self.adjs[self.counter-1]
        else:
            raise StopIteration

import sys
import copy
import queue
from itertools import chain
from operator import itemgetter, attrgetter

def xadjacents(positions):
    return [a for pos in positions for a in adjacents(pos)]

def msetter(map,char,positions):
    tmp = copy.deepcopy(map)
    for pos in positions: 
        mset(pos,Marker(char),tmp)
    return tmp

exit_count = 0
def exit_after(n):
    global exit_count
    exit_count += 1
    if exit_count >= n : exit()

def find_path(pos1,pos2):
    debug("find_path?",pos1,pos2)
    # is there a path from pos1 to pos2?
    q = queue.Queue()
    q.put((pos1,[]))
    visited = []
    while not q.empty() :
        (x,p2x) = q.get()
        debug(x, p2x, visited)
        # exit_after(5)
        if x == pos2 :
            # print("found with path",p2x+[x])
            return (True,p2x+[x])
        visited.append(x)
        p2k = copy.deepcopy(p2x)
        p2k.append(x)
        # print("p2k =",p2k)
        for k in empty(adjacents(x)):
            if not k in visited :
                q.put((k,p2k))
    return (False,[])

def second(path):
    return path[1]

def select_path(tuple):
    (player,pos) = tuple
    other_marker = other(player.marker)
    debug("select path:",player,pos)
    opponent_tuples = get_player_tuples(map,other_marker)
    positions = set([ x for (p,x) in opponent_tuples])
    all_opponent_adjacents = set(xadjacents(positions))
    debug("all_opponent_adjacents",all_opponent_adjacents)
    opponent_spots = empty(all_opponent_adjacents)

    debug("opponent spots:")
    debug(mstring(msetter(map,"?",opponent_spots)))
    path_tuples = [
        (pos,x) for x in opponent_spots]
    debug("paths tuples = ",path_tuples)
    paths = [p for (x,p) in path_tuples if x]
    debug("paths = ",paths)
    if not paths : return None

    debug("paths:")
    for p in paths : debug(p)
    debug("reachable:")
    reachable_spots = [p[-1] for p in paths]
    debug(mstring(msetter(map,"@",reachable_spots)))

    shortest_len = min([len(p) for p in paths])
    nearest_paths = [p for p in paths if len(p) == shortest_len ]
    # second spot in the path is the first move to take
    nearest_paths.sort(key=second)

    debug("nearest:")
    for p in nearest_paths: debug(p)
    debug("nearest one:",nearest_paths[0])
    nearest_spots = [p[-1] for p in nearest_paths]
    debug(mstring(msetter(map,"+",[nearest_spots[0]])))

    # return the PATH to the nearest reachable adjacent 
    # spot that is sorted by reading order

    return nearest_paths[0] 

def get_player_tuples(map,target_marker=None):
    tuples = []
    for i in range(len(map)):
        row = map[i]
        for j in range(len(row)):
            obj = row[j] # maybe player
            if( is_player(obj.marker) ):
                if not target_marker or target_marker == obj.marker :
                    tuples.append((obj,(i,j)))
    return tuples

def find_creature(creatures,pos):
    for c in creatures:
        if c.pos == pos : return c
    return None

def find_by_attr(targets,value,field):
    results = []
    return results

def attack(player,pos,neighbor_positions):
    low = MAX_POINTS+1
    for (r,c) in neighbor_positions :
        n = map[r][c]
        if n.points < low :
            low = n.points
            save_pos = (r,c)
    # debug("lowest is",low,save_pos,save_obj)
    all_lowest = [x for x in neighbor_positions if mget(x).points == low]
    if len(all_lowest) > 1 : 
        print("**********",len(all_lowest))
        print(all_lowest)
        print(sorted(all_lowest)[0])
    
    save_pos = sorted(all_lowest)[0]
    save_obj = mget(save_pos)
    save_obj.points = max(0,save_obj.points-player.power)
    debug("attack", player, pos, "hits", save_obj, save_pos, "result=", save_obj.points)
    if save_obj.points == 0 :
        # debug("attack", player, pos, "hits", save_obj, save_pos, "result=", save_obj.points)

        # remove the saved object by setting to empty
        debug("remove",save_obj,save_pos)
        mset(save_pos,Marker('.'),map)
        remaining = get_player_tuples(map,save_obj.marker)
        if len(remaining) == 0 :
            print("game over")
            return True
    return False

def main():

    global map
    print("Initially:")
    print(mstring(map))

    for round in range(300):
        players = get_player_tuples(map)
        for (player,pos) in players:

            # in case the player had been removed
            if mget(pos).marker == '.' : continue

            # print("Round",round,">> tuple",player,pos)
            neighbor_positions = filter(adjacents(pos),other(player.marker))
            if neighbor_positions :
                # print("ATTACK")
                game_over = attack(player,pos,neighbor_positions)
                if game_over :
                    break

            else :
                # move the 'player' based on where the opponents sit
                new_pos = get_move((player,pos))
                if new_pos :
                    # print("move", player, "from", pos, "to", new_pos)
                    mset(new_pos,player,map)
                    mset(pos,Marker("."),map)
                    # after a move we might still attack
                    neighbor_positions = filter(adjacents(new_pos),other(player.marker))
                    if neighbor_positions :
                        # print("ATTACK after move")
                        game_over = attack(player,new_pos,neighbor_positions)
                        if game_over :
                            break

        else:
            # if round in [0,1,3,4,5,22,23,24,25,26,27]:
            print("After {} Rounds:".format(round+1))
            print(mstring(map))
            continue

        break

    print("\nFinal:".format(round+1))
    print(mstring(map))

    print("rounds = ",round)
    survivor_tuples = get_player_tuples(map)
    points = sum([ x.points for (x,p) in survivor_tuples ])
    print("points = ",points)
    print(points * (round))


def get_move(tuple):
    (player,pos) = tuple
    opp_marker = other(player.marker)
    full = set([])
    sets = []
    prev = [pos]
    for i in range(1000):
        adjs = xadjacents(prev)
        opponents = set(contains(adjs,opp_marker))
        if opponents : 
            # some of cells adjacent to the prev contain an opponent
            # so that means that those in prev are a target cells
            targets = [ q for q in prev if contains(adjacents(q),opp_marker)]
            # if targets : print("targets",targets)
            break
        curr = set(empty(adjs))
        news = curr - full
        full.update(news)
        # print("news",news)
        # print("full",full)
        sets.append(news)
        # m = copy.deepcopy(map)
        # for s in range(len(sets)) :
        #     m = msetter(m,str(s%10),sets[s])
        # print(mstring(m))

        prev = sets[-1]

    # for s in range(len(sets)) :
    #     m = msetter(m,str(s%10),sets[s])
    # print(mstring(m))

    #### now do a back track to save only connected cells

    sets.append(opponents)
    for s in range(len(sets)-2,-1,-1):
        # print("\nprev", sets[s+1])
        adjs = set(xadjacents(sets[s+1]))
        # print("adj to prev:", adjs)
        # print(s,"curr:", sets[s])
        sets[s] = adjs.intersection(sets[s])
        # print(s,"new set:", sets[s])

    # m = copy.deepcopy(map)
    # for s in range(len(sets)-1) :
    #     m = msetter(m,str(s%10),sets[s])
    # print(mstring(m))

    # there may b e no move to make
    if not sets[0] : return None

    # the MOVE is the first of set Zero in read order
    move = sorted(list(sets[0]))[0]
    # print("move: ",move)
    return move

# data file name is command line argument
print ('Argument List:', str(sys.argv))

data_file = open(sys.argv[1],"r+")  
rows = data_file.readlines()
map = [ [Marker(x) for x in row.rstrip('\n')] for row in rows ]
print("\n\n\n\n\n\n")
main() 