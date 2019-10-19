

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
        print("{0:5d}: ".format(i), "".join(["{0:4d}".format(x) for x in matrix[i][c_start:c_end]]))

SIZE = 300

def main(serial):
    print("serial=",serial)
    matrix = [ [0 for col in range(SIZE)] for rol in range(SIZE) ]
    for i in range(SIZE):
        for j in range(SIZE):
            matrix[i][j] = power_level(i+1,j+1,serial)

    printer(matrix, 0, 20, 0, 20)

    max = 0
    for r in range(SIZE-2):
        for c in range(SIZE-2):
            total = sum([ sum(row[c:c+3]) for row in matrix[r:r+3]])
            if r<5 and c<5 :
                print(format("{},{} : {}".format(r, c, total)))
            if total > max : 
                max = total
                save_r = r
                save_c = c
    print("max = ", max, save_r, save_c)
    return (max, save_r+1, save_c+1)

# For grid serial number 18, the largest total 3x3 square 
# has a top-left corner of 33,45 (with a total power of 29

assert(main(18) == (29,33,45))

# For grid serial number 42, the largest 3x3 square's top-left
# is 21,61 (with a total power of 30); 

assert(main(42) == (30,21,61))

print(main(8141))


