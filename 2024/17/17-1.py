import re
# part the Registers and the sequence
with open("17-1.txt", "r") as file:
    m, s = file.read().split("\n\n")
A, B, C = re.findall(r"(\d+)", m)
s = [i for i in re.findall(r"(\d+)", s)]

instr_p = 0 #default +2


def adv0():
