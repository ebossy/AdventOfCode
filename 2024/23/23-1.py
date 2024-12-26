#Idee:
#alle verbindungen in einem dict abbilden
#Iterative herausfinden ob 3 pcs sich gegenseitig in ihrem dict haben

#Daten einlesen
pairs = []
with open("23-1.txt", "r") as file:
    for line in file.read().split("\n"):
        pairs.append(line.split("-"))

#dict bilden
connections = {}
for pair in pairs:
    if pair[0] not in connections:
        connections[pair[0]] = set()
    if pair[1] not in connections:
        connections[pair[1]] = set()
    connections[pair[0]].add(pair[1])
    connections[pair[1]].add(pair[0])

#alle 3er verbind engen herausfinden
three_i_c = set()
for pcx in connections:
    for pcy in connections[pcx]:
        for pcz in connections[pcy]:
            if pcx != pcz and pcx in connections[pcz]:#3er pc darf nicht erster sein da es sonst nur eine 2er verbindung wäre
                three_i_c.add(tuple(sorted([pcx, pcy, pcz]))) #dem set ein sortiertes tuple übergeben, damit das set automatisch dopplungen verhindert

#filtern welche mit t anfangen
three_with_t = []
for three in three_i_c:
    if three[0].startswith("t") or three[1].startswith("t") or three[2].startswith("t"):
        three_with_t.append(three)

print(len(three_with_t))





