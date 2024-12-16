disc = []
with open("9-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        for char in line:
            disc.append(char)

#Format the disc
#01=file -01=freespace
switch = 1
longdisc = []
disc_id = 0
for char in disc:
    char = int(char)
    if switch == 1:
        disc_input = str(disc_id)
        disc_id += 1
    else:
        disc_input = "."
    for i in range(char):
        longdisc.append(disc_input)
    switch *= -1

def swap(l, i, j):
    l[i], l[j] = l[j], l[i]


x = 0
y = len(longdisc)-1
#sort data
while True:
    while longdisc[x]!=".":
        x += 1
    while longdisc[y]==".":
        y -= 1
    if x < y:
        swap(longdisc, x, y)
    else:
        break

print(longdisc)


summary = 0
for i,num in enumerate(longdisc):
    if num != ".":
        summary += int(num)*i
print(summary)