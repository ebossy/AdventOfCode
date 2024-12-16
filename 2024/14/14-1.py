bots_map = []
wide = 101
tall = 103

#create map
for i in range(tall):
    tmp=[]
    for j in range(wide):
        tmp.append(0)
    bots_map.append(tmp)

#method that gets pos with velocity and seconds
def get_new_pos(px, py, vx, vy, sec):
    new_px = (px + vx * sec)%wide
    new_py = (py + vy * sec)%tall
    return new_px, new_py

#put all pos in the map
import re
for block in open("14-1.txt").read().split("\n"):
    px, py, vx, vy = map(int ,re.findall(r"(-?\d+)", block))
    new_px, new_py = get_new_pos(px, py, vx, vy, 100)
    bots_map[new_py][new_px] += 1

#count the bots in the quarters
q=[0,0,0,0]
for i in range(tall):
    for j in range(wide):
        if i < tall//2 and j < wide//2:
            q[0] += bots_map[i][j]
        if i < tall//2 and j > wide//2:
            q[1] += bots_map[i][j]
        if i > tall//2 and j < wide//2:
            q[2] += bots_map[i][j]
        if i > tall//2 and j > wide//2:
            q[3] += bots_map[i][j]
print(q)
#put the quarters in the Formula
print(q[0]*q[1]*q[2]*q[3])

