#Idee
# alle Fälle druch gucken deshalb die Abbruchbedingung abgeändert
# anstatt True wird der counter hoch gezählt
# Memoisierung für eine bessere Laufzeit

from functools import cache

# pattern und designs trennen
with open("19-1.txt", "r") as file:
    pattern, designs = file.read().split("\n\n")

#Formatieren
pattern = [p for p in pattern.split(", ")]
designs = [d for d in designs.split("\n")]


@cache #Memoisierung für laufzeit
def pattern_legitness(design, lenght):
    inner_sum = 0 # summ die möglichkeiten mitzählt
    while True:
        if design == "": # bei erfolg 1 möglichkeit dazu
            inner_sum += 1

        if lenght <= 0: # abbruchbedingung innersum wird nach außen gegeben
            return inner_sum
        # print(design[:lenght])
        if design[:lenght] in pattern:
            inner_sum += pattern_legitness(design, lenght - 1) # innersum wird mit der Rekursion hoch gezählt
            design = design[lenght:]
            lenght = len(design)
        else:
            lenght -= 1


summary = 0
for design in designs:
    summary += pattern_legitness(design, len(design))

print(summary)
