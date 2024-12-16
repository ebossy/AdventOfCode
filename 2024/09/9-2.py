disc = []
longdisc = []
with open("9-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        for char in line:
            disc.append(int(char))

#Format the disc
#01=file -01=freespace
switch = 1
longdisc = []
disc_id = 0
for char in disc:
    char = int(char)
    if switch == 1:
        disc_input = disc_id
        disc_id += 1
    else:
        disc_input = "."
    for i in range(char):
        longdisc.append(disc_input)
    switch *= -1

from collections import Counter
data_frequenzy = Counter(longdisc)
data_frequenzy.pop(".")
data_frequenzy = {k: data_frequenzy[k] for k in sorted(data_frequenzy.keys(), reverse=True)}

print(data_frequenzy)
#sort data
for key in data_frequenzy:
    #hierdrin alle punkte iterieren
    print(key)
    x = 0
    while True:
        #print(key)
        dot_freq = 0
        pos_dot = 0
        while longdisc[x] != "." and x < len(longdisc) - 1:
            x += 1
            pos_dot = x
        while longdisc[x] == "." and x < len(longdisc) - 1:
            x += 1
            dot_freq += 1
        if dot_freq >= data_frequenzy[key] and longdisc.index(key)>pos_dot:
            longdisc = ['.' if item == key else item for item in longdisc]
            for i in range(pos_dot, pos_dot + data_frequenzy[key]):
                longdisc[i] = key

            break
        if all(x == "." for x in longdisc[x:]):
            break

print(longdisc)


summary = 0
for i,num in enumerate(longdisc):
    if num != ".":
        summary += int(num)*i
print(summary)