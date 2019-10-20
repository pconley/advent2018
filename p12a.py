
rules = { # the example
    "...##" : True,
    "..#.." : True,
    ".#..." : True,
    ".#.#." : True,
    ".#.##" : True,
    ".##.." : True,
    ".####" : True,
    "#.#.#" : True,
    "#.###" : True,
    "##.#." : True,
    "##.##" : True,
    "###.." : True,
    "###.#" : True,
    "####." : True,
}

rules = { # my real rules
    "#####": True,
    ".#..#": True,
    "#..#.": True,
    "#...#": True,
    "...##": True,
    "##..#": True,
    ".#.##": True,
    "#.###": True,
    ".##.#": True,
    ".#...": True,
    "##...": True,
    "##.##": True,
    "##.#.": True,
    "#.##.": True,
}

def count(text, c):
    return sum([1 for i in range(len(text)) if text[i]==c ])

def mprint(n,line):
    cnt = count(line,'#')
    print("[{:3d}] {:5d}: ".format(cnt,n)+line)

header_row1 =   "          1    1    2    2    3"
header_row2 =   "0....5....0....5....0....5....0"
initial_state = "#..#.#..##......###...###"
initial_state = "##.#....#..#......#..######..#.####.....#......##.##.##...#..#....#.#.##..##.##.#.#..#.#....#.#..#.#"


def apply(state):
    next_state_arr = [ '.' for i in range(len(state))]
    for pos in range(2,len(state)-4):
        situ = state[pos:pos+5]
        # print("consider: {} : {}".format(situ,rules.get(situ)))
        next_state_arr[pos+2] = "#" if rules.get(situ) else "."
        
    return "".join(next_state_arr)

leader = 25
state = initial_state
buffer = "".join([ "." for i in range(leader)])
full_pots = buffer + initial_state + buffer
mprint(0, buffer+header_row1)
mprint(0, buffer+header_row2)
mprint(0,full_pots)
pcnt = count(full_pots,'#')
for i in range(20):
    full_pots = apply(full_pots)
    pcnt += count(full_pots,'#')
    mprint(i+1,full_pots)

total = 0
for i in range(len(full_pots)):
    if full_pots[i] == '#':
        total += i-leader
print(total)
