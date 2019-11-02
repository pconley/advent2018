import copy, sys

def generic(reg,c,result):
    out = copy.deepcopy(reg)
    out[c] = result
    return out

# Addition:
# addr (add register) stores into register C the result of adding register A and register B.
def addr(reg,a,b,c):
    return generic(reg,c,reg[a]+reg[b])
# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(reg,a,b,c):
    return generic(reg,c,reg[a]+b)

# Multiplication:
# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(reg,a,b,c):
    return generic(reg,c,reg[a]*reg[b])
# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(reg,a,b,c):
    return generic(reg,c,reg[a]*b)

# Bitwise AND:
# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(reg,a,b,c):
    return generic(reg,c,reg[a]&reg[b])
# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(reg,a,b,c):
    return generic(reg,c,reg[a]&b)

# Bitwise OR:
# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(reg,a,b,c):
    return generic(reg,c,reg[a]|reg[b])
# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(reg,a,b,c):
    return generic(reg,c,reg[a]|b)

# Assignment:
# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(reg,a,b,c):
    return generic(reg,c,reg[a])
# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(reg,a,b,c):
    return generic(reg,c,a)

# Greater-than testing:
# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(reg,a,b,c):
    return generic(reg,c,1 if a>reg[b] else 0)
# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(reg,a,b,c):
    return generic(reg,c,1 if reg[a]>b else 0)
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(reg,a,b,c):
    return generic(reg,c,1 if reg[a]>reg[b] else 0)

# Equality testing:
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(reg,a,b,c):
    return generic(reg,c,1 if a==reg[b] else 0)
# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(reg,a,b,c):
    return generic(reg,c,1 if reg[a]==b else 0)
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(reg,a,b,c):
    return generic(reg,c,1 if reg[a]==reg[b] else 0)

def test(func,start,expect,opcode,a,b,c):
    finish = func(start,a,b,c)
    match = "a match" if expect==finish else ""
    # print("as",func.__name__,[a,b,c],":",start,"=>",finish,"    ",expect,match)
    return 1 if expect==finish else 0

functions = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

start = [3, 2, 1, 1]
after = [3, 2, 2, 1]

print("command:","9 2 1 2")
matches = 0
for func in functions:  
    matches += test(func,start,after,9,2,1,2)
print("matches = ",matches)
# exit()

print ('Argument List:', str(sys.argv))
data_file = open(sys.argv[1],"r+")  
lines = data_file.readlines()

triples = []
n = 0
while n < len(lines) :
    before = [int(x) for x in lines[n].strip()[9:19].split(", ")]
    command = [int(x) for x in lines[n+1].strip().split(" ")]
    after = [int(x) for x in lines[n+2].strip()[9:19].split(", ")]
    triples.append((command,before,after))
    n += 4

codes = {}

while len(functions) > 0:
    temp = copy.deepcopy(triples)
    s = 0
    for (command,before,after) in temp :
        s += 1
        # print(before,command,after)
        matches = 0
        last_match = None
        for func in functions:  
            m = test(func,before,after,*command)
            if m == 1 : last_match = func
            matches += m
        # print(s, "sample has function matches=",matches)
        if matches == 1 : 
            # print(s,"of",len(temp),(command,before,after),"sample has a singular match",command[0],last_match.__name__)
            # triples.remove((command,before,after))
            codes[command[0]] = last_match
            to_remove = last_match
            break
    # print("remove",to_remove.__name__)
    functions.remove(to_remove)
    # input(str(len(functions))+" Continue?")

i = 0
for code in codes : 
    print(i,code,":",codes[code].__name__)
    i += 1

# exit()

pgm_file = open("p16pgm","r+")  
lines = pgm_file.readlines()
print("\nstart execution")
registers = [0,0,0,0]
k = 0
print(registers)
for line in lines : 
    (opcode,a,b,c) = [ int(x) for x in line.strip().split()]
    registers = codes[opcode](registers,a,b,c)
    print(k,"of",len(lines),opcode,codes[opcode].__name__,":",a,b,c,">>",registers[0],"line=",k)
    if k%100 == 0 : 
        input("Continue?")
    k += 1

