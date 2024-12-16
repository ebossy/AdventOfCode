#part the map and the sequence
with open("15-1.txt", "r") as file:  # Encoding anpassen, falls nötig
    m, s = file.read().split("\n\n")
m = [[j for j in i] for i in m.split("\n")]

#finds bot
def find_robo():
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == "@":
                return i, j

#rekurisve function for movement
def movement(ri, rj, y, x, symbol = "@"):
    ni = ri + y
    nj = rj + x
    if m[ni][nj] == "#":
        return ri, rj
    if m[ni][nj] == "O":
        movement(ni, nj, y, x, "O")
    #chekcs if theres a . after moving other blocks
    if m[ni][nj] == ".":
        m[ni][nj] = symbol
        m[ri][rj] = "."
        return ni, nj
    return ri, rj





ri, rj = find_robo()
for seq in s:
    if seq == "^":
        ri, rj = movement(ri, rj, -1, 0)
    elif seq == "v":
        ri, rj = movement(ri, rj, 1, 0)
    elif seq == ">":
        ri, rj = movement(ri, rj, 0, 1)
    elif seq == "<":
        ri, rj = movement(ri, rj, 0, -1)




summary = 0
for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] == "O":
            summary += 100*i+j
print(summary)