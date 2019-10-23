
def as_str(i, positions, recipes):
    text = "{:5d}: ".format(i)
    for r in range(len(recipes)) :
        if r == positions[0] :
            t = "({}) ".format(recipes[r])
        elif r == positions[1] :
            t = "[{}] ".format(recipes[r])
        else :
            t = " {}  ".format(recipes[r])
        text += t
    return text

def generate(positions, recipes):
    total = recipes[positions[0]] + recipes[positions[1]]
    # print("total = ", total)
    text = str(total)
    for c in text :
        recipes.append(int(c))
    # return number created
    return len(c)

def shift(positions,recipes):
    for p in range(len(positions)):
        pos = positions[p]
        # print("recipes = ",recipes)
        advance = 1 + recipes[pos]
        positions[p] = (positions[p]+advance)%len(recipes) 

def rstr(arr):
    return "".join([str(x) for x in arr])

def process(target):
    recipes   = [3,7]
    positions = [0,1]
    i = -1
    while i < 1000000000 :
        generate(positions, recipes)
        shift(positions, recipes)
        # print(as_str(i, positions, recipes))
        candidate = rstr(recipes[i:i+len(target)])
        if candidate == target :
            print(i, "found", target)
            return i
        if i%10000 : print(".", )
        # print(i, rstr(recipes[0:i]), candidate)
        i += 1
    return 0

assert( 5     == process("01245"))
assert( 9     == process("51589"))
assert( 18    == process("92510"))
assert( 2018  == process("59414"))

print(process("084601"))
