fencemap = []
with open("12-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        tmp = []
        for char in line.strip():
            tmp.append(char)
        fencemap.append(tmp)

directions = [(1, 0), (-1, 0), (0, 1), (0, -1) ]

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


for i in range(len(fencemap)):
    for j in range(len(fencemap[0])):
        if (i, j) not in already_visited:
            tmp = []
            find_area(i, j, fencemap[i][j], tmp)
            areas.append(tmp)

#counts the fences
for area in areas:
    fences = 0
    for are in area:
        for direction in directions:
            x, y = are[0] + direction[0], are[1] + direction[1]
            if (x, y) not in area:
                fences += 1
    fence_and_size.append((fences, len(area)))

#sums up the formula
summary = 0
for t in fence_and_size:
    check = t[1] * t[0]
    summary += check

print(summary)
