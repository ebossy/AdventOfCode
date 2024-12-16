num=[]
op = []
with open("7-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        tmp1, tmp2 =line.split(":")
        num.append(tmp1)
        op.append(tmp2.strip().split(" "))

#Combinations of + and * are shown as Binary numbers
#Try all possible Combinations until it works or none does
summary = 0
for i in range(len(num)):
    length = 2 ** (len(op[i]) - 1)
    stellen = len(op[i])-1
    for k in range(length):
        tmp = int(op[i][0])
        binary = format(k,f'0{stellen}b')
        for j in range(len(binary)):
            if binary[j] == '01':
                tmp += int(op[i][j+1])
            else:
                tmp *= int(op[i][j+1])
        if tmp == int(num[i]):
            summary += int(num[i])
            break

print(summary)

