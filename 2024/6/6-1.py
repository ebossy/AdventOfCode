guard_map = []
with open("6-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        tmp = []
        for sym in line:
            tmp.append(sym)
        guard_map.append(tmp)

class Guard:
    def __init__(self):
        for i in range(len(guard_map)):
            for j in range(len(guard_map[0])):
                if guard_map[i][j] == "^":
                    self.pos = (i, j)
        self.dir = (-1, 0)

#Walk till out of map and mark every step
def walk_till():
    visitedlist = set()
    visitedlist.add(guard.pos)

    while True:
        yn, xn = guard.pos[0] + guard.dir[0], guard.pos[1] + guard.dir[1]
        if guard_map[yn][xn] == "#":
            if guard.dir == (-1, 0): guard.dir = (0, 1)
            elif guard.dir == (0, 1): guard.dir = (1, 0)
            elif guard.dir == (1, 0): guard.dir = (0, -1)
            elif guard.dir == (0, -1): guard.dir = (-1, 0)
            continue
        elif guard_map[yn][xn] == ".":
            visitedlist.add((yn, xn))
        if len(guard_map[0])-1 == xn or xn == 0 or len(guard_map)-1 == yn or yn == 0:
            return len(visitedlist)
        guard.pos = (yn, xn)


guard = Guard()
print(walk_till())
