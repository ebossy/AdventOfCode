#Idee:
# gucken ob die ersten x stellen ein pattern entsprechen
# wenn ja diese stellen raus holen und für den restlichen string wiederholen

# pattern und designs trennen
with open("19-1.txt", "r") as file:
    pattern, designs = file.read().split("\n\n")

#Formatieren
pattern = [p for p in pattern.split(", ")]
designs = [d for d in designs.split("\n")]


#Rekursiver aufruf um zu gucken ob ein design(rest design) gültig ist
def pattern_legitness(design, lenght):
    legitness = False
    while True:
        if design == "" or legitness: # Abbruch bedingung der rekursion (Lösung)
                                      # das or sorgt dafür, # dass nicht unnötig viele Rekursionen gemacht werden sobald 1 gültige kombination gefunden wurde
            return True

        if lenght <= 0: # Abbruch bedingung der Rekursion (Keine Lösung)
            return legitness
        if design[:lenght] in pattern:# ersten x stellen entsprechen eines patterns
            legitness = pattern_legitness(design, lenght-1)
            design = design[lenght:] # vorhandenen teil entfernen
            lenght = len(design) # rest länge
        else:
            lenght -= 1


#sumieren
summary = 0
for design in designs:
    if pattern_legitness(design, len(design)):
        summary += 1

print(summary)
print(pattern, designs)
