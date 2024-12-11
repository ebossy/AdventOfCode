from collections import defaultdict

numbers = defaultdict(int)
with open("11-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        for key in line.strip().split():
            numbers[key] += 1

blinks = 75

for q in range(blinks):
    new_numbers = defaultdict(int)
    for key in numbers:
        if key == "0":
            new_numbers["1"] += 1*numbers[key]
        elif len(key) % 2 == 0:
            new_numbers[key[:len(key) // 2]] += 1*numbers[key]
            new_numbers[str(int(key[len(key)//2:]))] += 1*numbers[key]
        else:
            new_numbers[str(int(key)*2024)] += 1*numbers[key]
    numbers = new_numbers

summary = 0
for key in numbers:
    summary += numbers[key]
print(summary)