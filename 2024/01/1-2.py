A = []
B = []

with open("1-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for zeile in datei:
        # Entferne Leerzeichen und Zeilenumbrüche
        zeile = zeile.strip()

        # Teile die Zeile nach Leerzeichen
        zahlen = zeile.split()

        A.append(int(zahlen[0]))
        B.append(int(zahlen[1]))

#put the numbers and their frequenzy in a dict and use formula of aoc website
from collections import Counter

A1 = Counter(A)
B1 = Counter(B)
total_similarity = 0

for i in A1:
    if i in B1:
        total_similarity += (i * B1[i]) * A1[i]

print(total_similarity)
