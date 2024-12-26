#Idee:
#anstatt 3er kombinationen müssen jetzt alle möglichkeiten bedacht werden
#Rekusiver ansatz, ab einem Punkt alle möglichkeiten betrachten

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

#Rekursion sucht alle möglichen kombinationen von lan Partys( voll vernetzten pcs)
lan_partys = set()
def find_connections(pc, lan_party):
    party = tuple(sorted(lan_party))
    if party in lan_partys: #Rekursions abbruch, wenn lan party bereits in dem set ist
        return
    lan_partys.add(party)
    for pcx in connections[pc]:
        if pcx in lan_party:# pc bereits in dem neuen set
            continue
        if not lan_party <= connections[pcx]: # <= zwischen 2 sets bedeutet alle items aus dem ersten set sind in dem zweiten
            continue                          # Prüft ob alle nachbarn des neuen pcs in dem aktuellen set sind. Abbruch, wenn nicht
        c_lan_party = lan_party.copy()
        c_lan_party.add(pcx)
        find_connections(pcx, c_lan_party)


for pc in connections:
    find_connections(pc, {pc})


#Ausgabe Formatieren
out = ""
for pc in sorted(max(lan_partys, key=len)):#Längste element nehmen
    out += f"{pc},"
print(out.strip(","))





