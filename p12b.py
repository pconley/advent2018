
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

def as_chars(arr):
    return [ ("#" if x else ".") for x in arr]

def as_str(arr):
    return "".join(as_chars(arr))

def as_bool(arr):
    return [ (x=='#') for x in arr]

def count(text, c):
    return sum([1 for i in range(len(text)) if text[i]==c ])

def mprint(n,arr):
    line = "".join([("#" if x else ".") for x in arr[:60]])
    print("{:5d}: ".format(n)+line)

# initial_state = "#..#.#..##......###...###"
initial_state = "##.#....#..#......#..######..#.####.....#......##.##.##...#..#....#.#.##..##.##.#.#..#.#....#.#..#.#"

def any(arr):
    for a in arr: 
        if a : return True
    return False

def get_rule_for(situation):
    s = as_str(situation)
    rule = rules.get(s,False)
    # print(s, ">>", rule)
    return rule

origin = 0
state = []

def apply():
    global origin
    # mprint(111,state)
    # grow the front of the state as necessary
    if any(state[:5]) :
        state.insert(0, False)
        state.insert(0, False)
        state.insert(0, False)
        state.insert(0, False)
        state.insert(0, False)
        origin += 5
        # mprint(222,state)

    ### pad the end of the state as necessary
    if any(state[-5:]):
        state.append(False)
        state.append(False)
        state.append(False)
        state.append(False)
        state.append(False)
        # mprint(333,state)

    zero = state[0] 
    one  = state[1]
    for pos in range(2,len(state)-4):
        situation = [zero,one] + state[pos:pos+3]
        # mprint(0,state)
        # print(pos, "situation = ", situation)
        # remember before the change (for next loop)
        zero = one
        one = state[pos]
        # apply the rule for this situatiopn
        rule = get_rule_for(situation)
        # print("rule = ", str(rule))
        state[pos] = get_rule_for(situation)

    return

# convert initial state to a boolean state array
state = [ (x=='#') for x in initial_state]
mprint(0,state)
generations = 50000000000
for i in range(20):
    apply()
    if i+1 % 100 == 0 :
        mprint(i+1,state)

mprint(0,state)
        
total = 0
print("origin = ", origin)
for i in range(len(state)):
    if state[i]:
        total += i-origin
print(total)
