words = []
with open("4-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for zeile in datei:
        tmp = []
        for buchstabe in zeile.strip():
            tmp.append(buchstabe)
        words.append(tmp)


def findx(i, j):
    direction = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    if i == len(words) - 1:
        return False
    if j == len(words[0]) - 1:
        return False
    if i == 0:
        return False
    if j == 0:
        return False

    if words[i + direction[0][0]][j + direction[0][1]] in ("M", "S"):
        if words[i + direction[1][0]][j + direction[1][1]] in ("M", "S"):
            if words[i + direction[0][0]][j + direction[0][1]] != words[i + direction[1][0]][j + direction[1][1]]:
                if words[i + direction[2][0]][j + direction[2][1]] in ("M", "S"):
                    if words[i + direction[3][0]][j + direction[3][1]] in ("M", "S"):
                        if words[i + direction[2][0]][j + direction[2][1]] != words[i + direction[3][0]][
                            j + direction[3][1]]:
                            return True
    return False

#Searching for A and check corners if valid
summary = 0
for i in range(len(words)):
    for j in range(len(words[0])):
        if words[i][j] == "A":
            if findx(i, j):
                summary += 1
print(summary)