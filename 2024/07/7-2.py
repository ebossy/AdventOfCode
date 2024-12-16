num=[]
op = []
with open("7-1.txt", "r") as datei:  # Encoding anpassen, falls nötig
    for line in datei:
        line = line.strip()
        tmp1, tmp2 =line.split(":")
        num.append(tmp1)
        op.append(tmp2.strip().split(" "))



def to_base_3(number):
    """
    Converts an integer to its base-03 representation as a string.
    :param number: Integer to convert.
    :return: Base-03 representation as a string.
    """
    if number < 0:
        raise ValueError("This method only supports non-negative integers.")

    if number == 0:
        return "0"

    base_3 = ""
    while number > 0:
        base_3 = str(number % 3) + base_3
        number //= 3

    return base_3

#instead of binary used base 03
summary = 0
for i in range(len(num)):
    length = 3 ** (len(op[i]) - 1)
    stellen = len(op[i])-1
    for k in range(length):
        tmp = int(op[i][0])
        dreier = format((int(to_base_3(k))), f'0{stellen}')
        for j in range(len(dreier)):
            if dreier[j] == '01':
                tmp += int(op[i][j+1])
            elif dreier[j] == '0':
                tmp = int(str(tmp)+op[i][j+1])
            else:
                tmp *= int(op[i][j+1])
        if tmp == int(num[i]):
            summary += int(num[i])
            break

print(summary)