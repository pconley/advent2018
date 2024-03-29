import copy, sys, re
import random

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
    def set(self,x,y,value):
        c = x - self.x_min + self.left_margin
        r = y
        try :
            self.canvas[r][c] = value
        except :
            pass
    def get(self,x,y):
        r = y
        c = x - self.x_min + self.left_margin
        try :
            return self.canvas[r][c]
        except :
            return '.' # empty
    def is_empty(self,x,y):
        return self.get(x,y) in ['.','|']
    def build(self,data):
        for (xr,yr) in data :
            for x in xr:
                for y in yr:
                    self.set(x,y,"#")
    def as_str(self,max_rows=200):
        # print("draw:",self.x_min, self.x_max, self.y_min, self.y_max)
        area = ""
        for r in range(len(self.canvas)) :
            row = self.canvas[r]
            area += "{:5d}: ".format(r)+"".join(row)+"\n"
            if r > max_rows : break
        return area
    def region(self,r,c,d,w):
        # print("draw:",self.x_min, self.x_max, self.y_min, self.y_max)
        area = ""
        for i in range(r,r+d) :
            if r+d < canvas.depth :
                row = "".join(self.canvas[i][c:c+w])
                area += "{:5d}: ".format(r)+"".join(row)+"\n"
        return area
    def is_in_full_pond(self,x,y):

        # if this is part of a string of 0s that is bounded
        # by walls to the left right and bottom

        # look left
        (xx,yy) = (x,y)
        while canvas.get(xx,yy) in ['0','~']:
            # print("Lpond: ",canvas.get(xx,yy+1))
            if canvas.get(xx,yy+1) not in ['~','#'] :
                return 1
            xx -= 1
        if canvas.get(xx,yy) != '#' : return 2
        # made it to a wall on left

        # look right
        (xx,yy) = (x,y)
        while canvas.get(xx,yy) in ['0','~'] :
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
                if self.canvas[r][c] in ['|','~','0'] :
                    total += 1
        return total

def relevant(pos):
    (x,y) = pos
    if y > canvas.depth : return False
    if canvas.get(x,y) == '~' : return False
    return True

print ('Argument List:', str(sys.argv))
data_file = open(sys.argv[1],"r+")  
lines = data_file.readlines()
data = convert(lines)
dims = dimensions(data)
canvas = Canvas(dims)
(s_x,s_y) = (500,0)
canvas.set(s_x,s_y,"+")
canvas.build(data)

# print(canvas.as_str())

linked = []

drops = []
looper = 0
created = 0
prev_count = -1
# cant be more than area drops
max_drops = 50000 # empirical
while created < max_drops:
    if created%1000 == 0 :
        drops = [d for d in drops if relevant(d)]
        count = canvas.count()
        print(created,"of",max_drops,"relevant=",len(drops),"count=",count,"({})".format(count-prev_count))
        if count == prev_count :
            print("no count change... exiting")
            break
        prev_count = count

    if looper%2 == 0 :
        drops.append((s_x,s_y))
        created += 1
    looper += 1
    canvas.set(s_x,s_y,"0")
    # then move all the drops one step
    for i in range(len(drops)) :
        (dx,dy) = drop = drops[i]
        if not relevant(drop) : continue

        # always try down first...
        (ax,ay) = down(drop)

        # if down is empty
        if canvas.is_empty(ax,ay): 
            # make the move to a
            canvas.set(dx,dy,'|')
            canvas.set(ax,ay,'0')
            drops[i] = (ax,ay)
        # or if down is drop-blocked
        elif canvas.get(ax,ay) == '0' :
            # print((dx,dy),"O blocked by",(ax,ay)) 
            pass # skip this one
        # or try left/right
        else :
            moved = False
            for (ax,ay) in sides(drop):
                if not moved and canvas.is_empty(ax,ay):
                    # make the move to a
                    canvas.set(dx,dy,'|')
                    canvas.set(ax,ay,'0')
                    drops[i] = (ax,ay)
                    moved = True
            if not moved :
                v = canvas.is_in_full_pond(dx,dy)
                # print((dx,dy),"had no move to make. v = ",v)
                if v == 0 : canvas.set(dx,dy,'~')

    canvas.set(s_x,s_y,"+") 
    print(canvas.region(0,0,100,200))
    input("Continue?")

canvas.set(s_x,s_y,"+") 
print(canvas.as_str())
print("count = ",canvas.count())

