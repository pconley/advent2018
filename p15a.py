rows = [ # example 1
    "#######",
    "#E..G.#",
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

map = [ [x for x in row] for row in rows ]

def mstring(map):
    return "\n".join([ "".join(row) for row in map ])


ELF = "E"
GOB = "G"

class Creature:
    def __init__(self,race,pos):
        self.race = race
        self.pos = pos
        self.points = 200
        self.power = 3

creatures = {
    ELF : [],
    GOB : []
}

def adjacents(pos):
    (r,c) = pos
    return [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]

def is_race(marker):
    return marker == GOB or marker == ELF

def other(marker):
    if marker == GOB : return ELF
    if marker == ELF : return GOB
    raise ValueError

def is_empty(pos):
    (r,c) = pos
    return map[r][c] == '.'

def empty(arr):
    return [ x for x in arr if is_empty(x) ]


for i in range(len(map)):
    row = map[i]
    for j in range(len(row)):
        marker = row[j]
        if( is_race(marker) ):
            creatures[marker].append(Creature(marker,(i,j)))

def cstring(arr):
    return " ".join([ "({},{})".format(x.pos[0],x.pos[1]) for x in arr])

class Adjacents:
  
    def __init__(self,pos):
        (self.r, self.c) = pos
        self.adjs = [(self.r-1,self.c),(self.r+1,self.c),(self.r,self.c-1),(self.r,self.c+1)]
 
    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.adjs):
            self.counter += 1
            return self.adjs[self.counter-1]
        else:
            raise StopIteration

import copy
import queue
from itertools import chain
from operator import itemgetter, attrgetter

def xadjacents(race):
    # return all adjecnt squares to a given race
    return [ a for creature in creatures[race] for a in Adjacents(creature.pos)]

def msetter(map,char,arr):
    tmp = copy.deepcopy(map)
    for (r,c) in arr: 
        tmp[r][c] = char
    return tmp

def find_path(pos1,pos2):
    # print("find_path?",pos1,pos2)
    # is there a path from pos1 to pos2?
    q = queue.Queue()
    q.put((pos1,[]))
    visited = []
    while not q.empty() :
        (x,p2x) = q.get()
        # print(x, p2x, visited)
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

def select_path(creature):
    all_opponent_adjacents = xadjacents(other(creature.race))
    opponent_spots = empty(all_opponent_adjacents)

    # print("adjacents:")
    # print(mstring(msetter(map,"?",opponent_spots)))

    path_tuples = [find_path(elf.pos,x) for x in opponent_spots]
    paths = [p for (x,p) in path_tuples if x]

    # print("reacable:")
    # reachable_spots = [p[-1] for p in paths]
    # print(mstring(msetter(map,"@",reachable_spots)))

    shortest_len = min([len(p) for p in paths])
    nearest_paths = [p for p in paths if len(p) == shortest_len ]
    # second spot in the path is the first move to take
    nearest_paths.sort(key=second)

    # print("nearest:")
    # nearest_spots = [p[-1] for p in nearest_paths]
    # print(mstring(msetter(map,"+",[nearest_spots[0]])))

    # return the PATH to the nearest reachable adjacent 
    # spot that is sorted by reading order

    return nearest_paths[0] 

##### 

print(mstring(map))
print("Elves:",cstring(creatures[ELF]))
print("Goblins:",cstring(creatures[GOB]))

elf = creatures[ELF][0]

path = select_path(elf)
print("path = ",path)

print("target", path[-1])
print(mstring(msetter(map,"!",[path[-1]])))
print("move". path[1])
print(mstring(msetter(map,"+",[path[1]])))
