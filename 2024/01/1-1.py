# %%
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

total_distance = 0


#sort to find lowest of each and so on and get distance
A.sort()
B.sort()
for i in range(len(A)):
    tmp = A[i]-B[i]
    if tmp<0: tmp*=-1
    total_distance += tmp

print(total_distance)

