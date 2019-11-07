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
        # return self.pget(pos) in ['#','~','|','>','<']
        return self.pget(pos) in ['#','~','|']
    def build(self,data):
        for (xr,yr) in data :
            for x in xr:
                for y in yr:
                    self.set(x,y,"#")
    def as_str(self,max_rows=2000):
        # print("draw:",self.x_min, self.x_max, self.y_min, self.y_max)
        area = ""
        for r in range(len(self.canvas)) :
            row = self.canvas[r]
            area += "{:5d}: ".format(r)+"".join(row)+"\n"
            if r > max_rows : break
        return area
    def is_still_water(self,pos):
        # if this is part of a string of ?s 
        # that is bounded by walls to the left right 
        # look left
        (xx,yy) = pos
        while canvas.get(xx,yy) == '?':
            xx -= 1
        if canvas.get(xx,yy) != '#' : return None
        leftie = xx+1
        # made it to a wall on left
        # look right
        (xx,yy) = pos
        while canvas.get(xx,yy) == '?' :
            xx += 1
        if canvas.get(xx,yy) != '#' : return None
        rightie = xx-1
        # made it to a wall on right
        return range(leftie,rightie+1)
    def count(self):
        total = 0
        for r in range(self.depth-self.bottom_margin):
            row_count = 0
            for c in range(self.width):
                # if self.canvas[r][c] in ['|','~','0','<','>','?'] :
                if self.canvas[r][c] not in ['.','#','+'] :
                    row_count += 1
            # if r > 1800 : print(r,row_count)
            if r < 100 : print(r,row_count)
            total += row_count
        return total

class Node:
    def __init__(self,pos,parent):
        self.pos = pos
        (self.x,self.y) = pos
        self.parent = parent
        self.down = None
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.pos)
    def __lt__(self, other):
        return self.x < other.y

def push(heap,node):
    # print("push:", node.pos)
    tuple = (-node.y,node)
    heapq.heappush(heap,tuple)

def pop(heap):
    (_,node) = heapq.heappop(heap)
    return node

print ('Argument List:', str(sys.argv))
run_to = int(sys.argv[2])
data_file = open(sys.argv[1],"r")
lines = data_file.readlines()
data = convert(lines)
dims = dimensions(data)
print("dimensions",dims)
canvas = Canvas(dims)
canvas.build(data)

root = Node((500,0),None)
canvas.pset(root.pos,"+")

# print(canvas.as_str(100))
# exit()

created = 0
cursors = []
heapq.heapify(cursors)
push(cursors,root)

loops = 0
while cursors :
    loops += 1

    current = pop(cursors)

    print("current = ",current.pos)

    # if we can flow down from current
    (bx,by) = below = down(current.pos)

    if by >= canvas.depth :
        pass
    
    elif canvas.pget(current.pos) == "~" :
        pass
    
    elif canvas.is_empty(below) :
        node = Node(below, current)
        canvas.pset(node.pos,"|")
        current.down = node
        print("down. push", node.pos)
        push(cursors,node)
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
            push(cursors,node)
            created += 1
            added += 1
        spot = left(current.pos)
        if canvas.is_empty(spot) :
            node = Node(spot, current)
            canvas.pset(spot,">")
            current.left = node
            print("left. push", node.pos)
            push(cursors,node)
            created += 1
            added += 1

        if added == 2 :
            print("split")
            # heapq.heappush(cursors,current)
        elif added == 1 :
            print("one added")
        elif added == 0 :
            canvas.pset(current.pos,"?")
            print(current.pos,"blocked... put parent")
            push(cursors,current.parent)
            v_range = canvas.is_still_water(current.pos)
            print(current.pos, "is blocked!!!! v_range=",v_range)
            if v_range :
                for x in v_range :
                    canvas.set(x,current.y,"~")
        else :
            pass
            # raise NotImplementedError

    else :
        pass
        # raise NotImplementedError

    if loops > run_to :
        # print(canvas.as_str(20))
        # print("The cursors are : ",end="") 
        # print(" ".join([str(node.pos) for (y,node) in heapq.nsmallest(10, cursors)]))

        cont = input("{}: Continue?".format(loops))
        try :
            cont = int(cont)
        except :
            cont = 1
        run_to += cont

print(canvas.as_str(2000))
print("count = ",canvas.count())

