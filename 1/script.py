cals = open("input.txt", "r")
cals = cals.read()

cals = cals.split("\n\n")
totals = []
for i in range(len(cals)):
    print(cals[i])
    elf = cals[i].split("\n")
    elf = list(map(int, elf))
    total = sum(elf)
    totals.append(total)

totals.sort(reverse=True)

print(totals[0] + totals[1] + totals[2])
