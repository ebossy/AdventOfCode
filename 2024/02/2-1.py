A = []

with open("2-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for zeile in datei:
        # Entferne Leerzeichen und Zeilenumbrüche
        zeile = zeile.strip()

        # Teile die Zeile nach Leerzeichen
        zahlen = zeile.split()
        zahlen = [int(x) for x in zahlen]
        A.append(zahlen)

#Try all cases and if its unsafe add up
unsafe = 0
for i in A:
    isincreasing = None
    done = False
    for j in range(len(i) - 1):
        if done:
            break
        if i[j] == i[j + 1]:
            unsafe += 1
            done = True
            break
        elif isincreasing is None:
            if i[j] > i[j + 1]:
                isincreasing = False
            else:
                isincreasing = True
        if isincreasing:
            if (i[j + 1] - i[j]) > 3 or i[j + 1] < i[j]:
                unsafe += 1
                done = True
                break
        else:
            if (i[j] - i[j + 1]) > 3 or i[j + 1] > i[j]:
                unsafe += 1
                done = True
                break

print(len(A) - unsafe)

