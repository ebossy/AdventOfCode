#Idee:
#-do und dont müssen an richtiger Stelle berücksichtigt werden
#-do und dont mit in matches packen damit reihenfolge bleibt
#-beim iterien abfragen, ob es ein do oder dont ist
#-mithilfe von einem bool entscheiden, ob die mul operation ausgeführt wird

raw = ""
with open("3-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for zeile in datei:
         raw += zeile

import re
pattern_mul = r"mul\(-?\d+,-?\d+\)|do\(\)|don't\(\)"
#Regex für alle Gültigen Mul (diesmal ohne direkt mit zahlen)
#do und dont mit in matches
pattern_num = r"(-?\d+)"
#weil diesmal die zahlen nicht direkt im tuple sind für später

matches = re.findall(pattern_mul, raw) #finden der Tuple
summary = 0
enabled = True # mit True initialisieren

for match in matches:
    if match == "don't()":
        enabled = False
        continue
    if match == "do()":
        enabled = True
        continue
    if enabled:
        numbers = re.findall(pattern_num, match) #zahlen im tuple speichern
        summary += int(numbers[0]) * int(numbers[1]) # String zahlen in Integer parsen
print(summary)
