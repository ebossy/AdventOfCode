#Idee:
#       Pfade immer speichern und bei erfolgsfall nochmal separate speichern
#       auch gleiche Fälle Berücksichtigen (Teil 1 wurde abgebrochen, wenn score gleich war)

#map
with open("16-1.txt", "r") as file:  # Encoding anpassen, falls nötig
    m = [[j for j in i] for i in file.read().strip().split("\n")]

#Tuple class um zu drehen und koordinaten zu ändern
class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot_r(self):
        x, y = self
        return T((y, -x))
    def rot_l(self):
        x, y = self
        return T((-y, x))

#findet den startknoten
def find_s():
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 'S':
                return T((i, j))

#alle möglichen scores
wins = []
#alle besuchten koordinaten mit dem aktuellen score um unnötige wege zu vermeiden
visited = {}
#alle positionen für alle scores
best_path = {}
def walk_straight(direction, pos, cur_score, path):#neuer parameter path um pfade zu trennen
    #gerade aus laufen bis eine Wand kommt
    while m[pos[0]][pos[1]] != "#" :
        path.add(pos)#pfad hinzufügen
        #Falls der Pfad bereits besucht wurde mit einem besseren score pfad ignorieren
        if pos in visited and cur_score > visited[pos]:#aus größer gleich größer damit auch mehrere gleich gute ergebnisse gezeigt werden
            return
        visited[pos] = cur_score

        #Prüfen ob rechts ein möglicher pfad ist und rekursiv aufrufen
        possible_path = direction.rot_r()
        new_pos = pos + possible_path
        if m[new_pos[0]][new_pos[1]] == ".":
            visited[pos] = cur_score+1000 # muss verändert werden, da man sich dreht
            walk_straight(possible_path, new_pos, cur_score+1001, path.copy()) #+1001 weil 100 für die drehung und 1 schritt in die richtung

        # Prüfen ob links ein möglicher pfad ist und rekursiv aufrufen
        possible_path = direction.rot_l()
        new_pos = pos + possible_path
        if m[new_pos[0]][new_pos[1]] == ".":
            visited[pos] = cur_score + 1000 # muss verändert werden, da man sich dreht
            walk_straight(possible_path, new_pos, cur_score + 1001, path.copy()) #+1001 weil 100 für die drehung und 1 schritt in die richtung

        #weiter gehen
        pos = pos + direction
        cur_score += 1
        #Falls Ziel gefunden Score speichern
        if m[pos[0]][pos[1]] == "E":
            wins.append(cur_score)
            #pfade hinzufügen
            if cur_score not in best_path:
                best_path[cur_score] = path
                best_path[cur_score].add(pos)
            else:
                best_path[cur_score].update(path)
            return







walk_straight(T((0,1)), find_s(), 0, set())
best_score = min(wins)
print(best_score)

print(len(best_path[best_score]))
