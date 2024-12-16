import re
tokens = 0

#read each machine
for block in open("13-1.txt").read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"(\d+)", block))
    px += 10000000000000
    py += 10000000000000
    x1 = (px*by-py*bx)/(ax*by-ay*bx)
    x2 = (px-ax*x1)/bx
    #has to be integers no "half button presses" allowed
    if x1%1==0 and x2%1==0:
        tokens += int(x1*3+x2)


print(tokens)

