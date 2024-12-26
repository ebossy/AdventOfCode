#Idee:
# erstmal rauten zählen und dann an die richtige Liste anhängen
# Listen durch Iterieren und mögliche Kombinationen zählen

#Daten einlesen und in die richtigen Listen einfügen
keys = []
locks = []
with open("25-1.txt", "r") as file:
    for block in file.read().split("\n\n"):
        tmp = [-1,-1,-1,-1,-1]
        for line in block.split("\n"):
            for i in range(len(line)):
                if line[i] == "#":
                    tmp[i] += 1
        if block[0] == "#":# wenn erstes zeichen ein # ist es immer ein schloss
            locks.append(tmp)
        else:
            keys.append(tmp)

#Funktion guckt, ob ein Schlüssel mit einem Schloss überlappen und return 1 bei keiner Überlappung und 0 Bei Überlappung
def check_lock(lock, key):
    for i in range(len(key)):
        if key[i] > 5-lock[i]:
            return 0
    return 1


#durch Iterieren und summe ziehen
summary = 0
for lock in locks:
    for key in keys:
        summary += check_lock(lock, key)
print(summary)