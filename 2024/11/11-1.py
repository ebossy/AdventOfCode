numbers = []
with open("11-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        for num in line.strip().split():
            numbers.append(num)

blinks = 25

for q in range(blinks):
    new_numbers = []
    for num in numbers:
        if num == "0":
            new_numbers.append("1")
        elif len(num)%2==0:
            new_numbers.append(num[:len(num)//2])
            new_numbers.append(str(int(num[len(num)//2:])))
        else:
            new_numbers.append(str(int(num)*2024))
    numbers = new_numbers

print(len(numbers))

