disc = []
with open("9-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        for char in line:
            disc.append(char)

#Format the disc
#1=file -1=freespace
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




from collections import Counter

data_frequenzy = Counter(longdisc)
data_frequenzy.pop(".")
data_frequenzy = {k: data_frequenzy[k] for k in sorted(data_frequenzy.keys(), reverse=True)}

print(longdisc)
x = 0
while True:

    dot_freq = 0
    pos_dot = 0
    while longdisc[x] != "." and x < len(longdisc)-1:
        x += 1
        pos_dot = x
    while longdisc[x] == "." and x < len(longdisc)-1:
        x += 1
        dot_freq += 1
    if all(x == "." for x in longdisc[x:]):
        break
    start_dot_freq = dot_freq
    while True:
        for key in data_frequenzy.keys():
            #print(dot_freq, data_frequenzy[key])
            if dot_freq >= data_frequenzy[key]:# dot frq =3 wenn 2 slots weg 1 übrig weiter machen !!!
                longdisc = ['.' if item == key else item for item in longdisc]
                for i in range(pos_dot, pos_dot+data_frequenzy[key]):
                    longdisc[i] = key
                pos_dot += data_frequenzy[key]
                #print(longdisc)
                dot_freq -= data_frequenzy[key]
                data_frequenzy.pop(key)
                break
        if start_dot_freq == dot_freq or dot_freq == 0:
            break

    #print(dot_freq)
    print(longdisc)


summary = 0
for i,num in enumerate(longdisc):
    if num != ".":
        summary += int(num)*i
print(summary)