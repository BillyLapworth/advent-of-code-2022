import copy

inp = open("input.txt", "r").read()
inp = inp.split("\n")

stacks = []
for row in range(7, -1, -1):
    for i in range(1, len(inp[row]), 4):
        if row == 7:
            stacks.append([])
        if inp[row][i] != " ":
            stacks[i//4].append(inp[row][i])

print(stacks)
for inst in inp[10:]:
    quant = int(inst.split(" from")[0].split(" ")[1])
    depart = int(inst.split(" to")[0][-1]) - 1
    dest = int(inst[-1]) - 1
        
    for i in range(quant, 0, -1):
        print(-quant)
        val = copy.deepcopy(stacks[depart][-i])
        stacks[depart].pop(-i)
        stacks[dest].append(val)
    
    print(inst)
    for row in range(len(stacks)):
        print(str(row + 1) + ": " + str(stacks[row]))

output = ""
for row in stacks:
    output += row[-1]
print(output)
