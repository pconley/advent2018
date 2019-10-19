
def power_level(x, y, serial):
    # print("\n",x, y, serial)
    rack_id = x + 10
    level = y * rack_id
    level += serial
    level *= rack_id
    # print("level = {}".format(level))
    text = str(100000000+level)
    # print(text)
    digit = text[-3:-2]
    result = int(digit)-5
    # print("result = ", result)
    return result

assert( power_level(3,5,8) == 4 )

# Fuel cell at  122,79, grid serial number 57: power level -5.
# Fuel cell at 217,196, grid serial number 39: power level  0.
# Fuel cell at 101,153, grid serial number 71: power level  4.

assert( power_level(122,79,57) == -5 )
assert( power_level(217,196,39) == 0 )
assert( power_level(101,153,71) == 4 )

def printer(matrix, r_start, r_end, c_start, c_end):
    for i in range(r_start, r_end):
        print("{0:5d}: ".format(i+1), "".join(["{0:4d}".format(x) for x in matrix[i][c_start:c_end]]))

def val(r, c):
    global matrix
    # does the index conversion
    return matrix[r-1][c-1]

def col(c, rng):
    global matrix
    return [ val(i,c) for i in rng ]

def row(r, rng):
    global matrix
    return [ val(r,i) for i in rng ]

def create(size, serial):
    matrix = [ [0 for col in range(size)] for rol in range(size) ]
    for i in range(size):
        for j in range(size):
            matrix[i][j] = power_level(i+1,j+1,serial)
    return matrix



def calc(i, j, n):
    global matrix, solutions

    if (i,j,n) in solutions: return solutions[(i,j,n)]

    # calculate the value of the area at i,j of size n
    if n == 1 :
        # gotta stop the recursion
        result = val(i,j)
    else :
        c = j+n-1 # the extra col
        r = i+n-1 # the extra row
        result = calc(i,j,n-1) + sum(row(r,range(j,c))) + sum(col(c,range(i,r))) + val(r,c)
        solutions[(i,j,n)] = result # save this result to use later
    # print("calc: {},{} for {} ==> {}".format(i,j,n,result))
    return result

SIZE = 300

def search(n):
    pmax = -10000000
    save_i = save_j = 0
    for i in range(1,SIZE-n-1):
        # print("     size=",n,"for row =",i,"of",SIZE-n-1, pmax)
        for j in range(1,SIZE-n-1):
            p = calc(i,j,n)
            if p > pmax :
                save_i = i
                save_j = j
                pmax = p
    return (pmax, save_i, save_j)

def scan():
    # do a search for all sizes
    pmax = -10000000
    save_n = save_i = save_j = 0
    for n in range(1,SIZE):
        print("search for size = ", n, "of", SIZE)
        (p, i, j) = search(n)
        print("size = ", n, i, j, "p=", p, "pmax=",pmax)
        if p > pmax :
            save_n = n
            save_i = i
            save_j = j
            pmax = p
    return (pmax, save_i, save_j, save_n)

def ctest(c,n,m):
    total = sum(col(c, range(n,m+1)))
    # print("sum of {} column {}:{} == {}".format(c,n,m,total))
    return total

def rtest(r,n,m):
    total = sum(row(r, range(n,m+1)))
    # print("sum of {} row {}:{} == {}".format(r,n,m,total))
    return total

def atest(i,j,n):
    total = calc(i,j,n)
    print("calc of {},{} for {} == {}".format(i,j,n,total))
    return total


# matrix = create(size=SIZE, serial=42)
# solutions = {}
# printer(matrix, 0, 20, 0, 20) 
# assert(-5  == ctest(5,2,4)) 
# assert(-5  == rtest(5,2,5))
# assert(-20 == atest(2,3,3))



# For grid serial number 18, the largest total 3x3 square has a top-left 
# corner of 33,45 (with a total power of 29)

# matrix = create(size=SIZE, serial=18)
# solutions = {}
# result = search(3)
# assert(result == (29,33,45))



# For grid serial number 18, the largest total square (with a total 
# power of 113) is 16x16 and has a top-left corner of 90,269, so 
# its identifier is 90,269,16.

# matrix = create(size=SIZE, serial=18)
# solutions = {}
# result = scan()
# print(result)
# assert( result == (113, 90, 269, 16))



# For grid serial number 42, the largest total square (with a total 
# power of 119) is 12x12 and has a top-left corner of 232,251, so its 
# identifier is 232,251,12.

# matrix = create(size=SIZE, serial=42)
# solutions = {}
# atest(232,251,12)
# printer(matrix, 230, 240, 250, 260) 
# result = scan()
# print("scan result = ", result)
# assert(result == (119,232,251,12))



# Now the real problem

matrix = create(size=SIZE, serial=8141)
solutions = {}
printer(matrix, 230, 240, 250, 260) 
result = scan()
print("scan result = ", result)
