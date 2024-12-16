
wide = 101
tall = 103




def get_new_pos(px, py, vx, vy, sec):
    new_px = (px + vx * sec)%wide
    new_py = (py + vy * sec)%tall
    return new_px, new_py

#items of worst score
worst_score = 10**18
worst_sec = 0
worst_map = []

#items of best score
best_score = 0
best_sec = 0
best_map = []

import re
#try x Seconds and get the best and worst score(this is the whole part 1 code)
for sec in range(tall * wide):
    bots_map = []
    for i in range(tall):
        tmp = []
        for j in range(wide):
            tmp.append(0)
        bots_map.append(tmp)
    for block in open("14-1.txt").read().split("\n"):
        px, py, vx, vy = map(int ,re.findall(r"(-?\d+)", block))
        new_px, new_py = get_new_pos(px, py, vx, vy, sec)
        bots_map[new_py][new_px] += 1
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
    score = q[0]*q[1]*q[2]*q[3]
    #check and update best/worst score
    if score < worst_score:
        worst_score = score
        worst_sec = sec
        worst_map = bots_map
    if score > best_score:
        best_score = score
        best_sec = sec
        best_map = bots_map

#worst sec ist the answer to part 2
print("worst",worst_score, worst_sec)
print("best", best_score, best_sec)

from PIL import Image
def make_pixel_pic(width, height, data, name):
    # Create a new image
    img = Image.new('RGB', (width, height), (255, 255, 255))
    pixels = img.load()

    # Set the pixel colors based on the data
    for y in range(height):
        for x in range(width):
            if data[y][x] == 0:
                pixels[x, y] = (255, 255, 255)
            else:
                pixels[x, y] = (0, 0, 0)

    # Save the image
    img.save(f'{name}.png')
#print both pictures to look which ones has the tree
make_pixel_pic(wide, tall, best_map, 'best')
make_pixel_pic(wide, tall, worst_map, 'worst')