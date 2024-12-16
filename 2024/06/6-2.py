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


def walk_till(map):
    guard = Guard()
    q = 0
    while True:
        q += 1
        if q > 20000: return True
        yn, xn = guard.pos[0] + guard.dir[0], guard.pos[1] + guard.dir[1]
        if map[yn][xn] == "#":
            if guard.dir == (-1, 0): guard.dir = (0, 1)
            elif guard.dir == (0, 1): guard.dir = (1, 0)
            elif guard.dir == (1, 0): guard.dir = (0, -1)
            elif guard.dir == (0, -1): guard.dir = (-1, 0)
            continue
        if len(map[0])-1 == xn or xn == 0 or len(map)-1 == yn or yn == 0:
            return False
        guard.pos = (yn, xn)



#adding a objekt in every possible location and try if its looped
summary = 0
for i in range(len(guard_map)):
    for j in range(len(guard_map[0])):
        if "#" != guard_map[i][j] != "^":
            tmp_map = []
            for k in guard_map:
                tmp=[]
                for l in k:
                    tmp.append(l)
                tmp_map.append(tmp)

            tmp_map[i][j] = "#"
            if walk_till(tmp_map):
                summary += 1
print(summary)