pairs = []
orders = []
first_data = True
with open("5-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        if line == "":
            first_data = False
        elif first_data:
            pairs.append(line.split("|"))
        else:
            orders.append(line.split(","))


#seperate the pairs that matter and remove 01 by one until no pairs are left, if pair is removable

summary = 0
for order in orders:
    orderRelevantPairs = [paar for paar in pairs if paar[0] in order and paar[1] in order]
    r = [x[1] for x in orderRelevantPairs]
    for i in range(len(order)):
        if order[i] not in r:
            orderRelevantPairs = [paar for paar in orderRelevantPairs if paar[0] != order[i]]
            r = [x[1] for x in orderRelevantPairs]
        else: break
        if len(orderRelevantPairs) == 0:
            summary += int(order[len(order)//2])
            break


print(summary)

