
current = 0
marbles = [0] # with first stone

def fmt(idx,m):
    f = "({})" if idx == current else " {} "
    return f.format(m)

# for idx, val in enumerate(ints):

def mprint(p):
    global marbles
    print str(p)+": "+"".join([fmt(idx,m) for (idx,m) in enumerate(marbles)])

def place(player, val, current):
    global marbles, players
    if val % 23 == 0:
        # the current player keeps the marble they would have placed, 
        # adding it to their score. In addition, the marble 7 marbles 
        # counter-clockwise from the current marble is removed from 
        # the circle and also added to the current player's score.
        pos = get_anticlock(current,7)
        # print "special=",marbles[pos]
        players[player] += val + marbles[pos]
        marbles = marbles[:pos]+marbles[pos+1:]
        return pos
    else:
        # place after one clockwise
        pos = get_clockwise(current,1)
        marbles = marbles[0:pos+1]+[val]+marbles[pos+1:]
        return pos+1

mprint(0)

def get_clockwise(n,m):
    # m clockwise of n
    return (n+m) % len(marbles)

def get_anticlock(n,m):
    # m anti of pos n
    return (n-m) % len(marbles)

# 13 players; last marble is worth 7999 points: high score is 146373
# 463 players; last marble is worth 71787 points
PLAYERS = 463
TOPSTONE = 100*71787
players = [0 for i in range(PLAYERS)]
player = 1
for i in range(1,TOPSTONE+1):
    if i % (TOPSTONE/100) == 0 :
        print i
    current = place(player,i,current)
    # mprint(player)
    player = 0 if player==PLAYERS-1 else player+1

print players
print "top score = ", max(players)

