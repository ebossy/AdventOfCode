#Idee:
#-Alle gültigen mul finden Abspeichern
#-muls durchiterieren und ergebnisse summieren

raw = ""
with open("3-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for zeile in datei:
         raw += zeile

import re #Regex für übereinstimmung
pattern = r"mul\((-?\d+),(-?\d+)\)" #Regex für alle Gültigen Mul als Tuple speichern (Wegen klammern um die zahlen)
matches = re.findall(pattern, raw) #finden der Tuple
summary = 0
for match in matches: #tuple iterieren
    summary += int(match[0])*int(match[1]) # String zahlen in Integer parsen
print(summary)
