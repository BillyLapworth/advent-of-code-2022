inp = open("input.txt", "r").read()
inp = inp.split("\n")

total = 0
for row in inp:
    elves = row.split(",")
    lb0 = int(elves[0].split("-")[0])
    ub0 = int(elves[0].split("-")[1])
    lb1 = int(elves[1].split("-")[0])
    ub1 = int(elves[1].split("-")[1])

    #print(row)
    if (lb1 <= ub0 and ub1 >= lb0) or (lb1 >= ub0 and ub1 <= lb0):
        #print("overlaps")
        total += 1
    else:
        print(row)
        print("doesn't")
        pass

print(total)
