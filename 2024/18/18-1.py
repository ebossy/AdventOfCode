import re
import sys

sys.setrecursionlimit(100000)


m = []
width = 71
height = 71
first_x_byte = 1024
for i in range(height):
    tmp = []
    for j in range(width):
        tmp.append(".")
    m.append(tmp)
m[height - 1][width - 1] = "S"


# Tuple class um koordinaten zu ändern
class T(tuple):
    def __add__(self, other):
        return T(x + y for x, y in zip(self, other))

    def rot_r(self):
        x, y = self
        return T((y, -x))

    def rot_l(self):
        x, y = self
        return T((-y, x))


start = T((0, 0))
falling_byte = []
# part the Registers and the sequence
with open("18-1.txt", "r") as file:
    for line in file.read().split("\n"):
        x, y = re.findall(r"(-?\d+)", line)
        x, y = int(x), int(y)
        falling_byte.append(T((y, x)))

for i in range(first_x_byte):
    m[falling_byte[i][0]][falling_byte[i][1]] = "#"
for line in m:
    print(line)


def in_range(t):
    if 0 <= t[0] < height and 0 <= t[1] < width:
        return True
    else:
        return False


# alle möglichen scores
wins = []
# alle besuchten koordinaten mit dem aktuellen score um unnötige wege zu vermeiden
visited = {}


def walk_straight(direction, pos, cur_score):
    # gerade aus laufen bis eine Wand kommt
    while in_range(pos) and m[pos[0]][pos[1]] != "#":
        # Falls der Pfad bereits besucht wurde mit einem besseren score pfad ignorieren
        if pos in visited and cur_score >= visited[pos]:
            return
        visited[pos] = cur_score

        # Prüfen ob rechts ein möglicher pfad ist und rekursiv aufrufen
        possible_path = direction.rot_r()
        new_pos = pos + possible_path
        if in_range(new_pos) and m[new_pos[0]][new_pos[1]] == ".":
            walk_straight(possible_path, new_pos,
                          cur_score + 1)  #+1001 weil 100 für die drehung und 1 schritt in die richtung

        # Prüfen ob links ein möglicher pfad ist und rekursiv aufrufen
        possible_path = direction.rot_l()
        new_pos = pos + possible_path
        if in_range(new_pos) and m[new_pos[0]][new_pos[1]] == ".":
            walk_straight(possible_path, new_pos,
                          cur_score + 1)  #+1001 weil 100 für die drehung und 1 schritt in die richtung

        #weiter gehen
        pos = pos + direction
        cur_score += 1
        #Falls Ziel gefunden Score speichern
        if in_range(pos) and m[pos[0]][pos[1]] == "S":
            wins.append(cur_score)
            return


walk_straight(T((0, 1)), T((0, 0)), 0)
print(visited)
print(min(wins))
