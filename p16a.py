import copy

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

# def equal(rs1,rs2):
#     for i in range(len(rs1)) : 
#         if rs1[i] != rs2[i] : 
#             return False
#     return True

def test(func,start,expect,opcode,a,b,c):
    finish = func(start,a,b,c)
    match = "a match" if expect==finish else ""
    print("as",func.__name__,[a,b,c],":",start,"=>",finish,"    ",expect,match)
    return expect==finish

functions = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]

start = [3, 2, 1, 1]
after = [3, 2, 2, 1]

print("command:","9 2 1 2")
for func in functions:  
    test(func,start,after,9,2,1,2)
