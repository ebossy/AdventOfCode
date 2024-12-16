import re
claw_machines = []
#putting the machines in a list each machine is a dict with A B und Prize
with open("13-1.txt", "r") as f:
    claw_machine = {}
    i = 0
    for line in f:
        line = line.strip()
        if i == 0:
            x, y = re.findall(r"[0-9]+", line)
            claw_machine["A"] = (int(x), int(y))
            i += 1
        elif i == 1:
            x, y = re.findall(r"[0-9]+", line)
            claw_machine["B"] = (int(x), int(y))
            i += 1
        elif i == 2:
            x, y = re.findall(r"[0-9]+", line)
            claw_machine["Prize"] = (int(x), int(y))
            i += 1
        elif i == 3:
            claw_machines.append(claw_machine)
            claw_machine = {}
            i = 0

#some Methods for Tuples
def tuple_sub(t1,t2):
    return tuple(a - b for a, b in zip(t1, t2))
def tuple_add(t1,t2):
    return tuple(a + b for a, b in zip(t1, t2))
def tuple_mul(t1,t2):
    return tuple(a*b for a, b in zip(t1, t2))
def tuple_div(t1,t2):
    return tuple(a/b for a, b in zip(t1, t2))
def tuple_mod(t1,t2):
    return tuple(a%b for a, b in zip(t1, t2))


def b_is_enough(claw_machine, cur):
    rest = tuple_sub(claw_machine["Prize"] ,cur)
    tmp = tuple_mod(rest, claw_machine["B"])
    tmp2 = tuple_div(rest, claw_machine["B"])
    #if rest is partable of B and its the same number (you cant press the x coordinate different often then y one)
    if tmp == (0, 0) and tmp2[0] == tmp2[1]:
        return True
    else:
        return False

tokens = 0
#Press A until only B is required
for claw_machine in claw_machines:
    start = (0, 0)
    token = 0
    while not b_is_enough(claw_machine, start):
        if start == claw_machine["Prize"]:
            token +=3
            tokens =+ token
        if start[0] >= claw_machine["Prize"][0] or start[1] >= claw_machine["Prize"][1]:
            break
        token += 3
        start = tuple_add(start, claw_machine["A"])
    if b_is_enough(claw_machine, start):
        rest = tuple_sub(claw_machine["Prize"], start)
        print(tuple_div(rest, claw_machine["B"]))
        token += tuple_div(rest, claw_machine["B"])[0]
        print(token)
        tokens += token
print(tokens)



