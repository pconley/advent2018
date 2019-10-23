
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

def shift(positions,recipes):
    for p in range(len(positions)):
        pos = positions[p]
        # print("recipes = ",recipes)
        advance = 1 + recipes[pos]
        positions[p] = (positions[p]+advance)%len(recipes) 

def process(target):

    recipes   = [3,7]
    positions = [0,1]
    i = 0
    while len(recipes) < target + 10 :
        # print(as_str(i, positions, recipes))
        generate(positions, recipes)
        shift(positions, recipes)
        i += 1
    # print(as_str(i, positions, recipes))
    # cannot just pull the last 10 as two may have been added
    text = "".join([str(x) for x in recipes[target:target+10]])
    print(text)
    return text

assert(process(9)    == "5158916779")
assert(process(5)    == "0124515891")
assert(process(18)   == "9251071085")
assert(process(2018) == "5941429882")

process(84601)
