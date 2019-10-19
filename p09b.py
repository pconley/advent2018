import sys

players = []
marbles = []
current = 0
played = 0

def fmt(idx,m):
    f = "({})" if idx == current else " {} "
    b = "T" if m else "F"
    return f.format(m)

def mprint(p):
    global marbles
    text = str(p)+": "
    pos = 0
    for i in range(len(marbles)):
        (l,r,val) = marbles[pos]
        text += " "+fmt(pos,val)
        pos = r
    print text

def place(player, val, current):
    global marbles, players
    if val % 23 == 0:
        # the current player keeps the marble they would have placed, 
        # adding it to their score. In addition, the marble 7 marbles 
        # counter-clockwise from the current marble is removed from 
        # the circle and also added to the current player's score.
        pos = get_anticlock(current,7)
        # print "special=",marbles[pos]
        (l, r, v) = marbles[pos]
        players[player] += val + v
        # reconnect the left and right
        # print "left", marbles[l]
        (ll, lr, lv) = marbles[l]
        # print "right", marbles[r]
        (rl, rr, rv) = marbles[r]
        marbles[l] = (ll, r, lv)
        # print "Left", marbles[l]
        marbles[r] = (l, rr, rv)
        # print "Right", marbles[r]
        return r
    else:
        # get marble that is one clockwise
        pos = get_clockwise(current,1)
        # print "current", current, "val", val, " >> pos", pos
        # chain looks like: current <> pos <> z
        (c,z,v) = marbles[pos]
        # place a marble in linked list such that
        # new chain: current <> pos <> new <> z
        marbles.append((pos,z,val)) # new one
        index_of_new = len(marbles)-1
        # print "val = ", val, "at", index_of_new
        marbles[pos] = (c,index_of_new,v)
        (z_left,z_right,z_value) = marbles[z]
        marbles[z] = (index_of_new, z_right, z_value)
        return index_of_new # now current

def get_clockwise(n,m):
    # m clockwise of n
    # after the marble that is 1 marble clockwise
    # return position of m-th clockwise marble
    pos = n
    for i in range(m):
        (left,pos,_) = marbles[pos]
    return pos

def get_anticlock(n,m):
    pos = n
    for i in range(m):
        (pos,right,_) = marbles[pos]
    return pos

def main(pcnt, mcnt):
    pcnt = int(pcnt)
    mcnt = int(mcnt)
    print "stones =", mcnt, "players =", pcnt
    global players, marbles, current, played
    marbles = []
    players = [0 for i in range(pcnt+1)]

    # first placement
    marbles.append((0,0,0)) # left, right, value
    played = 1

    # print "current", current, "played", played
    # mprint(0)

    player = 1
    for i in range(1,mcnt+1):
        current = place(player,i,current)
        played = i+1
        # print "current", current, "played", played
        # mprint(player)
        player = 1 if player==pcnt else player+1

    print players
    print "top score = ", max(players)

print ('Argument List:', str(sys.argv))

main(sys.argv[1], sys.argv[2])
