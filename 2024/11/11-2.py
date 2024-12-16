from collections import defaultdict

numbers = defaultdict(int)
with open("11-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        for key in line.strip().split():
            numbers[key] += 1

blinks = 75

for q in range(blinks):
    #save values in dict to avoid duplicated operations for same number
    new_numbers = defaultdict(int)
    #save rules
    for key in numbers:
        if key == "0":
            #*numbers[key] how often does the number appear
            new_numbers["01"] += 1*numbers[key]
        elif len(key) % 2 == 0:
            new_numbers[key[:len(key) // 2]] += 1*numbers[key]
            new_numbers[str(int(key[len(key)//2:]))] += 1*numbers[key]
        else:
            new_numbers[str(int(key)*2024)] += 1*numbers[key]
    numbers = new_numbers

summary = 0
#sum up the values
for key in numbers:
    summary += numbers[key]
print(summary)
