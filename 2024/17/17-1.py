import re
# part the Registers and the sequence
with open("17-1.txt", "r") as file:
    m, s = file.read().split("\n\n")
A, B, C = re.findall(r"(\d+)", m)
s = [int(i) for i in re.findall(r"(\d+)", s)]
reg = {"A": int(A), "B": int(B), "C": int(C)}
print(reg, s)
out = ""

instr_p = 0 #default +2

def get_combo(op):
    if op in [0, 1, 2, 3]:
        return op
    if op == 4:
        return reg["A"]
    if op == 5:
        return reg["B"]
    if op == 6:
        return reg["C"]
    if op == 7:
        print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")

def get_literal(op):
    return op

def adv0(op):
    op = get_combo(op)
    reg["A"] = reg["A"]//(2**op)

def bxl1(op):
    op = get_literal(op)
    reg["B"] = reg["B"]^op

def bst2(op):
    op = get_combo(op)
    reg["B"]=op%8

def jnz3(op):
    return get_literal(op)

def bxc4(op):
    reg["B"] = reg["B"]^reg["C"]

def out5(op):
    return str(get_combo(op)%8)

def bdv6(op):
    op = get_combo(op)
    reg["B"] = reg["A"] // (2 ** op)

def cdv7(op):
    op = get_combo(op)
    reg["C"] = reg["A"] // (2 ** op)

while instr_p < len(s)-1:
    if s[instr_p] == 0:
        adv0(s[instr_p+1])

    elif s[instr_p] == 1:
        bxl1(s[instr_p+1])

    elif s[instr_p] == 2:
        bst2(s[instr_p+1])

    elif s[instr_p] == 3:
        if reg["A"] > 0:
            instr_p = jnz3(s[instr_p+1])-2

    elif s[instr_p] == 4:
        bxc4(s[instr_p+1])

    elif s[instr_p] == 5:
        out += ","
        out += out5(s[instr_p+1])


    elif s[instr_p] == 6:
        bdv6(s[instr_p+1])

    elif s[instr_p] == 7:
        cdv7(s[instr_p+1])
    instr_p += 2

print(out[1:])