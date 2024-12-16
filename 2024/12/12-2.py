from stringprep import in_table_c21

fencemap = []
with open("12-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        tmp = []
        for char in line.strip():
            tmp.append(char)
        fencemap.append(tmp)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

already_visited = set()
areas = []
fence_and_size = []

#finds an area
def find_area(i, j, c, area):
    already_visited.add((i, j))
    area.append((i, j))
    for direction in directions:
        ix, jx = i + direction[0], j + direction[1]
        if 0 <= ix < len(fencemap) and 0 <= jx < len(fencemap[0]) and fencemap[ix][jx] == c and (ix, jx) not in already_visited:
            find_area(ix, jx, c, area)

#delete all neighbours(only 1 fence)
def check_neighbors(pos, di, neigh):
    it = (pos[0] , pos[1])
    while True:
        it = (di[0] + it[0], di[1] + it[1])
        if it in neigh:
            neigh.remove(it)
        else:
            break
    it = (pos[0] , pos[1])
    while True:
        it = (it[0] - di[0], it[1] - di[1])
        if it in neigh:
            neigh.remove(it)
        else:
            break

#find all areas
for i in range(len(fencemap)):
    for j in range(len(fencemap[0])):
        if (i, j) not in already_visited:
            tmp = []
            find_area(i, j, fencemap[i][j], tmp)
            areas.append(tmp)


#count the fences and their position for each direction they face
for area in areas:
    fence_pos = {}
    for direction in directions:
        fence_pos[direction] = []
    for are in area:
        for direction in directions:
            x, y = are[0] + direction[0], are[1] + direction[1]
            if (x, y) not in area:
                fence_pos[direction].append((x, y))
    #remove all unnecessary fences
    for cord in fence_pos[(-1, 0)]:#up
        check_neighbors(cord, (0, 1), fence_pos[(-1, 0)])
    for cord in fence_pos[(1, 0)]:#down
        check_neighbors(cord, (0, 1), fence_pos[(1, 0)])
    for cord in fence_pos[(0, 1)]:#right
        check_neighbors(cord, (1, 0), fence_pos[(0, 1)])
    for cord in fence_pos[(0, -1)]:#left
        check_neighbors(cord, (1, 0), fence_pos[(0, -1)])

    #count'em and add to fence and size
    fences = 0
    for side in fence_pos:
        fences += len(fence_pos[side])
    fence_and_size.append((fences, len(area)))

#sums up the formula
summary = 0
for t in fence_and_size:
    check = t[1] * t[0]
    summary += check

print(summary)
