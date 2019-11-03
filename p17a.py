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
    return [(x-1,y),(x+1,y)]

    # randomize the left and right
    # n = random.choice([-1,1])
    # return [(x-n,y),(x+n,y)]

class Canvas:
    def __init__(self,dims):
        self.left_margin = 3
        self.right_margin = 3
        self.bottom_margin = 1
        (self.x_min, self.x_max, self.y_min, self.y_max) = dims
        self.width = self.x_max - self.x_min + self.left_margin + self.right_margin + 1
        self.depth = self.y_max + self.bottom_margin + 1
        self.canvas = [ ['.' for c in range(self.width)] for r in range(self.depth)]
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
    def as_str(self,max_rows=100):
        # print("draw:",self.x_min, self.x_max, self.y_min, self.y_max)
        area = ""
        for r in range(len(self.canvas)) :
            row = self.canvas[r]
            area += "{:5d}: ".format(r)+"".join(row)+"\n"
            if r > max_rows : break
        return area
    def count(self):
        total = 0
        for r in range(self.depth-self.bottom_margin):
            for c in range(self.width):
                if self.canvas[r][c] in ['|','~','0'] :
                    total += 1
        return total

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


stop = False
drops = []
incr = 5
while True:
    for n in range(incr):
        drops.append((s_x,s_y))
        canvas.set(s_x,s_y,"0")
        # then move all the drops one step
        for i in range(len(drops)) :
            (dx,dy) = drops[i]
            if dy > canvas.depth : continue # ignore
            if canvas.get(dx,dy) == '~' : continue # ignore
            # move to the first, empty adjacent
            # always try down first...
            (ax,ay) = down(drops[i])

            # if down is empty
            if canvas.is_empty(ax,ay): 
                # make the move to a
                canvas.set(dx,dy,'|')
                canvas.set(ax,ay,'0')
                drops[i] = (ax,ay)
                continue # to next drop
            # or if down is drop-blocked
            elif canvas.get(ax,ay) == 'O' : 
                continue # skip this one
            # or try left/right
            else :
                moved = False
                for (ax,ay) in sides(drops[i]):
                    if not moved and canvas.is_empty(ax,ay):
                        # make the move to a
                        canvas.set(dx,dy,'|')
                        canvas.set(ax,ay,'0')
                        drops[i] = (ax,ay)
                        moved = True
                if moved : continue

            print("no move to make")
            canvas.set(dx,dy,'~')

    canvas.set(s_x,s_y,"+") 
    print(canvas.as_str())

    x = input(" Continue?")
    try:
        incr = int(x)
    except:
        incr = 1




print("count = ",canvas.count())
# for (dx,dy) in drops :
#     if dy <= canvas.depth :
#         print(dx,dy)
