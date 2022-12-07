guide = open("input.txt", "r").read()
guide = guide.split("\n")

total = 0
for row in guide:
    opp = ord(row[0]) - 65
    if row[2] == "X":
        total += ((opp - 1)  % 3) + 1
    if row[2] == "Y":
        total += opp + 1 + 3
    if row[2] == "Z":
        total += 6
        total += ((opp + 1) % 3) + 1

print(total)
