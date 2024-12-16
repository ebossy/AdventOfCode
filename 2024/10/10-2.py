hike_map = []
with open("10-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        tmp = []
        for num in line.strip():
            tmp.append(int(num))
        hike_map.append(tmp)

for line in hike_map:
    print(line)



def get_score(i, j, height):
    if height == 9 and (i,j):
        return 1
    summary = 0
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]#up, down, right, left
    for move in directions:
        ix , jx = i + move[0], j + move[1]
        if 0 <= ix < len(hike_map) and 0 <= jx< len(hike_map[0]):
            if hike_map[ix][jx] == height+1:
                summary+=get_score(ix, jx, height+1)

    if(height==0):
        print(summary)
    return summary


summary = 0
for i in range(len(hike_map)):
    for j in range(len(hike_map[0])):
        if hike_map[i][j] == 0:
            summary += get_score(i,j, 0)
print(summary)