data = [
    (224, 153),
    (176, 350),
    (353, 241),
    (207, 59),
    (145, 203),
    (123, 210),
    (113, 203),
    (191, 241),
    (172, 196),
    (209, 249),
    (260, 229),
    (98, 231),
    (305, 215),
    (258, 141),
    (337, 282),
    (156, 140),
    (325, 197),
    (179, 279),
    (283, 233),
    (317, 150),
    (305, 245),
    (67, 109),
    (251, 140),
    (245, 59),
    (173, 105),
    (59, 173),
    (257, 70),
    (269, 110),
    (102, 162),
    (179, 180),
    (324, 112),
    (357, 311),
    (317, 245),
    (239, 112),
    (321, 220),
    (133, 97),
    (334, 99),
    (117, 102),
    (133, 112),
    (222, 316),
    (68, 296),
    (150, 287),
    (263, 263),
    (66, 347),
    (128, 118),
    (63, 202),
    (68, 236),
    (264, 122),
    (77, 243),
    (92, 110)
]

# import Queue
import copy

# data = [(1, 1),(1, 6),(8, 3),(3, 4),(5, 5),(8, 9)]

EMPTY = '-'
OVERLAP = '.'

size = 0
for (x,y) in data:
    if x > size : size = x
    if y > size : size = y
print "max coordinate is", size
size += 2 # some buffer

canvas = [ [ EMPTY for i in range(0,size) ] for i in range(0,size) ]
previous_canvas = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
letters = alphabet[0:len(data)] # just enough letters to use
print(letters)

def set(letter, x, y):
    if x < 0 or x > size-1: return
    if y < 0 or y > size-1: return
    if previous_canvas[x][y] != EMPTY :
        # prev was already populated
        return

    elif canvas[x][y] == EMPTY :
        # prev was empty and current is empty
        canvas[x][y] = letter

    elif canvas[x][y] == letter:
        # prev was empty, but curr has my letter
        return

    else:
        # prev was empty, but curr has another letter
        canvas[x][y] = OVERLAP

def mdist(x1,y1,x2,y2):
    # calc manhattan distance
    x = abs(x1-x2)
    y = abs(y1-y2)
    return x+y

def expand(letter, x, y, dist):
    cnt = 0
    for i in range(size):
        for j in range(size):
            d = mdist(x,y,i,j)
            if d == dist :
                set(letter,i,j)
                cnt += 1
                # cprint(previous_canvas)
                # if cnt > 3 : exit(0)

# place initial letters
count = 0
for (x,y) in data:
    canvas[y][x] = letters[count]
    count += 1


def cprint(canvas):
    count = 0
    for row in canvas :
        print "{0:5d} : ".format(count)+"".join(row)
        count += 1


def is_full(canvas):
    for i in range(size):
        for j in range(size):
            if canvas[i][j] == EMPTY : return False
    return True

def is_on_edge(x, y):
    if x == 0 or x == size-1: return True
    if y == 0 or y == size-1: return True   
    return False

def is_internal(letter):
    count = 0 
    for i in range(size):
        for j in range(size):
            if canvas[i][j] == letter : 
                if is_on_edge(i,j):
                    return 0
                count += 1
    return count # every instance of letter passed safe check


# print("start")
# cprint(canvas)

# expand
for round in range(size):
    if is_full(canvas): break
    previous_canvas = copy.deepcopy(canvas)
    index = 0
    for (x,y) in data:
        expand(letters[index], y, x, round)
        index += 1
    # print "\nround", round
    # cprint(canvas)
    print "round", round, "of", size


max = 0
letter = ""
for l in letters:
    area = is_internal(l)
    if area == 0: # infinite
        print(l, "is infinite")
    else :
        print(l, "area = ", area)
        if area > max : 
            max = area
            letter = l

print letter, "has max area of", max
