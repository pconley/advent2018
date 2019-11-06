import copy, sys, re
import random, queue
import heapq

def convert(lines):
    data = []
    for line in lines : 
        match = re.search("^(.)=(.*), (.)=(.*)$", line.strip()) 
        if match :
            (x_ind,y_ind) = (2,4) if match.group(1)=='x' else (4,2)
            (x_str,y_str) = (match.group(x_ind),match.group(y_ind))
            # print((x_str,y_str))
            x_vals = [int(x) for x in x_str.split("..")]
            y_vals = [int(y) for y in y_str.split("..")]
            # print(x_vals,y_vals)
            x_range = range(x_vals[0],x_vals[-1]+1)
            y_range = range(y_vals[0],y_vals[-1]+1)
            data.append((x_range,y_range))
        else :
            raise AttributeError
    return data

def dimensions(data):
    x_max = y_max = 0
    x_min = y_min = 10000
    for (x_range,y_range) in data : 
        x_min = min(x_min,min(x_range))
        x_max = max(x_max,max(x_range))
        y_min = min(y_min,min(y_range))
        y_max = max(y_max,max(y_range))
    return (x_min, x_max, y_min, y_max)

def down(pos):
    (x,y) = pos
    return (x,y+1)
def left(pos):
    (x,y) = pos
    return (x-1,y)
def right(pos):
    (x,y) = pos
    return (x+1,y)

def sides(pos):
    (x,y) = pos
    # return [(x-1,y),(x+1,y)]

    # randomize the left and right
    n = random.choice([-1,1])
    return [(x-n,y),(x+n,y)]

class Canvas:
    def __init__(self,dims):
        self.left_margin = 3
        self.right_margin = 3
        self.bottom_margin = 1
        (self.x_min, self.x_max, self.y_min, self.y_max) = dims
        self.width = self.x_max - self.x_min + self.left_margin + self.right_margin + 1
        self.depth = self.y_max + self.bottom_margin + 1
        self.canvas = [ ['.' for c in range(self.width)] for r in range(self.depth)]
        self.area = self.width * self.depth
    def pset(self,pos,val):
        (x,y) = pos
        self.set(x,y,val)
    def set(self,x,y,value):
        c = x - self.x_min + self.left_margin
        r = y
        try :
            self.canvas[r][c] = value
        except :
            pass
    def pget(self,pos):
        (x,y) = pos
        return self.get(x,y)
    def get(self,x,y):
        r = y
        c = x - self.x_min + self.left_margin
        try :
            return self.canvas[r][c]
        except :
            return '.' # empty
    def is_empty(self,pos):
        return self.pget(pos) in ['.']
    def is_blocked(self,pos):
        return self.pget(pos) in ['#','~','|','>','<','?']
    def build(self,data):
        for (xr,yr) in data :
            for x in xr:
                for y in yr:
                    self.set(x,y,"#")
    def as_str(self,max_rows=1000):
        # print("draw:",self.x_min, self.x_max, self.y_min, self.y_max)
        area = ""
        for r in range(len(self.canvas)) :
            row = self.canvas[r]
            area += "{:5d}: ".format(r)+"".join(row)+"\n"
            if r > max_rows : break
        return area
    def is_in_a_pond(self,pos):

        # if this is part of a string of 0s that is bounded
        # by walls to the left right and bottom

        # look left
        (xx,yy) = pos
        while canvas.get(xx,yy) in ['0','~','|','.','<','>']:
            # print("Lpond: ",canvas.get(xx,yy+1))
            if canvas.get(xx,yy+1) not in ['~','#'] :
                return 1
            xx -= 1
        if canvas.get(xx,yy) != '#' : return 2
        # made it to a wall on left

        # look right
        (xx,yy) = pos
        while canvas.get(xx,yy) in ['0','~','|','.','<','>'] :
            # print("Rpond: ",canvas.get(xx,yy+1))
            if canvas.get(xx,yy+1) not in ['~','#'] :
                return 3
            xx += 1
        if canvas.get(xx,yy) != '#' : return 4
        # made it to a wall on right

        return 0

    def count(self):
        total = 0
        for r in range(self.depth-self.bottom_margin):
            for c in range(self.width):
                if self.canvas[r][c] in ['|','~','0','<','>'] :
                    total += 1
        return total

def relevant(pos):
    (x,y) = pos
    if y > canvas.depth : return False
    if canvas.get(x,y) == '~' : return False
    return True

class Node:
    def __init__(self,pos,parent):
        self.pos = pos
        (self.x,self.y) = pos
        self.parent = parent
        self.down = None
        self.left = None
        self.right = None
        self.resolved = False
    def __str__(self):
        return str(self.pos)
    def __lt__(self, other):
        return self.x < other.y


tree = []
heapq.heapify(tree)
node_set = set([])

def push(node):
    global tree, node_set
    print("set:", node_set)
    print("push:", node.pos)
    tuple = (-node.y,node)
    if tuple not in node_set:
        node_set.add(tuple)
        heapq.heappush(tree,tuple)

def pop():
    global tree, node_set
    (y,node) = heapq.heappop(tree)
    node_set = set(tree)
    return node

print ('Argument List:', str(sys.argv))
data_file = open(sys.argv[1],"r+")  
lines = data_file.readlines()
data = convert(lines)
dims = dimensions(data)
canvas = Canvas(dims)
canvas.build(data)

root = Node((500,0),None)
canvas.pset(root.pos,"+")

# print(canvas.as_str())

drops = []
created = 0
prev_count = -1
# cant be more than area drops
max_drops = 100 # 39000 # empirical

splits = []
heapq.heapify(splits)



push(root)
loops = 0
while not root.resolved :
    loops += 1

    current = pop()
    print("current = ",current.pos, current.resolved)
    # if current.resolved == 1 : 
    #     print("no action")
    #     continue

    # if we can flow down from current
    (bx,by) = below = down(current.pos)
    if by < canvas.depth and canvas.is_empty(below) :
        node = Node(below, current)
        canvas.pset(node.pos,"|")
        current.down = node
        print("down. push", node.pos)
        push(node)
        created += 1

    # flow left/right from current
    elif canvas.is_blocked(below) :
        added = 0
        spot = right(current.pos)
        if canvas.is_empty(spot) :
            node = Node(spot, current)
            canvas.pset(spot,"<")
            current.right = node
            print("right. push", node.pos)
            push(node)
            created += 1
            added += 1
        spot = left(current.pos)
        if canvas.is_empty(spot) :
            node = Node(spot, current)
            canvas.pset(spot,">")
            current.left = node
            print("left. push", node.pos)
            push(node)
            created += 1
            added += 1

        if added > 0 :
            print("split: put back on queue to reprocess")
            heapq.heappush(splits,current)
        else :
            print("blocked")
            # v = canvas.is_in_a_pond(current.pos)
            # print(current.pos, "is blocked!!!! v=",v)
            # if v == 0 :
            #     canvas.pset(current.pos,"~")
            #     parent = current.parent
            #     push(parent)

    else :
        pass
        # raise NotImplementedError

    if loops > 0 :
        print(canvas.as_str())
        print("The 10 smallest numbers in list are : ",end="") 
        print(" ".join([str(node.pos) for (y,node) in heapq.nsmallest(10, tree)]))
        print("The splits are : ",end="") 
        print(" ".join([str(node.pos) for node in heapq.nsmallest(10, splits)]))

        input("{}: Continue?".format(loops))



print(canvas.as_str())
print("count = ",canvas.count())

