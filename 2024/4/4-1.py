words = []
with open("4-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for zeile in datei:
        tmp = []
        for buchstabe in zeile.strip():
            tmp.append(buchstabe)
        words.append(tmp)


def findline(x, i, j, direc):
    if len(x) == 0:
        return True
    if i > len(words) - 1:
        return False
    if j > len(words[0]) - 1:
        return False
    if i < 0:
        return False
    if j < 0:
        return False
    if x[0] == words[i][j]:
        x.pop(0)
        return findline(x, i + direc[0], j + direc[1], direc)
    return False


def findletter(i, j):
    tmp = 0
    direction = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    for direc in direction:
        if findline(["M", "A", "S"], i + direc[0], j + direc[1], direc):
            tmp += 1
    return tmp

#searching for X and look in every direction if there is MAS
summary = 0
for i in range(len(words)):
    for j in range(len(words[0])):
        if words[i][j] == "X":
            summary += findletter(i, j)
print(summary)
