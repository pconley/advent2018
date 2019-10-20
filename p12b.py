
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

def count(arr):
    return sum([1 for x in arr if x==True ])

def mprint(n,arr):
    print("{:5d}: ".format(n)+as_str(arr))


initial_state = "#..#.#..##......###...###"
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

    # shorten the front of the state as possible
    if not any(state[:10]) :
        del state[0]
        del state[0]
        del state[0]
        del state[0]
        del state[0]
        origin -= 5
        # mprint(222,state)

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

def value():
    global origin
    total = 0
    for i in range(len(state)):
        if state[i]: total += i-origin
    return total

def same(state1, state2):
    if len(state1) != len(state2) : return False
    for i in range(len(state1)):
        if state1[i] != state2[i] : return False
    return True

import copy

# convert initial state to a boolean state array
state = [ (x=='#') for x in initial_state]
print("[{:5d}] {:5d}: ".format(count(state),0)+as_str(state[:60]))
mprint(0,state)
prev_state = copy.deepcopy(state)
generations = 50000000000
generations = 500000000
generations = 30
for i in range(100000):
    apply() # changes the state
    if (i<30) or ((i+1) % 10000) == 0 :
        print("{:5d}: count={} len={} origin={} value={} :".format(i+1, count(state), len(state), origin, value())+as_str(state[-20:]))
    # print("prev: "+str(prev_state))
    # print("curr: "+str(state))
    if same(prev_state,state) : 
        print("steady state")
        break
    prev_state = copy.deepcopy(state)


mprint(0,state)
        
total = 0
print("origin = ", origin)
print("value = "+str(value()));

# So, what is different in this solution is that we do NOT actually
# let the program run to completion... that would take a VERY long
# time.  BUT - we noticed a pattern that repeats and allows us to 
# calculate the final value (using a spreadsheet)
