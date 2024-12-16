#part map and sequence
with open("15-1.txt", "r") as file:  # Encoding anpassen, falls nötig
    m, s = file.read().split("\n\n")
mt = [[j for j in i] for i in m.split("\n")]

m = []
#make the map wider
for i in range(len(mt)):
    tmp = []
    for j in range(len(mt[0])):
        if mt[i][j] == "@":
            tmp.append("@")
            tmp.append(".")
        elif mt[i][j] == ".":
            tmp.append(".")
            tmp.append(".")
        elif mt[i][j] == "#":
            tmp.append("#")
            tmp.append("#")
        elif mt[i][j] == "O":
            tmp.append("[")
            tmp.append("]")
        j += 1
    m.append(tmp)

#finds bot
def find_robo():
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "@":
                return i, j

#movement logic for horizontal (doesnt change much from p1)
def movement_lr(ri, rj, y, x, symbol = "@"):
    ni = ri + y
    nj = rj + x
    if m[ni][nj] == "#":
        return
    if m[ni][nj] in ["[", "]"]:
        movement_lr(ni, nj, y, x, m[ni][nj])
    if m[ni][nj] == ".":
        m[ni][nj] = symbol
        m[ri][rj] = "."




#vertically movement(only for bot)
def movement_u(ri, rj, y, x, symbol = "@"):
    ni = ri + y
    nj = rj + x
    if m[ni][nj] == "#":
        return
    if m[ni][nj] in ["[", "]"]:
        movement_box(ni, nj, y, x, m[ni][nj])
    if m[ni][nj] == ".":
        m[ni][nj] = symbol
        m[ri][rj] = "."


#rekursive function to move boxes
def movement_box(ri, rj, y, x, symbol = "["):
    ni = ri + y
    nj = rj + x
    if symbol == "[":
        nj2 = nj + 1
        rj2 = rj + 1
        symbol2 = "]"
    else:
        rj2 = rj - 1
        nj2 = nj - 1
        symbol2 = "["
    if m[ni][nj] == "#" or m[ni][nj2] == "#":
        return
    if m[ni][nj] in ["[", "]"]:
        movement_box(ni, nj, y, x, m[ni][nj])
    if m[ni][nj2] in ["[", "]"]:
        movement_box(ni, nj2, y, x, m[ni][nj2])
    if m[ni][nj] == "." and m[ni][nj2] == ".":
        m[ni][nj] = symbol
        m[ri][rj] = "."
        m[ni][nj2] = symbol2
        m[ri][rj2] = "."




#make a deep copy of the map and if the position of the bot didnt change load the backup because some boxes could have moved
import copy
ri, rj = find_robo()
for seq in s:
    backup = copy.deepcopy(m)

    ri, rj = find_robo()
    if seq == "^":
        movement_u(ri, rj, -1, 0)
    elif seq == "v":
        movement_u(ri, rj, 1, 0)
    elif seq == ">":
        movement_lr(ri, rj, 0, 1)
    elif seq == "<":
        movement_lr(ri, rj, 0, -1)

    if (ri, rj) == find_robo():
        m = copy.deepcopy(backup)








summary = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "[":
            summary += 100*i+j
for line in m:
    print(line)
print(summary)

