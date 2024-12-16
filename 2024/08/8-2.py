#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Baut auf 01 auf unterschiede kommentiert
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
ant_map = []
with open("8-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        tmp=[]
        line = line.strip()
        for letter in line:
            tmp.append(letter)
        ant_map.append(tmp)

valsWpos = {}
summary = 0
for i in range(len(ant_map)):
    for j in range(len(ant_map[i])):
        if ant_map[i][j] != ".":
            if ant_map[i][j] not in valsWpos:
                valsWpos[ant_map[i][j]]=[]
            valsWpos[ant_map[i][j]].append((i, j))
            ant_map[i][j] = "#"    # Die Türme selber haben jetzt auch ein Signal
            summary += 1           #Deshalb +01 signal


def tuple_sub(t1,t2):
    return tuple(a - b for a, b in zip(t1, t2))
def tuple_add(t1,t2):
    return tuple(a + b for a, b in zip(t1, t2))
def in_range(t):
    i, j = t[0], t[1]
    h = len(ant_map[0])
    v = len(ant_map)
    if i < 0 or i >= v or j < 0 or j >= h:
        return False
    else:
        return True



for key in valsWpos:
    for i in range(len(valsWpos[key])-1):
        for second in valsWpos[key][i+1:]:
            first = valsWpos[key][i]
            dif = tuple_sub(first, second)
            first = tuple_add(first, dif)
            second = tuple_sub(second, dif)

            while in_range(first):#aus einer if jetzt eine while
                if ant_map[first[0]][first[1]] != "#":#prüfung ob signal bereits vorhanden
                    summary += 1
                    ant_map[first[0]][first[1]] = "#"
                first = tuple_add(first, dif)#Koordinaten updaten

            while in_range(second):#""
                if ant_map[second[0]][second[1]] != "#":
                    summary += 1
                    ant_map[second[0]][second[1]] = "#"
                second = tuple_sub(second, dif)

print(valsWpos)
for line in ant_map:
    print(line)
print(summary)